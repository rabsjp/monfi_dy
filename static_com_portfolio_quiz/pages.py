from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import json


class Introduction(Page):
    pass


class Question2(Page):
    form_model = 'player'
    form_fields = ['answer2']

    def vars_for_template(self):
        prices_list = {"p_1": 0.037, "p_2": 0.2222,
                       "p_3": 0.4444, "p_4": 0.2964
                       }
        chance_list = {"pi_1": 0.125, "pi_2": 0.375,
                       "pi_3": 0.375, "pi_4": 0.125
                       }
        quantities_list = {"q_1": 0, "q_2": 0,
                           "q_3": 91.6, "q_4": 'X'}

        expenditures_list = {"e_1": 0, "e_2": 0,
                             "e_3": 40.7, "e_4": 59.3
                             }

        return {
            'num_states': 4,
            'prices': json.dumps(prices_list),
            'quantities': json.dumps(quantities_list),
            'expenditures': json.dumps(expenditures_list),
            'chances': json.dumps(chance_list),
            'realized_state': "",
            'initial_wealth': 100
        }


class Question4(Page):
    form_model = 'player'
    form_fields = ['answer4']

    def vars_for_template(self):
        prices_list = {"p_1": 0.037, "p_2": 0.2222,
                       "p_3": 0.4444, "p_4": 0.2964
                       }
        chance_list = {"pi_1": 0.125, "pi_2": 0.375,
                       "pi_3": 0.375, "pi_4": 0.125
                       }
        quantities_list = {"q_1": 401, "q_2": 210,
                           "q_3": 80, "q_4": 10}

        expenditures_list = {"e_1": 14.8, "e_2": 46.7,
                             "e_3": 35.6, "e_4": 3
                             }

        return {
            'num_states': 4,
            'prices': json.dumps(prices_list),
            'quantities': json.dumps(quantities_list),
            'expenditures': json.dumps(expenditures_list),
            'chances': json.dumps(chance_list),
            'realized_state': 2,
            'initial_wealth': 100
        }


class Question6(Page):
    form_model = 'player'
    form_fields = ['answer6']

    def vars_for_template(self):
        prices_list = {"p_1": 0.037, "p_2": 0.2222,
                       "p_3": 0.4444, "p_4": 0.2964
                       }
        chance_list = {"pi_1": 0.125, "pi_2": 0.375,
                       "pi_3": 0.375, "pi_4": 0.125
                       }
        quantities_list = {"q_1": 401, "q_2": 210,
                           "q_3": 80, "q_4": 10}

        expenditures_list = {"e_1": 14.8, "e_2": 46.7,
                             "e_3": 35.6, "e_4": 3
                             }

        return {
            'num_states': 4,
            'prices': json.dumps(prices_list),
            'quantities': json.dumps(quantities_list),
            'expenditures': json.dumps(expenditures_list),
            'chances': json.dumps(chance_list),
            'realized_state': 3,
            'initial_wealth': 100
        }


page_sequence = [
    Introduction,
    Question2,
    Question4,
    Question6,
]
