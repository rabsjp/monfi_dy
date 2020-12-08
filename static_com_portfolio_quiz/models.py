from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'static_portfolio_quiz'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    answer2 = models.IntegerField(
        choices=[
            [1, '2'],
            [2, '20'],
            [3, '200'],
            [4, '2000']
        ],
        widget=widgets.RadioSelect
    )

    def answer2_error_message(self, value):
        if value != 3:
            return 'Wrong answer, try again.'

    answer4 = models.IntegerField(
        choices=[
            [1, '37.5%'],
            [2, '12.5%'],
            [3, '50%'],
            [4, '100%']
        ],
        widget=widgets.RadioSelect
    )

    def answer4_error_message(self, value):
        if value != 1:
            return 'Wrong answer, try again.'

    answer6 = models.IntegerField(
        choices=[
            [1, '35.6'],
            [2, '37'],
            [3, '80'],
            [4, '44']
        ],
        widget=widgets.RadioSelect
    )

    def answer6_error_message(self, value):
        if value != 3:
            return 'Wrong answer, try again.'