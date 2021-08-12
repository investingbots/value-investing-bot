import json
from tests.resources import TestBase, TestOrderAndPositionsObjectsMixin
from investing_algorithm_framework import PortfolioManager, Order, OrderSide, \
    Position


class PortfolioManagerOne(PortfolioManager):
    trading_currency = "USDT"
    identifier = "KRAKEN"

    def get_initial_unallocated_size(self) -> float:
        return 1000


class PortfolioManagerTwo(PortfolioManager):
    trading_currency = "BUSD"
    identifier = "BINANCE"

    def get_initial_unallocated_size(self) -> float:
        return 2000


SERIALIZATION_DICT = {
    'amount',
    'position_id',
    'executed',
    'id',
    'price',
    'target_symbol',
    'trading_symbol',
    'order_type',
    'order_side',
    'executed',
    'successful',
}


class Test(TestBase, TestOrderAndPositionsObjectsMixin):
    TICKERS = [
        "BTC",
        "DOT",
        "ADA",
        "XRP",
        "ETH"
    ]

    def setUp(self):
        super(Test, self).setUp()
        self.portfolio_manager_one = PortfolioManagerOne()
        self.portfolio_manager_two = PortfolioManagerTwo()
        self.algo_app.algorithm.add_portfolio_manager(
            self.portfolio_manager_one
        )
        self.algo_app.algorithm.add_portfolio_manager(
            self.portfolio_manager_two
        )
        self.algo_app.algorithm.start()

    def tearDown(self):
        super(Test, self).tearDown()

    def test_list_orders(self):
        self.create_buy_orders(5, self.TICKERS, self.portfolio_manager_one)
        self.create_buy_orders(5, self.TICKERS, self.portfolio_manager_two)
        self.create_sell_orders(2, self.TICKERS, self.portfolio_manager_one)
        self.create_sell_orders(2, self.TICKERS, self.portfolio_manager_two)

        positions = Position.query\
            .filter_by(portfolio=self.portfolio_manager_one.get_portfolio())\
            .with_entities(Position.id)

        response = self.client.get(
            f"/api/orders/identifiers/{self.portfolio_manager_one.identifier}"
        )
        self.assert200(response)
        data = json.loads(response.data.decode())

        self.assertEqual(
            Order.query.filter(Order.position_id.in_(positions)).count(),
            len(data["items"])
        )
        self.assertEqual(SERIALIZATION_DICT, set(data.get("items")[0]))

    def test_list_orders_with_target_symbol_query_params(self):
        self.create_buy_orders(5, self.TICKERS, self.portfolio_manager_one)
        self.create_buy_orders(5, self.TICKERS, self.portfolio_manager_two)
        self.create_sell_orders(2, self.TICKERS, self.portfolio_manager_one)
        self.create_sell_orders(2, self.TICKERS, self.portfolio_manager_two)

        query_params = {
            'target_symbol': self.TICKERS[0]
        }

        response = self.client.get(
            f"/api/orders/identifiers/{self.portfolio_manager_one.identifier}",
            query_string=query_params
        )
        self.assert200(response)
        data = json.loads(response.data.decode())

        position_ids = Position.query\
            .filter_by(portfolio=self.portfolio_manager_one.get_portfolio())\
            .with_entities(Position.id)

        self.assertEqual(
            Order.query
                .filter(Order.position_id.in_(position_ids))
                .filter_by(target_symbol=self.TICKERS[0])
                .count(),
            len(data["items"])
        )
        self.assertEqual(SERIALIZATION_DICT, set(data.get("items")[0]))

    def test_list_orders_with_pending_query_params(self):
        self.create_buy_orders(5, self.TICKERS, self.portfolio_manager_one)
        self.create_buy_orders(5, self.TICKERS, self.portfolio_manager_two)
        self.create_sell_orders(2, self.TICKERS, self.portfolio_manager_one)
        self.create_sell_orders(2, self.TICKERS, self.portfolio_manager_two)

        query_params = {
            'pending': True
        }

        response = self.client.get(
            f"/api/orders/identifiers/{self.portfolio_manager_one.identifier}",
            query_string=query_params
        )

        self.assert200(response)
        data = json.loads(response.data.decode())

        self.assertEqual(
            Order.query.filter_by(executed=True).count(),
            len(data["items"])
        )

    def test_list_orders_with_trading_symbol_query_params(self):
        self.create_buy_orders(5, self.TICKERS, self.portfolio_manager_one)
        self.create_buy_orders(5, self.TICKERS, self.portfolio_manager_two)
        self.create_sell_orders(2, self.TICKERS, self.portfolio_manager_one)
        self.create_sell_orders(2, self.TICKERS, self.portfolio_manager_two)

        query_params = {
            'trading_symbol': self.portfolio_manager_one.trading_currency
        }

        response = self.client.get(
            f"/api/orders/identifiers/{self.portfolio_manager_one.identifier}",
            query_string=query_params
        )
        self.assert200(response)
        data = json.loads(response.data.decode())

        position_ids = Position.query \
            .filter_by(portfolio=self.portfolio_manager_one.get_portfolio()) \
            .with_entities(Position.id)

        self.assertEqual(
            Order.query
                .filter(Order.position_id.in_(position_ids))
                .filter_by(
                    trading_symbol=self.portfolio_manager_one.trading_currency
                )
                .count(),
            len(data["items"])
        )
        self.assertEqual(SERIALIZATION_DICT, set(data.get("items")[0]))

    def test_list_orders_with_order_side_query_params(self):
        self.create_buy_orders(5, self.TICKERS, self.portfolio_manager_one)
        self.create_buy_orders(5, self.TICKERS, self.portfolio_manager_two)
        self.create_sell_orders(2, self.TICKERS, self.portfolio_manager_one)
        self.create_sell_orders(2, self.TICKERS, self.portfolio_manager_two)

        query_params = {
            'order_side': OrderSide.BUY.value
        }

        response = self.client.get(
            f"/api/orders/identifiers/{self.portfolio_manager_one.identifier}",
            query_string=query_params
        )

        self.assert200(response)
        data = json.loads(response.data.decode())

        position_ids = Position.query \
            .filter_by(portfolio=self.portfolio_manager_one.get_portfolio()) \
            .with_entities(Position.id)

        self.assertEqual(
            Order.query
                .filter(Order.position_id.in_(position_ids))
                .filter_by(order_side=OrderSide.BUY.value)
                .count(),
            len(data["items"])
        )
        self.assertEqual(SERIALIZATION_DICT, set(data.get("items")[0]))

    def test_all_query_params(self):
        self.create_buy_orders(5, self.TICKERS, self.portfolio_manager_one)
        self.create_buy_orders(5, self.TICKERS, self.portfolio_manager_two)
        self.create_sell_orders(2, self.TICKERS, self.portfolio_manager_one)
        self.create_sell_orders(2, self.TICKERS, self.portfolio_manager_two)

        query_params = {
            'target_symbol': self.TICKERS[0],
            'trading_symbol': self.portfolio_manager_one.trading_currency,
            'order_side': OrderSide.BUY.value
        }

        response = self.client.get(
            f"/api/orders/identifiers/{self.portfolio_manager_one.identifier}",
            query_string=query_params
        )

        self.assert200(response)
        data = json.loads(response.data.decode())

        position_ids = Position.query \
            .filter_by(portfolio=self.portfolio_manager_one.get_portfolio()) \
            .with_entities(Position.id)

        self.assertEqual(
            Order.query
                .filter(Order.position_id.in_(position_ids))
                .filter_by(
                    order_side=OrderSide.BUY.value,
                    trading_symbol=self.portfolio_manager_one.trading_currency,
                    target_symbol=self.TICKERS[0]
                ).count(),
            len(data["items"])
        )
        self.assertEqual(SERIALIZATION_DICT, set(data.get("items")[0]))
