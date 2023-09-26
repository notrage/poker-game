from utils.enumerations.value import Value
from utils.enumerations.color import Color

class Card:
    """Represents a playing card."""
    
    def __init__(self, card_value: Value, card_color: Color) -> None:
        
        self.value: Value = card_value
        self.color: Color = card_color
        
    def __value__(self) -> Value: 
        
        return self.value
    
    def __color__(self) -> Color:
        
        return self.color
    
    def __str__(self) -> str:
        
        return f"{self.value.__str__()}{self.color.__str__()}"
    
    @staticmethod
    def card_list_gen() -> list:
        """Return a list of 52 cards, a combination of every Value and Color."""        
        return [Card(v, c) for v in Value.__list__() for c in Color.__list__()]