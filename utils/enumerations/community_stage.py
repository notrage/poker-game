from enum import Enum

class CommunityStage(Enum):
    
    EMPTY = 0
    FLOP = 1
    TURN = 2
    RIVER = 3
    
    def __str__(self) -> str:
        
        match(self):
            
            case self.EMPTY: return "empty"
            case self.FLOP: return "flop"
            case self.TURN: return "turn"
            case self.RIVER: return "river"
            
    def next_community_stage(self):
        
        assert self != self.RIVER, "Error, there is no community stage after the RIVER's one"
        
        match(self):
            
            case self.EMPTY: return self.FLOP
            case self.FLOP: return self.TURN
            case self.TURN: return self.RIVER