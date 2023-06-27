from enum import Enum

class PokerHand(Enum):
    
    HIGH_CARD      = 1
    PAIR           = 2
    TWO_PAIR       = 3
    THREE_OF_KIND  = 4
    STRAIGHT       = 5
    FLUSH          = 6
    FULL_HOUSE     = 7
    FOUR_OF_KIND   = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH    = 10
    
    def __str__(self) -> str:
        
        match(self):
            
            case self.HIGH_CARD:      return "HICH CARD"
            case self.PAIR:           return "PAIR"
            case self.TWO_PAIR:       return "TWO PAIR"
            case self.THREE_OF_KIND:  return "THREE OF KIND"
            case self.STRAIGHT:       return "STRAIGHT"
            case self.FLUSH:          return "FLUSH"
            case self.FULL_HOUSE:     return "FULL HOUSE"
            case self.FOUR_OF_KIND:   return "FOUR OF KIND"
            case self.STRAIGHT_FLUSH: return "STRAIGHT FLUSH"
            case self.ROYAL_FLUSH:    return "ROYAL FLUSH"