from binance.order_utils import get_open_orders_binance, get_open_orders_binance_post_details, \
    get_open_orders_binance_result_processor
from bittrex.order_utils import get_open_orders_bittrix, get_open_orders_bittrex_result_processor, \
    get_open_orders_bittrix_post_details
from kraken.order_utils import get_open_orders_kraken, get_open_orders_kraken_post_details, \
    get_open_orders_kraken_result_processor
from poloniex.order_utils import get_open_orders_poloniex, get_open_orders_poloniex_post_details, \
    get_open_orders_poloniex_result_processor
from huobi.order_utils import get_open_orders_huobi, get_open_orders_huobi_post_details, \
    get_orders_huobi_result_processor

from constants import HTTP_TIMEOUT_SECONDS

from data_access.classes.work_unit import WorkUnit

from utils.debug_utils import print_to_console, LOG_ALL_ERRORS

from enums.exchange import EXCHANGE
from enums.status import STATUS
from enums.http_request import HTTP_REQUEST

from utils.currency_utils import get_currency_pair_name_by_exchange_id
from utils.key_utils import get_key_by_exchange


def get_open_orders_by_exchange(exchange_id, pair_id):
    res = STATUS.FAILURE, None

    key = get_key_by_exchange(exchange_id)

    pair_name = get_currency_pair_name_by_exchange_id(pair_id, exchange_id)

    method_by_exchange = {
        EXCHANGE.BITTREX: get_open_orders_bittrix,
        EXCHANGE.KRAKEN: get_open_orders_kraken,
        EXCHANGE.POLONIEX: get_open_orders_poloniex,
        EXCHANGE.BINANCE: get_open_orders_binance,
        EXCHANGE.HUOBI: get_open_orders_huobi
    }

    if exchange_id in method_by_exchange:
        get_open_orders = method_by_exchange[exchange_id]
        res = get_open_orders(key, pair_name)
    else:
        msg = "get_open_orders_by_exchange - Unknown exchange! {idx}".format(idx=exchange_id)
        print_to_console(msg, LOG_ALL_ERRORS)

    return res


def get_open_orders_post_details_generator(exchange_id):
    return {
        EXCHANGE.BITTREX: get_open_orders_bittrix_post_details,
        EXCHANGE.KRAKEN: get_open_orders_kraken_post_details,
        EXCHANGE.POLONIEX: get_open_orders_poloniex_post_details,
        EXCHANGE.BINANCE: get_open_orders_binance_post_details,
        EXCHANGE.HUOBI: get_open_orders_huobi_post_details
    }[exchange_id]


def get_open_orders_constructor_by_exchange_id(exchange_id):
    return {
        EXCHANGE.BITTREX: get_open_orders_bittrex_result_processor,
        EXCHANGE.KRAKEN: get_open_orders_kraken_result_processor,
        EXCHANGE.POLONIEX: get_open_orders_poloniex_result_processor,
        EXCHANGE.BINANCE: get_open_orders_binance_result_processor,
        EXCHANGE.HUOBI: get_orders_huobi_result_processor
    }[exchange_id]


def get_http_method_open_order_by_exchange_id(exchange_id):
    return {
        EXCHANGE.BINANCE: HTTP_REQUEST.GET,
        EXCHANGE.BITTREX: HTTP_REQUEST.POST,
        EXCHANGE.POLONIEX: HTTP_REQUEST.POST,
        EXCHANGE.KRAKEN: HTTP_REQUEST.POST,
        EXCHANGE.HUOBI: HTTP_REQUEST.GET
    }[exchange_id]


def get_open_orders_for_arbitrage_pair(cfg, processor):

    open_orders = []

    for exchange_id in [cfg.sell_exchange_id, cfg.buy_exchange_id]:
        key = get_key_by_exchange(exchange_id)
        pair_name = get_currency_pair_name_by_exchange_id(cfg.pair_id, exchange_id)

        method_for_url = get_open_orders_post_details_generator(exchange_id)
        post_details = method_for_url(key, pair_name)
        constructor = get_open_orders_constructor_by_exchange_id(exchange_id)
        http_method = get_http_method_open_order_by_exchange_id(exchange_id)

        wu = WorkUnit(post_details.final_url, constructor, pair_name)
        wu.add_post_details(post_details)
        wu.add_http_method(http_method)

        open_orders.append(wu)

    return processor.process_async_custom(open_orders, HTTP_TIMEOUT_SECONDS)
