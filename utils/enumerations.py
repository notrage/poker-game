from enum import Enum

class CardValue(Enum):
    
    TWO   = 2  #'2'
    THREE = 3  #'3'
    FOUR  = 4  #'4'
    FIVE  = 5  #'5'
    SIX   = 6  #'6'
    SEVEN = 7  #'7'
    EIGHT = 8  #'8'
    NINE  = 9  #'9'
    TEN   = 10 #'10'
    JOKEY = 11 #'J'
    QUEEN = 12 #'Q'
    KING  = 13 #'K'
    ACE   = 14 #'A'
    
    def __str__(self) -> str:
        
        match(self):
            
            case self.TWO:   return '2'
            case self.THREE: return '3'
            case self.FOUR:  return '4'
            case self.FIVE:  return '5'
            case self.SIX:   return '6'
            case self.SEVEN: return '7'
            case self.EIGHT: return '8'
            case self.NINE:  return '9'
            case self.TEN:   return '10'
            case self.JOKEY: return 'J'
            case self.QUEEN: return 'Q'
            case self.KING:  return 'K'
            case self.ACE:   return 'A'
            
    def __list__() -> list: 
        return [CardValue.__members__[value.name] for value in CardValue]


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