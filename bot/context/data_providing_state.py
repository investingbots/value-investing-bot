import logging
from time import sleep
from wrapt import synchronized

from bot import OperationalException
from bot.events.observer import Observer
from bot.context.bot_state import BotState
from bot.context.bot_context import BotContext
from bot.data.data_provider_manager import ConfigDataProviderManager
from bot.context.analyzing_state import AnalyzingState


logger = logging.getLogger(__name__)


class DataProvidingState(BotState, Observer):

    def __init__(self):
        super(DataProvidingState, self).__init__()

        logger.info("Initializing data providing state ...")

        # Initialize the manager
        context = BotContext()

        self._manager = ConfigDataProviderManager(context.config)
        self._manager.add_observer(self)

        self._updated = False
        self._started = False

    def _clean_up(self):

        if self._manager.processing:
            self._manager.stop_data_providers()

        self._updated = False
        self._started = False

    def run(self):
        logger.info("Data providing state started ...")

        if not self._started:
            self._manager.start_data_providers()

        # Sleep till updated
        while not self._updated:
            sleep(1)

        if self._updated:

            # Collect all data from the data providers
            data_entries = {}

            for data_provider in self._manager.registered_data_providers:
                data_entries[data_provider.get_id()] = data_provider.data

            context = BotContext()
            context.raw_data = data_entries
            context.transition_to(AnalyzingState)
        else:
            raise OperationalException("Abruptly ended out of run state")

    def stop(self):
        pass

    def reconfigure(self):
        self._clean_up()

    @synchronized
    def update(self, observable, **kwargs) -> None:
        self._updated = True
