from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'instructions_link_task2': self.session.config['instructions_link_task2'],
        }

page_sequence = [
    Page1
]
