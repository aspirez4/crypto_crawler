from data.BaseData import BaseData
from utils.other_utils import get_next_id
from enums.deal_type import get_deal_type_by_id


class TradePair(BaseData):
    def __init__(self, deal_1, deal_2, timest_1, timest_2, deal_type):
        self.deal_1 = deal_1
        self.deal_2 = deal_2

        self.id = get_next_id()

        self.timest1 = timest_1
        self.timest2 = timest_2

        self.deal_type = deal_type

        self.current_profit = self.compute_profit(self.deal_1, self.deal_2)

    def __str__(self):
        str_repr = "Trade #{num} at timest1: {timest1} timest2: {timest2} type: {type}\n".format(
            num=self.id, timest1=self.timest1, timest2=self.timest2, type=get_deal_type_by_id(self.deal_type))
        str_repr += str(self.deal_1) + "\n"
        str_repr += str(self.deal_2) + "\n"
        str_repr += "Current profit - {bakshish}".format(bakshish=self.current_profit)

        return str_repr

    @staticmethod
    def compute_profit(deal_1, deal_2):
        # FIXME NOTE internal magic numbers >_<
        return deal_1.volume * deal_1.price * 0.9975 - deal_2.volume * deal_2.price * 1.0025