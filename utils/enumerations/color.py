from enum import Enum

class Color(Enum):
    """Enumeration representing card colors."""
    
    DIAMOND = 1
    SPADE   = 2
    HEART   = 3
    CLUB    = 4
    
    def __str__(self) -> str:
        
        match self:
            
            case self.DIAMOND: return 'D'
            case self.SPADE:   return 'S'
            case self.HEART:   return 'H'
            case self.CLUB:    return 'C'
    
    @staticmethod
    def __list__() -> list:
        """Return a list of all card colors."""
        return [Color.__members__[color.name] for color in Color]
