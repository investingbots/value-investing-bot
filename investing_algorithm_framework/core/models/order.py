import logging
from abc import abstractmethod

from investing_algorithm_framework.core.models import OrderStatus, \
    OrderType, OrderSide
from investing_algorithm_framework.core.exceptions import OperationalException
logger = logging.getLogger(__name__)


class Order:

    def __init__(
        self,
        target_symbol,
        trading_symbol,
        type,
        side,
        status,
        amount_trading_symbol=None,
        amount_target_symbol=None,
        price=None,
        initial_price=None,
        closing_price=None,
        reference_id=None
    ):
        self.reference_id = reference_id
        self.target_symbol = target_symbol
        self.trading_symbol = trading_symbol
        self.price = price
        self.amount_trading_symbol = amount_trading_symbol
        self.amount_target_symbol = amount_target_symbol
        self.side = OrderSide.from_value(side)
        self.type = OrderType.from_value(type)
        self.status = OrderStatus.from_value(status)
        self.initial_price = initial_price
        self.closing_price = closing_price

        self._initialize_order_amount()
        self._validate_initial_price_attribute()
        self._validate_amount()
        self._validate_price_attribute()
        self._validate_closing_price_attribute()

    def _validate_price_attribute(self):

        if OrderStatus.SUCCESS.equals(self.status) \
                or OrderStatus.PENDING.equals(self.status):

            if self.price is None:
                raise OperationalException(
                    "Price attribute is not set for order"
                )

    def _validate_initial_price_attribute(self):

        if OrderStatus.SUCCESS.equals(self.status) \
                or OrderStatus.CLOSED.equals(self.status):

            if self.initial_price is None:
                raise OperationalException(
                    "Initial price attribute is not set for order"
                )

    def _validate_closing_price_attribute(self):

        if OrderStatus.CLOSED.equals(self.status):

            if self.closing_price is None:
                raise OperationalException(
                    "Closing price attribute is not set for order"
                )

    def _validate_amount(self):

        if OrderType.MARKET.equals(self.type):

            if self.amount_target_symbol is None:
                raise OperationalException(
                    "Amount target symbol attribute is "
                    "not set for market sell order"
                )
        else:
            if self.amount_target_symbol is None:
                raise OperationalException(
                    "Amount target symbol attribute is "
                    "not set for limit order"
                )

            if self.amount_trading_symbol is None:
                raise OperationalException(
                    "Amount trading symbol attribute is "
                    "not set for limit order"
                )

    def _initialize_order_amount(self):
        price = 0

        if (OrderStatus.SUCCESS.equals(self.status)
            or OrderStatus.CLOSED.equals(self.status)) \
                and self.initial_price is not None:
            price = self.initial_price
        elif self.price is not None:
            price = self.price

        if OrderType.LIMIT.equals(self.type):

            if self.amount_trading_symbol is not None:
                self.amount_target_symbol = \
                    price / self.amount_trading_symbol
            elif self.amount_target_symbol is not None:
                self.amount_trading_symbol = \
                    price * self.amount_target_symbol

        if OrderType.MARKET.equals(self.type):

            if OrderStatus.SUCCESS.equals(self.status) \
                    or OrderStatus.CLOSED.equals(self.status):
                self.amount_trading_symbol = \
                    price * self.amount_target_symbol

    def get_reference_id(self):
        return self.reference_id

    def get_target_symbol(self):
        return self.target_symbol

    def get_trading_symbol(self):
        return self.trading_symbol

    def get_initial_price(self):
        return self.initial_price

    def get_price(self):

        if OrderStatus.CLOSED.equals(self.status):
            return self.closing_price

        return self.price

    def get_closing_price(self):
        return self.closing_price

    def get_side(self):
        return self.side

    def get_status(self) -> OrderStatus:
        return self.status

    def get_type(self):
        return self.type

    def get_amount_target_symbol(self):
        return self.amount_target_symbol

    def get_amount_trading_symbol(self):
        return self.amount_trading_symbol

    @staticmethod
    def from_dict(data: dict):
        return Order(
            reference_id=data.get("reference_id", None),
            target_symbol=data.get("target_symbol", None),
            trading_symbol=data.get("trading_symbol", None),
            price=data.get("price", None),
            initial_price=data.get("initial_price", None),
            closing_price=data.get("closing_price", None),
            amount_trading_symbol=data.get("amount_trading_symbol", None),
            amount_target_symbol=data.get("amount_target_symbol", None),
            status=data.get("status", None),
            type=data.get("type", None),
            side=data.get("side", None)
        )

    @abstractmethod
    def to_dict(self):
        return {
            "reference_id": self.get_reference_id(),
            "target_symbol": self.get_target_symbol(),
            "trading_symbol": self.get_trading_symbol(),
            "amount_trading_symbol": self.get_amount_trading_symbol(),
            "amount_target_symbol": self.get_amount_target_symbol(),
            "price": self.get_price(),
            "initial_price": self.get_initial_price(),
            "closing_price": self.get_closing_price(),
            "status": self.get_status(),
            "order_type": self.get_type(),
            "order_side": self.get_side()
        }

    def split(self, amount):
        pass

    def repr(self, **fields) -> str:
        """
        Helper for __repr__
        """

        field_strings = []
        at_least_one_attached_attribute = False

        for key, field in fields.items():
            field_strings.append(f'{key}={field!r}')
            at_least_one_attached_attribute = True

        if at_least_one_attached_attribute:
            return f"<{self.__class__.__name__}({','.join(field_strings)})>"

        return f"<{self.__class__.__name__} {id(self)}>"

    def to_string(self):
        return self.repr(
            reference_id=self.get_reference_id(),
            status=self.get_status(),
            initial_price=self.get_initial_price(),
            price=self.get_price(),
            closing_price=self.get_closing_price(),
            order_side=self.get_side(),
            order_type=self.get_type(),
            amount_target_symbol=self.get_amount_target_symbol(),
            amount_trading_symbol=self.get_amount_trading_symbol()
        )

    def __repr__(self):
        return self.to_string()
