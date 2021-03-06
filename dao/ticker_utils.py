from binance.constants import BINANCE_CURRENCY_PAIRS
from binance.ticker_utils import get_tickers_binance, get_tickers_binance_url, get_ticker_binance, \
    get_ticker_binance_result_processor
from bittrex.constants import BITTREX_CURRENCY_PAIRS
from bittrex.ticker_utils import get_ticker_bittrex, get_ticker_bittrex_url, get_ticker_bittrex_result_processor
from data_access.classes.work_unit import WorkUnit
from utils.debug_utils import print_to_console, LOG_ALL_ERRORS

from enums.currency_pair import CURRENCY_PAIR
from enums.exchange import EXCHANGE

from kraken.constants import KRAKEN_CURRENCY_PAIRS
from kraken.ticker_utils import get_ticker_kraken, get_ticker_kraken_url, get_ticker_kraken_result_processor

from poloniex.constants import POLONIEX_CURRENCY_PAIRS
from poloniex.ticker_utils import get_tickers_poloniex, get_ticker_poloniex_url, get_ticker_poloniex, \
    get_ticker_poloniex_result_processor

from huobi.constants import HUOBI_CURRENCY_PAIRS
from huobi.ticker_utils import get_ticker_huobi, get_ticker_huobi_url, get_ticker_huobi_result_processor

from utils.currency_utils import get_currency_pair_name_by_exchange_id
from utils.time_utils import get_now_seconds_utc
from constants import HTTP_TIMEOUT_SECONDS


def get_ticker_constructor_by_exchange_id(exchange_id):
    """
        Return functor that expect following arguments:
            json_document - response of exchange,
            exchange specific name of currency
            timest - current time
        It will return array of object from data/* folder
    """
    return {
        EXCHANGE.BITTREX: get_ticker_bittrex_result_processor,
        EXCHANGE.KRAKEN: get_ticker_kraken_result_processor,
        EXCHANGE.POLONIEX: get_ticker_poloniex_result_processor,
        EXCHANGE.BINANCE: get_ticker_binance_result_processor,
        EXCHANGE.HUOBI: get_ticker_huobi_result_processor
    }[exchange_id]


def get_ticker_speedup(timest, processor):

    ohlc_async_requests = []

    for exchange_id in [EXCHANGE.BITTREX, EXCHANGE.KRAKEN, EXCHANGE.HUOBI]:
        for pair_id in CURRENCY_PAIR.values():

            pair_name = get_currency_pair_name_by_exchange_id(pair_id, exchange_id)
            if pair_name is None:
                continue

            method_for_url = get_ticker_url_by_exchange_id(exchange_id)
            request_url = method_for_url(pair_name)
            constructor = get_ticker_constructor_by_exchange_id(exchange_id)

            ohlc_async_requests.append(WorkUnit(request_url, constructor, pair_name, timest))

    async_results = processor.process_async_get(ohlc_async_requests, timeout=HTTP_TIMEOUT_SECONDS)

    async_results += get_tickers_poloniex(POLONIEX_CURRENCY_PAIRS, timest)
    async_results += get_tickers_binance(BINANCE_CURRENCY_PAIRS, timest)

    return async_results


def get_tickers():
    all_tickers = {}

    timest = get_now_seconds_utc()

    bittrex_tickers = {}
    for pair_name in BITTREX_CURRENCY_PAIRS:
        ticker = get_ticker_bittrex(pair_name, timest)
        if ticker is not None:
            bittrex_tickers[ticker.pair_id] = ticker
    all_tickers[EXCHANGE.BITTREX] = bittrex_tickers

    kraken_tickers = {}
    for pair_name in KRAKEN_CURRENCY_PAIRS:
        ticker = get_ticker_kraken(pair_name, timest)
        if ticker is not None:
            kraken_tickers[ticker.pair_id] = ticker
    all_tickers[EXCHANGE.KRAKEN] = kraken_tickers

    huobi_tickers = {}
    for pair_name in HUOBI_CURRENCY_PAIRS:
        ticker = get_ticker_huobi(pair_name, timest)
        if ticker is not None:
            huobi_tickers[ticker.pair_id] = ticker
    all_tickers[EXCHANGE.HUOBI] = huobi_tickers

    # NOTE: poloniex return all tickers by single call
    poloniex_tickers = get_tickers_poloniex(POLONIEX_CURRENCY_PAIRS, timest)
    all_tickers[EXCHANGE.POLONIEX] = poloniex_tickers

    # NOTE: binance return all tickers by single call
    binance_tickers = get_tickers_binance(BINANCE_CURRENCY_PAIRS, timest)
    all_tickers[EXCHANGE.BINANCE] = binance_tickers

    return all_tickers


def get_ticker_for_arbitrage(pair_id, timest, exchange_list, processor):

    async_requests = []

    for exchange_id in exchange_list:
        pair_name = get_currency_pair_name_by_exchange_id(pair_id, exchange_id)
        if pair_name is None:

            msg = "get_ticker for arbitrage - wrong pair_id - {pair_id} for exchange_id = {idd}!".format(pair_id=pair_id, idd=exchange_id)
            print_to_console(msg, LOG_ALL_ERRORS)

            assert pair_name is None

        method_for_url = get_ticker_url_by_exchange_id(exchange_id)
        request_url = method_for_url(pair_name)
        constructor = get_ticker_constructor_by_exchange_id(exchange_id)

        async_requests.append(WorkUnit(request_url, constructor, pair_name, timest))

    res = processor.process_async_get(async_requests, timeout=5)

    return res


def get_ticker_method_by_exchange_id(exchange_id):
    return {
        EXCHANGE.KRAKEN: get_ticker_kraken,
        EXCHANGE.BITTREX: get_ticker_bittrex,
        EXCHANGE.POLONIEX: get_ticker_poloniex,
        EXCHANGE.BINANCE: get_ticker_binance,
        EXCHANGE.HUOBI: get_ticker_huobi
    }[exchange_id]


def get_ticker_url_by_exchange_id(exchange_id):
    return {
        EXCHANGE.BITTREX: get_ticker_bittrex_url,
        EXCHANGE.KRAKEN: get_ticker_kraken_url,
        EXCHANGE.POLONIEX: get_ticker_poloniex_url,
        EXCHANGE.BINANCE: get_tickers_binance_url,
        EXCHANGE.HUOBI: get_ticker_huobi_url
    }[exchange_id]


def get_ticker(exchange_id, pair_id):
    method = get_ticker_method_by_exchange_id(exchange_id)

    pair_name = get_currency_pair_name_by_exchange_id(pair_id, exchange_id)

    if pair_name is None:
        msg = "get_ticker for arbitrage - wrong pair_id - {pair_id} for exchange_id = {idd}!".format(pair_id=pair_id,
                                                                                                     idd=exchange_id)
        print_to_console(msg, LOG_ALL_ERRORS)

        assert pair_name is None

    return method(pair_name, get_now_seconds_utc())
