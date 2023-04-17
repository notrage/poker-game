from enumerations import CardValue, CardColor

class Card:
    
    def __init__(self, card_value: CardValue, card_color: CardColor):
        
        self.value = card_value
        self.color = card_color
        
    def get_value(self) -> CardValue: 
        return self.value
    
    def get_color(self) -> CardColor: 
        return self.color
    
    def to_string(self) -> str: 
        return self.value.to_string() + self.color.to_string()
    
    def card_list_gen() -> list:
        return [Card(card_value=v, card_color=c) for v in CardValue.to_list() for c in CardColor.to_list()]