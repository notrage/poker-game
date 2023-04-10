from enumerations import CardColor, CardValue

class Card:
    
    def __init__(self, card_value: CardValue, card_color: CardColor):
        
        self.value = card_value
        self.color = card_color
        
    def get_value(self): return self.value
    
    def get_color(self): return self.color
    
    def to_string(self): return str(self.value) + self.color
    
    def card_list_gen():
        return [Card(card_value=i_value, card_color=j_color) for ]