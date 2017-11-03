class EXCHANGE:
    POLONIEX = 1
    POLONIEX_EXCHANGE = "POLONIEX"

    KRAKEN = 2
    KRAKEN_EXCHANGE = "KRAKEN"

    BITTREX = 3
    BITTREX_EXCHANGE = "BITTREX"

    @classmethod
    def values(cls):
        return [EXCHANGE.POLONIEX,
                EXCHANGE.KRAKEN,
                EXCHANGE.BITTREX
                ]

    @classmethod
    def exchange_names(cls):
        return [EXCHANGE.POLONIEX_EXCHANGE, EXCHANGE.KRAKEN_EXCHANGE, EXCHANGE.BITTREX_EXCHANGE]

# In percents
EXCHANGE_FEE = {EXCHANGE.POLONIEX: 0.25, EXCHANGE.KRAKEN: 0.26, EXCHANGE.BITTREX: 0.25}