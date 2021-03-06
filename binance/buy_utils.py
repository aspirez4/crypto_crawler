from binance.constants import BINANCE_BUY_ORDER, BINANCE_NUM_OF_DEAL_RETRY, BINANCE_DEAL_TIMEOUT
from binance.rest_api import generate_post_request

from data_access.internet import send_post_request_with_header

from utils.debug_utils import get_logging_level, print_to_console, LOG_ALL_MARKET_RELATED_CRAP

from utils.file_utils import log_to_file
from utils.time_utils import get_now_seconds_utc_ms
from utils.string_utils import float_to_str

"""
time in force:
IOC: An immediate or cancel order
GTC: Good-Til-Canceled
"""


def add_buy_order_binance_url(key, pair_name, price, amount):
    #  curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
    # -X POST 'https://api.binance.com/api/v3/order' -d 'symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1
    # &price=0.1&recvWindow=6000000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71'

    body = {
        "symbol": pair_name,
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "recvWindow": 5000,
        "timestamp": get_now_seconds_utc_ms(),
        "quantity": amount,
        "price": float_to_str(price)
    }

    res = generate_post_request(BINANCE_BUY_ORDER, body, key)

    if get_logging_level() >= LOG_ALL_MARKET_RELATED_CRAP:
        msg = "add_buy_order_binance: {res}".format(res=res)
        print_to_console(msg, LOG_ALL_MARKET_RELATED_CRAP)
        log_to_file(msg, "market_utils.log")

    return res


def add_buy_order_binance(key, pair_name, price, amount):

    post_details = add_buy_order_binance_url(key, pair_name, price, amount)

    err_msg = "add_buy_order_binance  called for {pair} for amount = {amount} with price {price}".format(pair=pair_name, amount=amount, price=price)

    res = send_post_request_with_header(post_details, err_msg,
                                        max_tries=BINANCE_NUM_OF_DEAL_RETRY, timeout=BINANCE_DEAL_TIMEOUT)

    """
    {
        "orderId": 1373289, 
        "clientOrderId": "Is7wGaKBtLBK7JjDkNAJwn",
        "origQty": "10.00000000",
        "symbol": "RDNBTC",
        "side": "BUY",
        "timeInForce": "GTC",
        "status": "NEW",
        "transactTime": 1512581468544,
        "type": "LIMIT",
        "price": "0.00022220",
        "executedQty": "0.00000000"
    }
    """

    if get_logging_level() >= LOG_ALL_MARKET_RELATED_CRAP:
        print_to_console(res, LOG_ALL_MARKET_RELATED_CRAP)
        log_to_file(res, "market_utils.log")

    return res
