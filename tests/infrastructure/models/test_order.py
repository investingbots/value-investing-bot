# from unittest import TestCase
#
# from investing_algorithm_framework import create_app
#
#
# class TestOrderModel(TestCase):
#
#     def setUp(self):
#         super(TestOrderModel, self).setUp()
#
#     def test_get_reference_id(self):
#         app = create_app(stateless=True)
#         order = app.algorithm.create_order(
#             amount=10, price=10, target_symbol="TEST"
#         )
#         self.assertIsNotNone(order.external_id)
#         self.assertIsNotNone(order.amount)
#         self.assertIsNotNone(order.amount)
#         self.assertIsNotNone(order.price)
#         self.assertIsNotNone(order.target_symbol)
#         self.assertIsNotNone(order.trading_symbol)
#         self.assertIsNotNone(order.created_at)
#         self.assertIsNotNone(order.updated_at)
#         self.assertIsNotNone(order.executed_at)
#         self.assertIsNotNone(order.status)
#
#     def test_get_target_symbol(self):
#         portfolio_manager = self.algo_app.algorithm \
#             .get_portfolio_manager("default")
#
#         self.create_buy_order(
#             amount=10,
#             price=self.get_price(self.TARGET_SYMBOL_A).price,
#             portfolio_manager=portfolio_manager,
#             target_symbol=self.TARGET_SYMBOL_A,
#             reference_id=10
#         )
#
#         portfolio = portfolio_manager.get_portfolio(algorithm_context=None)
#         order = portfolio.get_order(10)
#         self.assertIsNotNone(order.get_target_symbol())
#
#     def test_get_trading_symbol(self):
#         portfolio_manager = self.algo_app.algorithm \
#             .get_portfolio_manager("default")
#
#         self.create_buy_order(
#             amount=10,
#             price=self.get_price(self.TARGET_SYMBOL_A).price,
#             portfolio_manager=portfolio_manager,
#             target_symbol=self.TARGET_SYMBOL_A,
#             reference_id=10
#         )
#
#         portfolio = portfolio_manager.get_portfolio(algorithm_context=None)
#         order = portfolio.get_order(10)
#         self.assertIsNotNone(order.get_trading_symbol())
#
#     def test_get_amount_of_trading_symbol(self):
#         portfolio_manager = self.algo_app.algorithm \
#             .get_portfolio_manager("default")
#
#         self.create_buy_order(
#             amount=10,
#             price=self.get_price(self.TARGET_SYMBOL_A).price,
#             portfolio_manager=portfolio_manager,
#             target_symbol=self.TARGET_SYMBOL_A,
#             reference_id=10
#         )
#
#         portfolio = portfolio_manager.get_portfolio(algorithm_context=None)
#         order = portfolio.get_order(10)
#         self.assertIsNotNone(order.get_amount())
#
#     def test_get_amount_of_target_symbol(self):
#         portfolio_manager = self.algo_app.algorithm \
#             .get_portfolio_manager("default")
#
#         self.create_buy_order(
#             amount=10,
#             price=self.get_price(self.TARGET_SYMBOL_A).price,
#             portfolio_manager=portfolio_manager,
#             target_symbol=self.TARGET_SYMBOL_A,
#             reference_id=10
#         )
#
#         portfolio = portfolio_manager.get_portfolio(algorithm_context=None)
#         order = portfolio.get_order(10)
#         self.assertIsNotNone(order.get_amount())
#
#     def test_get_initial_price(self):
#         portfolio_manager = self.algo_app.algorithm \
#             .get_portfolio_manager("default")
#
#         self.create_buy_order(
#             amount=10,
#             price=self.get_price(self.TARGET_SYMBOL_A).price,
#             portfolio_manager=portfolio_manager,
#             target_symbol=self.TARGET_SYMBOL_A,
#             reference_id=10
#         )
#
#         portfolio = portfolio_manager.get_portfolio(algorithm_context=None)
#         order = portfolio.get_order(10)
#         order.initial_price = 10
#         self.assertIsNotNone(order.get_initial_price())
#
#     def test_get_price(self):
#         portfolio_manager = self.algo_app.algorithm \
#             .get_portfolio_manager("default")
#
#         self.create_buy_order(
#             amount=10,
#             price=self.get_price(self.TARGET_SYMBOL_A).price,
#             portfolio_manager=portfolio_manager,
#             target_symbol=self.TARGET_SYMBOL_A,
#             reference_id=10
#         )
#
#         portfolio = portfolio_manager.get_portfolio(algorithm_context=None)
#         order = portfolio.get_order(10)
#
#         self.assertIsNotNone(order.get_price())
#
#     def test_get_closing_price(self):
#         portfolio_manager = self.algo_app.algorithm \
#             .get_portfolio_manager("default")
#
#         self.create_buy_order(
#             amount=10,
#             price=self.get_price(self.TARGET_SYMBOL_A).price,
#             portfolio_manager=portfolio_manager,
#             target_symbol=self.TARGET_SYMBOL_A,
#             reference_id=10
#         )
#
#         portfolio = portfolio_manager.get_portfolio(algorithm_context=None)
#         order = portfolio.get_order(10)
#         order.closing_price = 10
#         self.assertIsNotNone(order.get_closing_price())
#
#     def test_get_side(self):
#         portfolio_manager = self.algo_app.algorithm \
#             .get_portfolio_manager("default")
#
#         self.create_buy_order(
#             amount=10,
#             price=self.get_price(self.TARGET_SYMBOL_A).price,
#             portfolio_manager=portfolio_manager,
#             target_symbol=self.TARGET_SYMBOL_A,
#             reference_id=10
#         )
#
#         portfolio = portfolio_manager.get_portfolio(algorithm_context=None)
#         order = portfolio.get_order(10)
#         self.assertIsNotNone(order.get_side())
#
#     def test_get_status(self):
#         portfolio_manager = self.algo_app.algorithm \
#             .get_portfolio_manager("default")
#
#         self.create_buy_order(
#             amount=10,
#             price=self.get_price(self.TARGET_SYMBOL_A).price,
#             portfolio_manager=portfolio_manager,
#             target_symbol=self.TARGET_SYMBOL_A,
#             reference_id=10
#         )
#
#         portfolio = portfolio_manager.get_portfolio(algorithm_context=None)
#         order = portfolio.get_order(10)
#         self.assertIsNotNone(order.get_status())
#
#     def test_get_type(self):
#         portfolio_manager = self.algo_app.algorithm \
#             .get_portfolio_manager("default")
#
#         self.create_buy_order(
#             amount=10,
#             price=self.get_price(self.TARGET_SYMBOL_A).price,
#             portfolio_manager=portfolio_manager,
#             target_symbol=self.TARGET_SYMBOL_A,
#             reference_id=10
#         )
#
#         portfolio = portfolio_manager.get_portfolio(algorithm_context=None)
#         order = portfolio.get_order(10)
#         self.assertIsNotNone(order.get_type())
#
#     def test_from_dict_with_symbol(self):
#         order = Order.from_dict(
#             {
#                 "reference_id": 10493,
#                 "symbol": "DOT/USDT",
#                 "amount": 40,
#                 "status": "PENDING",
#                 "price": 10,
#                 "type": "LIMIT",
#                 "side": "BUY"
#             }
#         )
#
#         self.assert_is_limit_order(order)
#
#     def test_from_dict_pending_limit_order_buy(self):
#         order = Order.from_dict(
#             {
#                 "reference_id": 10493,
#                 "target_symbol": "DOT",
#                 "trading_symbol": "USDT",
#                 "amount": 40,
#                 "status": "PENDING",
#                 "price": 10,
#                 "type": "LIMIT",
#                 "side": "BUY"
#             }
#         )
#
#         self.assertIsNotNone(order.get_reference_id())
#         self.assertIsNotNone(order.get_target_symbol())
#         self.assertIsNotNone(order.get_trading_symbol())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_status())
#         self.assertIsNotNone(order.get_side())
#         self.assertIsNotNone(order.get_type())
#         self.assertIsNotNone(order.get_price())
#
#     def test_from_dict_successful_limit_order_buy(self):
#         order = Order.from_dict(
#             {
#                 "reference_id": 10493,
#                 "target_symbol": "DOT",
#                 "trading_symbol": "USDT",
#                 "amount": 40,
#                 "status": "CLOSED",
#                 "price": 10,
#                 "initial_price": 10,
#                 "type": "LIMIT",
#                 "side": "BUY"
#             }
#         )
#
#         self.assertIsNotNone(order.get_reference_id())
#         self.assertIsNotNone(order.get_target_symbol())
#         self.assertIsNotNone(order.get_trading_symbol())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_status())
#         self.assertIsNotNone(order.get_side())
#         self.assertIsNotNone(order.get_type())
#         self.assertIsNotNone(order.get_price())
#
#         with self.assertRaises(OperationalException):
#             Order.from_dict(
#                 {
#                     "reference_id": 10493,
#                     "target_symbol": "DOT",
#                     "trading_symbol": "USDT",
#                     "amount": 40,
#                     "status": "CLOSED",
#                     "price": 10,
#                     "type": "LIMIT",
#                     "side": "BUY"
#                 }
#             )
#
#     def test_from_dict_closed_limit_order_buy(self):
#         order = Order.from_dict(
#             {
#                 "reference_id": 10493,
#                 "target_symbol": "DOT",
#                 "trading_symbol": "USDT",
#                 "amount": 40,
#                 "status": "CLOSED",
#                 "initial_price": 10,
#                 "closing_price": 11,
#                 "type": "LIMIT",
#                 "side": "BUY"
#             }
#         )
#
#         self.assertIsNotNone(order.get_reference_id())
#         self.assertIsNotNone(order.get_target_symbol())
#         self.assertIsNotNone(order.get_trading_symbol())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_status())
#         self.assertIsNotNone(order.get_side())
#         self.assertIsNotNone(order.get_type())
#         self.assertIsNotNone(order.get_closing_price())
#         self.assertIsNotNone(order.get_initial_price())
#
#         with self.assertRaises(OperationalException):
#             Order.from_dict(
#                 {
#                     "reference_id": 10493,
#                     "target_symbol": "DOT",
#                     "trading_symbol": "USDT",
#                     "amount": 40,
#                     "status": "CLOSED",
#                     "price": 10,
#                     "type": "LIMIT",
#                     "side": "BUY"
#                 }
#             )
#
#     def test_from_dict_pending_limit_order_sell(self):
#         order = Order.from_dict(
#             {
#                 "reference_id": 10493,
#                 "target_symbol": "DOT",
#                 "trading_symbol": "USDT",
#                 "amount": 40,
#                 "status": "PENDING",
#                 "price": 10,
#                 "type": "LIMIT",
#                 "side": "SELL"
#             }
#         )
#
#         self.assertIsNotNone(order.get_reference_id())
#         self.assertIsNotNone(order.get_target_symbol())
#         self.assertIsNotNone(order.get_trading_symbol())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_status())
#         self.assertIsNotNone(order.get_side())
#         self.assertIsNotNone(order.get_type())
#         self.assertIsNotNone(order.get_price())
#
#     def test_from_dict_success_limit_order_sell(self):
#         order = Order.from_dict(
#             {
#                 "reference_id": 10493,
#                 "target_symbol": "DOT",
#                 "trading_symbol": "USDT",
#                 "amount": 40,
#                 "status": "CLOSED",
#                 "price": 10,
#                 "initial_price": 9,
#                 "type": "LIMIT",
#                 "side": "SELL"
#             }
#         )
#
#         self.assertIsNotNone(order.get_reference_id())
#         self.assertIsNotNone(order.get_target_symbol())
#         self.assertIsNotNone(order.get_trading_symbol())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_status())
#         self.assertIsNotNone(order.get_side())
#         self.assertIsNotNone(order.get_type())
#         self.assertIsNotNone(order.get_price())
#
#     def test_from_dict_closed_limit_order_sell(self):
#         order = Order.from_dict(
#             {
#                 "reference_id": 10493,
#                 "target_symbol": "DOT",
#                 "trading_symbol": "USDT",
#                 "amount": 40,
#                 "status": "CLOSED",
#                 "closing_price": 10,
#                 "initial_price": 9,
#                 "type": "LIMIT",
#                 "side": "SELL"
#             }
#         )
#
#         self.assertIsNotNone(order.get_reference_id())
#         self.assertIsNotNone(order.get_target_symbol())
#         self.assertIsNotNone(order.get_trading_symbol())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_status())
#         self.assertIsNotNone(order.get_side())
#         self.assertIsNotNone(order.get_type())
#         self.assertIsNotNone(order.get_price())
#
#     def test_from_dict_pending_market_order_sell(self):
#         order = Order.from_dict(
#             {
#                 "reference_id": 10493,
#                 "target_symbol": "DOT",
#                 "trading_symbol": "USDT",
#                 "amount": 40,
#                 "status": "PENDING",
#                 "price": 10,
#                 "type": "MARKET",
#                 "side": "SELL"
#             }
#         )
#
#         self.assertIsNotNone(order.get_reference_id())
#         self.assertIsNotNone(order.get_target_symbol())
#         self.assertIsNotNone(order.get_trading_symbol())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNone(order.get_amount())
#         self.assertIsNotNone(order.get_status())
#         self.assertIsNotNone(order.get_side())
#         self.assertIsNotNone(order.get_type())
#         self.assertIsNotNone(order.get_price())
#
#     def test_from_dict_success_market_order_sell(self):
#         order = Order.from_dict(
#             {
#                 "reference_id": 10493,
#                 "target_symbol": "DOT",
#                 "trading_symbol": "USDT",
#                 "amount": 40,
#                 "status": "CLOSED",
#                 "price": 10,
#                 "initial_price": 9,
#                 "type": "LIMIT",
#                 "side": "SELL"
#             }
#         )
#
#         self.assertIsNotNone(order.get_reference_id())
#         self.assertIsNotNone(order.get_target_symbol())
#         self.assertIsNotNone(order.get_trading_symbol())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_status())
#         self.assertIsNotNone(order.get_side())
#         self.assertIsNotNone(order.get_type())
#         self.assertIsNotNone(order.get_price())
#
#     def test_from_dict_closed_market_order_sell(self):
#         order = Order.from_dict(
#             {
#                 "reference_id": 10493,
#                 "target_symbol": "DOT",
#                 "trading_symbol": "USDT",
#                 "amount": 40,
#                 "status": "CLOSED",
#                 "closing_price": 10,
#                 "initial_price": 9,
#                 "type": "MARKET",
#                 "side": "SELL"
#             }
#         )
#
#         self.assertIsNotNone(order.get_reference_id())
#         self.assertIsNotNone(order.get_target_symbol())
#         self.assertIsNotNone(order.get_trading_symbol())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_amount())
#         self.assertIsNotNone(order.get_status())
#         self.assertIsNotNone(order.get_side())
#         self.assertIsNotNone(order.get_type())
#         self.assertIsNotNone(order.get_price())
