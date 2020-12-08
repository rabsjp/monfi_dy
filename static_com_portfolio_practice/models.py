from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import json
import numpy
from scipy.stats import binom
author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'static_com_portfolio_practice'
    players_per_group = None
    num_rounds = 2
    initial_wealth = 100
    up_prob = 0.5
    up_tick = 2
    down_tick = 0.5
    initial_wealth_list = [120, 80]
    num_periods = 2


class Subsession(BaseSubsession):
    num_periods = models.IntegerField()
    static_prices = models.StringField()
    static_chances = models.StringField()
    initial_wealth = models.IntegerField()

    def creating_session(self):
        if self.round_number == 1:
            num_rounds = Constants.num_rounds
            for r in range(1, num_rounds+1):
                t = Constants.num_periods
                self.in_round(r).num_periods = t
                self.in_round(r).initial_wealth = Constants.initial_wealth_list[r - 1]
                price_label = "p_{}"
                static_price_list = {"p_1": 0}
                price_label_com = "p_{}"
                prob_label_com = "pi_{}"
                static_price_list_com = {"p_1": 0}
                static_prob_list_com = {"pi_1": 0}

                for i in range(1, t+1, 1):
                    static_price_list_com[price_label_com.format(i)] = round(binom.pmf(i-1, t, 2.0/3), 4)
                    static_prob_list_com[prob_label_com.format(i)] = round(binom.pmf(i-1, t, 1.0/2), 4)

                static_price_list_com[price_label_com.format(t+1)] = 1.0000 - sum(static_price_list_com.values())
                static_prob_list_com[prob_label_com.format(t+1)] = 1.0000 - sum(static_prob_list_com.values())


                self.in_round(r).static_prices = json.dumps(static_price_list_com)
                self.in_round(r).static_chances = json.dumps(static_prob_list_com)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    static_securities = models.StringField()
    static_realized_state = models.IntegerField()
    static_realized_pay = models.FloatField()

    def static_get_outcome(self):
        self.static_realized_state = int(numpy.random.binomial(self.subsession.num_periods, 1.0/2, 1))+1
        securities_list = json.loads(self.static_securities)
        security_label = "q_{}"
        self.static_realized_pay = securities_list[security_label.format(self.static_realized_state)]
