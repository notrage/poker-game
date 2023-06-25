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
            
            case self.HIGH_CARD: return "high card"
            case self.PAIR: return "pair"
            case self.TWO_PAIR: return "two pair"
            case self.THREE_OF_KIND: return "three of kind"
            case self.STRAIGHT: return "straight"
            case self.FLUSH: return "flush"
            case self.FULL_HOUSE: return "full house"
            case self.FOUR_OF_KIND: return "four of kind"
            case self.STRAIGHT_FLUSH: return "straight flush"
            case self.ROYAL_FLUSH: return "royal flush"
    
    def __list__(self) -> list:
        
        return [PokerHand.__members__[poker_hand.name] for poker_hand in PokerHand]