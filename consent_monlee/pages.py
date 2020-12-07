from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class Consent(Page):
    form_model = 'player'
    form_fields = ['name','accept']
    
    def error_message(self, values):
        if values['name'] and values['accept'] == None:
            return 'If you accept the terms, you must enter your name'

page_sequence = [
    Consent,
    ]
    