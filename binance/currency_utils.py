from enums.currency import CURRENCY
from enums.currency_pair import CURRENCY_PAIR


def get_currency_id_from_binance(currency_name):
    return {
        'BTC': CURRENCY.BITCOIN,
        'DASH': CURRENCY.DASH,
        'BCC': CURRENCY.BCC,
        'XRP': CURRENCY.XRP,
        'LTC': CURRENCY.LTC,
        'ETC': CURRENCY.ETC,
        'ETH': CURRENCY.ETH,
        'SC': CURRENCY.SC,
        'DGB': CURRENCY.DGB,
        'XEM': CURRENCY.XEM,
        'ARDR': CURRENCY.ARDR,
        'OMG': CURRENCY.OMG,
        'ZEC': CURRENCY.ZEC,
        'REP': CURRENCY.REP,
        'XMR': CURRENCY.XMR,
        'DOGE': CURRENCY.DOGE,
        'DCR': CURRENCY.DCR,
        'NEO': CURRENCY.NEO,
        'QTUM': CURRENCY.QTUM,
        'EOS': CURRENCY.EOS,
        'IOTA': CURRENCY.IOTA,
        'BTG': CURRENCY.BTG,
        'WTC': CURRENCY.WTC,
        'KNC': CURRENCY.KNC,
        'BAT': CURRENCY.BAT,
        'ZRX': CURRENCY.ZRX,
        'RDN': CURRENCY.RDN,
        'GAS': CURRENCY.GAS,
        'ADA': CURRENCY.ADA,
        'QSP': CURRENCY.QSP,
        'RCN': CURRENCY.RCN,
        'ICX': CURRENCY.ICX,
        'WABI': CURRENCY.WABI,
        'XLM': CURRENCY.XLM,
        'TRX': CURRENCY.TRX,
        'AION': CURRENCY.AION,
        'ARK': CURRENCY.ARK,
        'STRAT': CURRENCY.STRAT,
        'USDT': CURRENCY.USDT
    }.get(currency_name)


def get_currency_name_for_binance(currency_id):
    return {
        CURRENCY.BITCOIN: 'BTC',
        CURRENCY.DASH: 'DASH',
        CURRENCY.BCC: 'BCC',
        CURRENCY.XRP: 'XRP',
        CURRENCY.LTC: 'LTC',
        CURRENCY.ETC: 'ETC',
        CURRENCY.ETH: 'ETH',
        CURRENCY.SC: 'SC',
        CURRENCY.DGB: 'DGB',
        CURRENCY.XEM: 'XEM',
        CURRENCY.ARDR: 'ARDR',
        CURRENCY.OMG: 'OMG',
        CURRENCY.ZEC: 'ZEC',
        CURRENCY.REP: 'REP',
        CURRENCY.XMR: 'XMR',
        CURRENCY.DOGE: 'DOGE',
        CURRENCY.DCR: 'DCR',
        CURRENCY.NEO: 'NEO',
        CURRENCY.QTUM: 'QTUM',
        CURRENCY.EOS: 'EOS',
        CURRENCY.IOTA: 'IOTA',
        CURRENCY.BTG: 'BTG',
        CURRENCY.WTC: 'WTC',
        CURRENCY.KNC: 'KNC',
        CURRENCY.BAT: 'BAT',
        CURRENCY.ZRX: 'ZRX',
        CURRENCY.RDN: 'RDN',
        CURRENCY.GAS: 'GAS',
        CURRENCY.ADA: 'ADA',
        CURRENCY.QSP: 'QSP',
        CURRENCY.RCN: 'RCN',
        CURRENCY.ICX: 'ICX',
        CURRENCY.WABI: 'WABI',
        CURRENCY.XLM: 'XLM',
        CURRENCY.TRX: 'TRX',
        CURRENCY.AION: 'AION',
        CURRENCY.ARK: 'ARK',
        CURRENCY.STRAT: 'STRAT',
        CURRENCY.USDT: 'USDT'
    }.get(currency_id)


def get_currency_pair_from_binance(pair_id):
    return {
        'DASHBTC': CURRENCY_PAIR.BTC_TO_DASH,
        'ETHBTC': CURRENCY_PAIR.BTC_TO_ETH,
        'LTCBTC': CURRENCY_PAIR.BTC_TO_LTC,
        'XRPBTC': CURRENCY_PAIR.BTC_TO_XRP,
        'BCCBTC': CURRENCY_PAIR.BTC_TO_BCC,
        'ETCBTC': CURRENCY_PAIR.BTC_TO_ETC,
        'OMGBTC': CURRENCY_PAIR.BTC_TO_OMG,
        'ZECBTC': CURRENCY_PAIR.BTC_TO_ZEC,
        'XMRBTC': CURRENCY_PAIR.BTC_TO_XMR,
        'NEOBTC': CURRENCY_PAIR.BTC_TO_NEO,
        'QTUMBTC': CURRENCY_PAIR.BTC_TO_QTUM,
        'EOSBTC': CURRENCY_PAIR.BTC_TO_EOS,
        'IOTABTC': CURRENCY_PAIR.BTC_TO_IOTA,
        'BTGBTC': CURRENCY_PAIR.BTC_TO_BTG,
        'WTCBTC': CURRENCY_PAIR.BTC_TO_WTC,
        'KNCBTC': CURRENCY_PAIR.BTC_TO_KNC,
        'BATBTC': CURRENCY_PAIR.BTC_TO_BAT,
        'ZRXBTC': CURRENCY_PAIR.BTC_TO_ZRX,
        'RDNBTC': CURRENCY_PAIR.BTC_TO_RDN,
        'GASBTC': CURRENCY_PAIR.BTC_TO_GAS,
        'ADABTC': CURRENCY_PAIR.BTC_TO_ADA,
        'QSPBTC': CURRENCY_PAIR.BTC_TO_QSP,
        'RCNBTC': CURRENCY_PAIR.BTC_TO_RCN,
        'ICXBTC': CURRENCY_PAIR.BTC_TO_ICX,
        'WABIBTC': CURRENCY_PAIR.BTC_TO_WABI,
        'XLMBTC': CURRENCY_PAIR.BTC_TO_XLM,
        'TRXBTC': CURRENCY_PAIR.BTC_TO_TRX,
        'AIONBTC': CURRENCY_PAIR.BTC_TO_AION,
        'ARKBTC': CURRENCY_PAIR.BTC_TO_ARK,
        'STRATBTC': CURRENCY_PAIR.BTC_TO_STRAT,
        'DASHETH': CURRENCY_PAIR.ETH_TO_DASH,
        'XRPETH': CURRENCY_PAIR.ETH_TO_XRP,
        'BCCETH': CURRENCY_PAIR.ETH_TO_BCC,
        'ETCETH': CURRENCY_PAIR.ETH_TO_ETC,
        'OMGETH': CURRENCY_PAIR.ETH_TO_OMG,
        'ZECETH': CURRENCY_PAIR.ETH_TO_ZEC,
        'XMRETH': CURRENCY_PAIR.ETH_TO_XMR,
        'NEOETH': CURRENCY_PAIR.ETH_TO_NEO,
        'QTUMETH': CURRENCY_PAIR.ETH_TO_QTUM,
        'EOSETH': CURRENCY_PAIR.ETH_TO_EOS,
        'IOTAETH': CURRENCY_PAIR.ETH_TO_IOTA,
        'BTGETH': CURRENCY_PAIR.ETH_TO_BTG,
        'WTCETH': CURRENCY_PAIR.ETH_TO_WTC,
        'KNCETH': CURRENCY_PAIR.ETH_TO_KNC,
        'BATETH': CURRENCY_PAIR.ETH_TO_BAT,
        'ZRXETH': CURRENCY_PAIR.ETH_TO_ZRX,
        'RDNETH': CURRENCY_PAIR.ETH_TO_RDN,
        'ADAETH': CURRENCY_PAIR.ETH_TO_ADA,
        'QSPETH': CURRENCY_PAIR.ETH_TO_QSP,
        'RCNETH': CURRENCY_PAIR.ETH_TO_RCN,
        'ICXETH': CURRENCY_PAIR.ETH_TO_ICX,
        'WABIETH': CURRENCY_PAIR.ETH_TO_WABI,
        'XLMETH': CURRENCY_PAIR.ETH_TO_XLM,
        'TRXETH': CURRENCY_PAIR.ETH_TO_TRX,
        'AIONETH': CURRENCY_PAIR.ETH_TO_AION,
        'ARKETH': CURRENCY_PAIR.ETH_TO_ARK,
        'STRATETH': CURRENCY_PAIR.ETH_TO_STRAT,
        'BTCUSDT': CURRENCY_PAIR.USDT_TO_BTC,
        'BCCUSDT': CURRENCY_PAIR.USDT_TO_BCC,
        'ETHUSDT': CURRENCY_PAIR.USDT_TO_ETH,
        'NEOUSDT': CURRENCY_PAIR.USDT_TO_NEO,
    }.get(pair_id)


def get_currency_pair_to_binance(pair_id):
    return {
        CURRENCY_PAIR.BTC_TO_DASH: 'DASHBTC',
        CURRENCY_PAIR.BTC_TO_ETH: 'ETHBTC',
        CURRENCY_PAIR.BTC_TO_LTC: 'LTCBTC',
        CURRENCY_PAIR.BTC_TO_XRP: 'XRPBTC',
        CURRENCY_PAIR.BTC_TO_BCC: 'BCCBTC',
        CURRENCY_PAIR.BTC_TO_ETC: 'ETCBTC',
        CURRENCY_PAIR.BTC_TO_OMG: 'OMGBTC',
        CURRENCY_PAIR.BTC_TO_ZEC: 'ZECBTC',
        CURRENCY_PAIR.BTC_TO_XMR: 'XMRBTC',
        CURRENCY_PAIR.BTC_TO_NEO: 'NEOBTC',
        CURRENCY_PAIR.BTC_TO_QTUM: 'QTUMBTC',
        CURRENCY_PAIR.BTC_TO_EOS: 'EOSBTC',
        CURRENCY_PAIR.BTC_TO_IOTA: 'IOTABTC',
        CURRENCY_PAIR.BTC_TO_BTG: 'BTGBTC',
        CURRENCY_PAIR.BTC_TO_WTC: 'WTCBTC',
        CURRENCY_PAIR.BTC_TO_KNC: 'KNCBTC',
        CURRENCY_PAIR.BTC_TO_BAT: 'BATBTC',
        CURRENCY_PAIR.BTC_TO_ZRX: 'ZRXBTC',
        CURRENCY_PAIR.BTC_TO_RDN: 'RDNBTC',
        CURRENCY_PAIR.BTC_TO_GAS: 'GASBTC',
        CURRENCY_PAIR.BTC_TO_ADA: 'ADABTC',
        CURRENCY_PAIR.BTC_TO_QSP: 'QSPBTC',
        CURRENCY_PAIR.BTC_TO_RCN: 'RCNBTC',
        CURRENCY_PAIR.BTC_TO_ICX: 'ICXBTC',
        CURRENCY_PAIR.BTC_TO_WABI: 'WABIBTC',
        CURRENCY_PAIR.BTC_TO_XLM: 'XLMBTC',
        CURRENCY_PAIR.BTC_TO_TRX: 'TRXBTC',
        CURRENCY_PAIR.BTC_TO_AION: 'AIONBTC',
        CURRENCY_PAIR.BTC_TO_ARK: 'ARKBTC',
        CURRENCY_PAIR.BTC_TO_STRAT: 'STRATBTC',
        CURRENCY_PAIR.ETH_TO_DASH: 'DASHETH',
        CURRENCY_PAIR.ETH_TO_XRP: 'XRPETH',
        CURRENCY_PAIR.ETH_TO_BCC: 'BCCETH',
        CURRENCY_PAIR.ETH_TO_ETC: 'ETCETH',
        CURRENCY_PAIR.ETH_TO_OMG: 'OMGETH',
        CURRENCY_PAIR.ETH_TO_ZEC: 'ZECETH',
        CURRENCY_PAIR.ETH_TO_XMR: 'XMRETH',
        CURRENCY_PAIR.ETH_TO_NEO: 'NEOETH',
        CURRENCY_PAIR.ETH_TO_QTUM: 'QTUMETH',
        CURRENCY_PAIR.ETH_TO_EOS: 'EOSETH',
        CURRENCY_PAIR.ETH_TO_IOTA: 'IOTAETH',
        CURRENCY_PAIR.ETH_TO_BTG: 'BTGETH',
        CURRENCY_PAIR.ETH_TO_WTC: 'WTCETH',
        CURRENCY_PAIR.ETH_TO_KNC: 'KNCETH',
        CURRENCY_PAIR.ETH_TO_BAT: 'BATETH',
        CURRENCY_PAIR.ETH_TO_ZRX: 'ZRXETH',
        CURRENCY_PAIR.ETH_TO_RDN: 'RDNETH',
        CURRENCY_PAIR.ETH_TO_ADA: 'ADAETH',
        CURRENCY_PAIR.ETH_TO_QSP: 'QSPETH',
        CURRENCY_PAIR.ETH_TO_RCN: 'RCNETH',
        CURRENCY_PAIR.ETH_TO_ICX: 'ICXETH',
        CURRENCY_PAIR.ETH_TO_WABI: 'WABIETH',
        CURRENCY_PAIR.ETH_TO_XLM: 'XLMETH',
        CURRENCY_PAIR.ETH_TO_TRX: 'TRXETH',
        CURRENCY_PAIR.ETH_TO_AION: 'AIONETH',
        CURRENCY_PAIR.ETH_TO_ARK: 'ARKETH',
        CURRENCY_PAIR.ETH_TO_STRAT: 'STRATETH',
        CURRENCY_PAIR.USDT_TO_BTC: 'BTCUSDT',
        CURRENCY_PAIR.USDT_TO_BCC: 'BCCUSDT',
        CURRENCY_PAIR.USDT_TO_ETH: 'ETHUSDT',
        CURRENCY_PAIR.USDT_TO_NEO: 'NEOUSDT',
    }.get(pair_id)
