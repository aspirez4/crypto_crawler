from enums.currency_pair import CURRENCY_PAIR
from enums.currency import CURRENCY


def get_currency_name_for_huobi(currency_id):
    return {
        CURRENCY.BITCOIN: 'btc',
        CURRENCY.DASH: 'dash',
        CURRENCY.BCC: 'bch',
        CURRENCY.XRP: 'xrp',
        CURRENCY.LTC: 'ltc',
        CURRENCY.ETC: 'etc',
        CURRENCY.ETH: 'eth',
        CURRENCY.XEM: 'xem',
        CURRENCY.OMG: 'omg',
        CURRENCY.ZEC: 'zec',
        CURRENCY.NEO: 'neo',
        CURRENCY.QTUM: 'qtum',
        CURRENCY.EOS: 'eos',
        CURRENCY.BTG: 'btg',
        CURRENCY.KNC: 'knc',
        CURRENCY.BAT: 'bat',
        CURRENCY.ZRX: 'zrx',
        CURRENCY.RDN: 'rdn',
        CURRENCY.GAS: 'gas',
        CURRENCY.RCN: 'rcn',
        CURRENCY.ICX: 'icx',
        CURRENCY.TRX: 'trx',
        CURRENCY.LSK: 'lsk',
        CURRENCY.ENG: 'eng',
        CURRENCY.QSP: 'qsp',
        CURRENCY.ONT: 'ont',
        CURRENCY.HSR: 'hsr',
        CURRENCY.ZIL: 'zil',
        CURRENCY.VEN: 'ven',
        CURRENCY.ELF: 'elf',
        CURRENCY.BLZ: 'blz',
        CURRENCY.REQ: 'req',
        CURRENCY.LINK: 'link',
        CURRENCY.ELA: 'ela',
        CURRENCY.NAS: 'nas',
        CURRENCY.USDT: 'usdt'
    }.get(currency_id)


def get_currency_id_from_huobi(currency_name):
    return {
        'btc': CURRENCY.BITCOIN,
        'dash': CURRENCY.DASH,
        'bch': CURRENCY.BCC,
        'xrp': CURRENCY.XRP,
        'ltc': CURRENCY.LTC,
        'etc': CURRENCY.ETC,
        'eth': CURRENCY.ETH,
        'xem': CURRENCY.XEM,
        'omg': CURRENCY.OMG,
        'zec': CURRENCY.ZEC,
        'neo': CURRENCY.NEO,
        'qtum': CURRENCY.QTUM,
        'eos': CURRENCY.EOS,
        'btg': CURRENCY.BTG,
        'knc': CURRENCY.KNC,
        'bat': CURRENCY.BAT,
        'zrx': CURRENCY.ZRX,
        'rdn': CURRENCY.RDN,
        'gas': CURRENCY.GAS,
        'rcn': CURRENCY.RCN,
        'icx': CURRENCY.ICX,
        'trx': CURRENCY.TRX,
        'lsk': CURRENCY.LSK,
        'eng': CURRENCY.ENG,
        'qsp': CURRENCY.QSP,
        'ont': CURRENCY.ONT,
        'hsr': CURRENCY.HSR,
        'zil': CURRENCY.ZIL,
        'ven': CURRENCY.VEN,
        'elf': CURRENCY.ELF,
        'blz': CURRENCY.BLZ,
        'req': CURRENCY.REQ,
        'link': CURRENCY.LINK,
        'ela': CURRENCY.ELA,
        'nas': CURRENCY.NAS,
        'usdt': CURRENCY.USDT
    }.get(currency_name)


def get_currency_pair_to_huobi(pair_id):
    return {
        CURRENCY_PAIR.BTC_TO_DASH: 'dashbtc',
        CURRENCY_PAIR.BTC_TO_ETH: 'ethbtc',
        CURRENCY_PAIR.BTC_TO_LTC: 'ltcbtc',
        CURRENCY_PAIR.BTC_TO_XRP: 'xrpbtc',
        CURRENCY_PAIR.BTC_TO_BCC: 'bchbtc',
        CURRENCY_PAIR.BTC_TO_ETC: 'etcbtc',
        CURRENCY_PAIR.BTC_TO_XEM: 'xembtc',
        CURRENCY_PAIR.BTC_TO_OMG: 'omgbtc',
        CURRENCY_PAIR.BTC_TO_ZEC: 'zecbtc',
        CURRENCY_PAIR.BTC_TO_NEO: 'neobtc',
        CURRENCY_PAIR.BTC_TO_QTUM: 'qtumbtc',
        CURRENCY_PAIR.BTC_TO_BTG: 'btgbtc',
        CURRENCY_PAIR.BTC_TO_BAT: 'batbtc',
        CURRENCY_PAIR.BTC_TO_RCN: 'rcnbtc',
        CURRENCY_PAIR.BTC_TO_ZRX: 'zrxbtc',
        CURRENCY_PAIR.BTC_TO_LSK: 'lskbtc',
        CURRENCY_PAIR.BTC_TO_ENG: 'engbtc',
        CURRENCY_PAIR.BTC_TO_TRX: 'trxbtc',
        CURRENCY_PAIR.BTC_TO_EOS: 'eosbtc',
        CURRENCY_PAIR.BTC_TO_ICX: 'icxbtc',
        CURRENCY_PAIR.BTC_TO_RDN: 'rdnbtc',
        CURRENCY_PAIR.BTC_TO_QSP: 'qspbtc',

        CURRENCY_PAIR.BTC_TO_ONT: 'ontbtc',
        CURRENCY_PAIR.BTC_TO_HSR: 'hsrbtc',
        CURRENCY_PAIR.BTC_TO_ZIL: 'zilbtc',
        CURRENCY_PAIR.BTC_TO_VEN: 'venbtc',
        CURRENCY_PAIR.BTC_TO_ELF: 'elfbtc',
        CURRENCY_PAIR.BTC_TO_BLZ: 'blzbtc',
        CURRENCY_PAIR.BTC_TO_REQ: 'reqbtc',
        CURRENCY_PAIR.BTC_TO_LINK: 'linkbtc',
        CURRENCY_PAIR.BTC_TO_NAS: 'nasbtc',
        CURRENCY_PAIR.BTC_TO_ELA: 'elabtc',

        CURRENCY_PAIR.ETH_TO_OMG: 'omgeth',
        CURRENCY_PAIR.ETH_TO_QTUM: 'qtumeth',
        CURRENCY_PAIR.ETH_TO_BAT: 'bateth',
        CURRENCY_PAIR.ETH_TO_RCN: 'rcneth',
        CURRENCY_PAIR.ETH_TO_ENG: 'engeth',
        CURRENCY_PAIR.ETH_TO_TRX: 'trxeth',
        CURRENCY_PAIR.ETH_TO_EOS: 'eoseth',
        CURRENCY_PAIR.ETH_TO_ICX: 'icxeth',
        CURRENCY_PAIR.ETH_TO_RDN:'rdneth',
        CURRENCY_PAIR.ETH_TO_QSP: 'qspeth',

        CURRENCY_PAIR.ETH_TO_ONT: 'onteth',
        CURRENCY_PAIR.ETH_TO_HSR: 'hsreth',
        CURRENCY_PAIR.ETH_TO_ZIL: 'zileth',
        CURRENCY_PAIR.ETH_TO_VEN: 'veneth',
        CURRENCY_PAIR.ETH_TO_ELF: 'elfeth',
        CURRENCY_PAIR.ETH_TO_BLZ: 'blzeth',
        CURRENCY_PAIR.ETH_TO_REQ: 'reqeth',
        CURRENCY_PAIR.ETH_TO_LINK: 'linketh',
        CURRENCY_PAIR.ETH_TO_LSK: 'lsketh',
        CURRENCY_PAIR.ETH_TO_NAS: 'naseth',
        CURRENCY_PAIR.ETH_TO_ELA: 'elaeth',

        CURRENCY_PAIR.USDT_TO_DASH: 'dashusdt',
        CURRENCY_PAIR.USDT_TO_BTC: 'btcusdt',
        CURRENCY_PAIR.USDT_TO_LTC: 'ltcusdt',
        CURRENCY_PAIR.USDT_TO_XRP: 'xrpusdt',
        CURRENCY_PAIR.USDT_TO_BCC: 'bchusdt',
        CURRENCY_PAIR.USDT_TO_ETC: 'etcusdt',
        CURRENCY_PAIR.USDT_TO_OMG: 'omgusdt',
        CURRENCY_PAIR.USDT_TO_QTUM: 'qtumusdt',
        CURRENCY_PAIR.USDT_TO_ETH: 'ethusdt',
        CURRENCY_PAIR.USDT_TO_ZEC: 'zecusdt',
        CURRENCY_PAIR.USDT_TO_NEO: 'neousdt',
        CURRENCY_PAIR.USDT_TO_EOS: 'eosusdt',

        CURRENCY_PAIR.USDT_TO_HSR: 'hsrusdt',
        CURRENCY_PAIR.USDT_TO_ZIL: 'zilusdt',
        CURRENCY_PAIR.USDT_TO_VEN: 'venusdt',
        CURRENCY_PAIR.USDT_TO_ELF: 'elfusdt',
        CURRENCY_PAIR.USDT_TO_NAS: 'nasusdt',
        CURRENCY_PAIR.USDT_TO_ELA: 'elausdt',

    }.get(pair_id)


def get_currency_pair_from_huobi(pair_name):
    return {
        'dashbtc': CURRENCY_PAIR.BTC_TO_DASH,
        'ethbtc': CURRENCY_PAIR.BTC_TO_ETH,
        'ltcbtc': CURRENCY_PAIR.BTC_TO_LTC,
        'xrpbtc': CURRENCY_PAIR.BTC_TO_XRP,
        'bchbtc': CURRENCY_PAIR.BTC_TO_BCC,
        'etcbtc': CURRENCY_PAIR.BTC_TO_ETC,
        'xembtc': CURRENCY_PAIR.BTC_TO_XEM,
        'omgbtc': CURRENCY_PAIR.BTC_TO_OMG,
        'zecbtc': CURRENCY_PAIR.BTC_TO_ZEC,
        'neobtc': CURRENCY_PAIR.BTC_TO_NEO,
        'qtumbtc': CURRENCY_PAIR.BTC_TO_QTUM,
        'btgbtc': CURRENCY_PAIR.BTC_TO_BTG,
        'batbtc': CURRENCY_PAIR.BTC_TO_BAT,
        'rcnbtc': CURRENCY_PAIR.BTC_TO_RCN,
        'zrxbtc': CURRENCY_PAIR.BTC_TO_ZRX,
        'lskbtc': CURRENCY_PAIR.BTC_TO_LSK,
        'engbtc': CURRENCY_PAIR.BTC_TO_ENG,
        'trxbtc': CURRENCY_PAIR.BTC_TO_TRX,
        'eosbtc': CURRENCY_PAIR.BTC_TO_EOS,
        'icxbtc': CURRENCY_PAIR.BTC_TO_ICX,
        'rdnbtc': CURRENCY_PAIR.BTC_TO_RDN,
        'qspbtc': CURRENCY_PAIR.BTC_TO_QSP,

        'ontbtc': CURRENCY_PAIR.BTC_TO_ONT,
        'hsrbtc': CURRENCY_PAIR.BTC_TO_HSR,
        'zilbtc': CURRENCY_PAIR.BTC_TO_ZIL,
        'venbtc': CURRENCY_PAIR.BTC_TO_VEN,
        'elfbtc': CURRENCY_PAIR.BTC_TO_ELF,
        'blzbtc': CURRENCY_PAIR.BTC_TO_BLZ,
        'reqbtc': CURRENCY_PAIR.BTC_TO_REQ,
        'linkbtc': CURRENCY_PAIR.BTC_TO_LINK,
        'nasbtc': CURRENCY_PAIR.BTC_TO_NAS,
        'elabtc': CURRENCY_PAIR.BTC_TO_ELA,

        'omgeth': CURRENCY_PAIR.ETH_TO_OMG,
        'qtumeth': CURRENCY_PAIR.ETH_TO_QTUM,
        'bateth': CURRENCY_PAIR.ETH_TO_BAT,
        'rcneth': CURRENCY_PAIR.ETH_TO_RCN,
        'engeth': CURRENCY_PAIR.ETH_TO_ENG,
        'trxeth': CURRENCY_PAIR.ETH_TO_TRX,
        'eoseth': CURRENCY_PAIR.ETH_TO_EOS,
        'icxeth': CURRENCY_PAIR.ETH_TO_ICX,
        'rdneth': CURRENCY_PAIR.ETH_TO_RDN,
        'qspeth': CURRENCY_PAIR.ETH_TO_QSP,

        'onteth': CURRENCY_PAIR.ETH_TO_ONT,
        'hsreth': CURRENCY_PAIR.ETH_TO_HSR,
        'zileth': CURRENCY_PAIR.ETH_TO_ZIL,
        'veneth': CURRENCY_PAIR.ETH_TO_VEN,
        'elfeth': CURRENCY_PAIR.ETH_TO_ELF,
        'blzeth': CURRENCY_PAIR.ETH_TO_BLZ,
        'reqeth': CURRENCY_PAIR.ETH_TO_REQ,
        'linketh': CURRENCY_PAIR.ETH_TO_LINK,
        'lsketh': CURRENCY_PAIR.ETH_TO_LSK,
        'naseth': CURRENCY_PAIR.ETH_TO_NAS,
        'elaeth': CURRENCY_PAIR.ETH_TO_ELA,

        'dashusdt': CURRENCY_PAIR.USDT_TO_DASH,
        'btcusdt': CURRENCY_PAIR.USDT_TO_BTC,
        'ltcusdt': CURRENCY_PAIR.USDT_TO_LTC,
        'xrpusdt': CURRENCY_PAIR.USDT_TO_XRP,
        'bchusdt': CURRENCY_PAIR.USDT_TO_BCC,
        'etcusdt': CURRENCY_PAIR.USDT_TO_ETC,
        'omgusdt': CURRENCY_PAIR.USDT_TO_OMG,
        'qtumusdt': CURRENCY_PAIR.USDT_TO_QTUM,
        'ethusdt': CURRENCY_PAIR.USDT_TO_ETH,
        'zecusdt': CURRENCY_PAIR.USDT_TO_ZEC,
        'neousdt': CURRENCY_PAIR.USDT_TO_NEO,
        'eosusdt': CURRENCY_PAIR.USDT_TO_EOS,

        'hsrusdt': CURRENCY_PAIR.USDT_TO_HSR,
        'zilusdt': CURRENCY_PAIR.USDT_TO_ZIL,
        'venusdt': CURRENCY_PAIR.USDT_TO_VEN,
        'elfusdt': CURRENCY_PAIR.USDT_TO_ELF,
        'nasusdt': CURRENCY_PAIR.USDT_TO_NAS,
        'elausdt': CURRENCY_PAIR.USDT_TO_ELA,

    }.get(pair_name)