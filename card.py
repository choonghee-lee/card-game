class Card:
    CARD_TYPE_YEOL = 'yeol'
    CARD_TYPE_PI = 'pi'

    def __init__(self, month, kind=CARD_TYPE_YEOL):
        self.month = month
        self.kind = kind
