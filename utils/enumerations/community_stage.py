from enum import Enum

class CommunityStage(Enum):
    """Enumeration representing community stages."""
    
    EMPTY = 0
    FLOP  = 1
    TURN  = 2
    RIVER = 3
    
    def __str__(self) -> str:
        
        match self:
            
            case self.EMPTY: return "EMPTY"
            case self.FLOP:  return "FLOP"
            case self.TURN:  return "TURN"
            case self.RIVER: return "RIVER"
    
    def next_community_stage(self) -> "CommunityStage":
        
        assert self != self.RIVER, "Error, there is no community stage after the RIVER's one"
        
        match self:
            
            case self.EMPTY: return self.FLOP
            case self.FLOP:  return self.TURN
            case self.TURN:  return self.RIVER