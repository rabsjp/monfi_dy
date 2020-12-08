from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'instructions_link': self.session.config['instructions_link'],
        }


class Consent(Page):
    form_model = 'player'
    form_fields = ['name', 'payid', 'accept']
    
    def error_message(self, values):
        if values['name'] == None or values['payid']  == None or values['accept'] == None:
            return 'If you accept the terms, you must enter your name and PayID'

    def before_next_page(self):
        self.participant.vars['payid'] = self.player.payid
page_sequence = [
    #Introduction,
    Consent,
    ]
