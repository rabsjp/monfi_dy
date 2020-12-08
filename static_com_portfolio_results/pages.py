from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class StaticResults(Page):

    def vars_for_template(self):
        r = self.round_number
        realized_state = self.participant.vars["static_realized_state_round{}".format(r)]
        num_states = self.session.vars["static_num_periods_round{}".format(r)]+1
        return {
            'num_states': num_states,
            'prices': self.session.vars["static_prices_round{}".format(r)],
            'quantities': self.participant.vars["static_securities_round{}".format(r)],
            'realized_lottery': num_states + 1 - realized_state,
            'realized_pay': self.participant.vars["static_realized_pay_round{}".format(r)]
        }


page_sequence = [
    StaticResults
]
