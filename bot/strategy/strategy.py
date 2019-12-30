import logging
from pandas import DataFrame
from typing import Dict, Any, List
from abc import ABC, abstractmethod

from bot.events.observable import Observable
from bot.events.observer import Observer

logger = logging.getLogger(__name__)


class Strategy(ABC):

    def __init__(self, config: Dict[str, Any]):
        self._config = config
        self._apply_populate_data: bool = True
        self._apply_buy_advice: bool = True
        self._apply_sell_advice: bool = True
        self._analyzed_data: DataFrame = None
        self._meta_data: Dict[str, Any] = None

    @abstractmethod
    def validate_data(self, data_provider_id: str, raw_data: DataFrame) -> bool:
        """
        Use this function to validate the raw data in the given DataFrame.
        When this hook returns false, the strategy will be skipped
        :return: True, if data can be used to apply strategy, else False
        """
        pass

    @abstractmethod
    def populate_data(self, raw_data: DataFrame) -> DataFrame:
        """
        Use this function to change the raw data DataFrame. If not used, consider changing the flag
        'apply_populate_data' to False.
        :return: custom populated DataFrame
        """

    @abstractmethod
    def get_buy_advice(self, data: DataFrame, meta_data: Dict) -> DataFrame:
        """
        Use this function to change the raw data DataFrame. If not used, consider changing the flag
        'apply_populate_data' to False.
        :return: custom populated DataFrame
        """
        pass

    @abstractmethod
    def get_sell_advice(self, data: DataFrame, meta_data: Dict) -> DataFrame:
        """
        Use this function to change the raw data DataFrame. If not used, consider changing the flag
        'apply_populate_data' to False.
        :return: custom populated DataFrame
        """
        pass

    @property
    def apply_populate_data(self) -> bool:
        return self._apply_populate_data

    @apply_populate_data.setter
    def apply_populate_data(self, flag: bool) -> None:
        self._apply_populate_data = flag

    @property
    def apply_buy_advice(self) -> bool:
        return self._apply_buy_advice

    @apply_buy_advice.setter
    def apply_buy_advice(self, flag: bool) -> None:
        self._apply_buy_advice = flag

    @property
    def apply_sell_advice(self) -> bool:
        return self._apply_sell_advice

    @apply_sell_advice.setter
    def apply_sell_advice(self, flag: bool) -> None:
        self._apply_sell_advice = flag

    @abstractmethod
    def get_id(self) -> str:
        pass

    def _extract_sell_indicators(self, data: DataFrame) -> List[Dict[str, Any]]:
        pass

    def _extract_buy_indicators(self, data: DataFrame) -> List[Dict[str, Any]]:
        pass

    def start(self, data_provider_id: str, raw_data: DataFrame) -> None:
        logger.info("Start strategy {}".format(self.get_id()))

        data_frame = raw_data
        meta_data = {}

        # check if strategy wants to validate the data
        if self.validate_data(data_provider_id, raw_data):

            if self.apply_populate_data:
                data_frame = self.populate_data(data_frame)

            if self.apply_buy_advice:
                data_frame = self.get_buy_advice(data_frame, meta_data)

            if self.apply_sell_advice:
                data_frame = self.get_sell_advice(data_frame, meta_data)

            self._analyzed_data = data_frame
            self._meta_data = meta_data
        else:
            self._analyzed_data = None
            self._meta_data = None


class ObservableStrategy(Observable, Strategy):

    def __init__(self, subject_strategy: Strategy):
        super(ObservableStrategy, self).__init__()
        self._subject_strategy = subject_strategy

    def validate_data(self, data_provider_id: str, raw_data: DataFrame) -> bool:
        return self._subject_strategy.validate_data(data_provider_id, raw_data)

    def populate_data(self, raw_data: DataFrame) -> DataFrame:
        return self._subject_strategy.populate_data(raw_data)

    def get_buy_advice(self, data: DataFrame, meta_data: Dict) -> DataFrame:
        return self._subject_strategy.get_buy_advice(data, meta_data)

    def get_sell_advice(self, data: DataFrame, meta_data: Dict) -> DataFrame:
        return self._subject_strategy.get_sell_advice(data, meta_data)

    def get_id(self) -> str:
        return self._subject_strategy.get_id()

    def add_observer(self, observer: Observer) -> None:
        super(ObservableStrategy, self).add_observer(observer)

    def remove_observer(self, observer: Observer) -> None:
        super(ObservableStrategy, self).remove_observer(observer)
