from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Static(Page):
    form_model = 'player'
    form_fields = ['static_securities']

    def vars_for_template(self):
        return {'num_states': self.subsession.num_periods+1}

    def before_next_page(self):
        self.player.static_get_outcome()


class StaticResults(Page):

    def vars_for_template(self):
        num_states = self.subsession.num_periods+1
        return {'num_states': num_states,
                'realized_lottery': num_states + 1 - self.player.static_realized_state}


page_sequence = [
    Introduction,
    Static,
    StaticResults
]
