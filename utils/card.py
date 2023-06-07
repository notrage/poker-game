from utils.enumerations.card_value import CardValue
from utils.enumerations.card_color import CardColor

class Card:
    
    def __init__(self, card_value: CardValue, card_color: CardColor) -> None:
        
        self.value: CardValue = card_value
        self.color: CardColor = card_color
        
    def __value__(self) -> CardValue: 
        
        return self.value
    
    def __color__(self) -> CardColor:
        
        return self.color
    
    def __str__(self) -> str:
        
        return f"{self.value.__str__()}{self.color.__str__()}"
    
    def card_list_gen() -> list:
        """return a 52 list of Card

        Returns:
            list: a combination between every CardValue and CardColor
        """
        
        return [Card(card_value=v, card_color=c) for v in CardValue.__list__() for c in CardColor.__list__()]