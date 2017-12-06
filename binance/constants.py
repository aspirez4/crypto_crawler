
BINANCE_GET_TICKER = "https://api.binance.com/api/v1/ticker/allBookTickers"  #  Yeah, it just return EVERYTHING

# OHLC ~ canddle stick urls
# https://api.binance.com/api/v1/klines?symbol=XMRETH&interval=15m&startTime=
# Periods: 1m,3m,5m,15m,30m,1h,2h,4h,6h,8h,12h,1d,3d,1w,1M
BINANCE_GET_OHLC = "https://api.binance.com/api/v1/klines?symbol="

#       FIXME NOTE - depth can vary
# https://api.binance.com/api/v1/depth?symbol=XMRETH
# optional parameter limit INT	NO Default 100; max 100.
BINANCE_GET_ORDER_BOOK = "https://api.binance.com/api/v1/depth?symbol="


BINANCE_GET_HISTORY = ""


BINANCE_CURRENCIES = ["DASHBTC", "ETHBTC", "LTCBTC", "XRPBTC", "BCCBTC", "ETCBTC", "OMGBTC", "ZECBTC",  "XMRBTC",
                      "DASHETH", "XRPETH", "BCCETH", "ETCETH", "OMGETH", "ZECETH", "XMRETH",
                      "BTCUSDT", "ETHUSDT", "BCCUSDT"
                      ]

# LIMIT
# BUY | SELL

# POST symbol side type timeInForce quantity price
BINANCE_BUY_ORDER = "https://api.binance.com/api/v3/order?"

# POST symbol side type timeInForce quantity price
BINANCE_SELL_ORDER = "https://api.binance.com/api/v3/order?"

# DELETE symbol orderId
BINANCE_CANCEL_ORDER = "https://api.binance.com/api/v3/order?"

# timestamp
BINANCE_CHECK_BALANCE = "https://api.binance.com/api/v3/account?"

BINANCE_GET_ALL_ORDERS = "https://api.binance.com/api/v3/allOrders?"