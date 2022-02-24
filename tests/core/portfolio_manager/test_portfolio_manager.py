from investing_algorithm_framework import OrderSide, OrderType, OrderStatus, \
    Position, Portfolio
from tests.resources import TestBase, TestOrderAndPositionsObjectsMixin


class Test(TestOrderAndPositionsObjectsMixin, TestBase):

    def setUp(self):
        super(Test, self).setUp()
        self.start_algorithm()

    def test_identifier(self):
        portfolio_manager = self.algo_app.algorithm\
            .get_portfolio_manager('default')
        self.assertIsNotNone(portfolio_manager.get_identifier())
        self.assertEqual("default", portfolio_manager.get_identifier())

    def test_get_trading_symbol(self):
        portfolio_manager = self.algo_app.algorithm \
            .get_portfolio_manager('default')
        self.assertIsNotNone(portfolio_manager.get_trading_symbol(self.algo_app.algorithm))
        self.assertEqual("USDT", portfolio_manager
                         .get_trading_symbol(self.algo_app.algorithm))

    def test_get_positions(self):
        portfolio_manager = self.algo_app.algorithm \
            .get_portfolio_manager('default')

        self.assertIsNotNone(
            portfolio_manager.get_positions(self.algo_app.algorithm)
        )

        positions = portfolio_manager.get_positions(self.algo_app.algorithm)
        self.assertTrue(isinstance(positions[0], Position))

    def test_get_portfolio(self):
        portfolio_manager = self.algo_app.algorithm \
            .get_portfolio_manager('default')

        self.assertIsNotNone(
            portfolio_manager.get_portfolio(self.algo_app.algorithm)
        )

        portfolio = portfolio_manager.get_portfolio(self.algo_app.algorithm)
        self.assertTrue(isinstance(portfolio, Portfolio))

    def test_get_orders(self):
        portfolio_manager = self.algo_app.algorithm \
            .get_portfolio_manager('default')

        self.assertIsNotNone(
            portfolio_manager.get_orders(self.algo_app.algorithm)
        )

    def test_initialize(self):
        self.assertTrue(
            self.algo_app.algorithm.get_portfolio_manager().initialize_has_run
        )

    def test_create_limit_buy_order(self):
        portfolio_manager = self.algo_app.algorithm\
            .get_portfolio_manager('default')

        order = portfolio_manager.create_order(
            order_type=OrderType.LIMIT.value,
            order_side=OrderSide.BUY.value,
            amount_target_symbol=1,
            target_symbol=self.TARGET_SYMBOL_A,
            price=self.BASE_SYMBOL_A_PRICE,
            algorithm_context=None
        )

        self.assertIsNotNone(order)
        self.assert_is_limit_order(order)

    def test_create_limit_sell_order(self):
        portfolio_manager = self.algo_app.algorithm\
            .get_portfolio_manager('default')

        order = portfolio_manager.create_order(
            order_type=OrderType.LIMIT.value,
            order_side=OrderSide.SELL.value,
            amount_target_symbol=1,
            target_symbol=self.TARGET_SYMBOL_A,
            price=self.BASE_SYMBOL_A_PRICE,
            algorithm_context=None
        )

        self.assertIsNotNone(order)
        self.assert_is_limit_order(order)
