from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'instructions_link': self.session.config['instructions_link'],
        }


class Question(Page):
    form_model = 'player'
    form_fields = ['submitted_answer']

    def vars_for_template(self):
        return {
            'table_link': self.session.config['table_link'],
        }


    def before_next_page(self):
        self.player.check_correct()


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return dict(
            player_in_all_rounds=player_in_all_rounds,
            questions_correct=sum([p.is_correct for p in player_in_all_rounds])
        )


page_sequence = [
    #Introduction,
    Question,
    Results
]
