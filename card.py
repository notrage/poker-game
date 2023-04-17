from enumerations import CardValue, CardColor

class Card:
    
    def __init__(self, card_value: CardValue, card_color: CardColor):
        
        self.value = card_value
        self.color = card_color
        
    def get_value(self): return self.value
    
    def get_color(self): return self.color
    
    def to_string(self): return self.value.to_string() + self.color.to_string()
    
    def card_list_gen():
        return [Card(card_value=v, card_color=c) for v in CardValue.to_list() for c in CardColor.to_list()]