from enum import Enum

class CardValue(Enum):
    
    #ONE   = 1
    TWO   = 2
    THREE = 3
    FOUR  = 4
    FIVE  = 5
    SIX   = 6
    SEVEN = 7
    EIGHT = 8
    NINE  = 9
    TEN   = 10
    JOKEY = 11
    QUEEN = 12
    KING  = 13
    ACE   = 14
    
    def __str__(self) -> str:
        
        match(self):
            
            #case self.ONE:   return '1'
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
