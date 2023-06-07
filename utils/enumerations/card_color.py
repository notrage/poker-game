from enum import Enum

class CardColor(Enum):
    
    DIAMOND = 1 #'D'
    SPADE   = 2 #'S'
    HEART   = 3 #'H'
    CLUB    = 4 #'C'
    
    def __str__(self) -> str:
        
        match (self):
            
            case self.DIAMOND: return 'D'
            case self.SPADE:   return 'S'
            case self.HEART:   return 'H'
            case self.CLUB:    return 'C'
    
    def __list__() -> list: 
        return [CardColor.__members__[color.name] for color in CardColor]