from utils.enumerations.community_stage import CommunityStage
from utils.card import Card

class Community():
    """Represent a community, including flop, turn and river"""
    
    def __init__(self, community_card_list: list[Card]) -> None:
        
        assert len(community_card_list) == 8, "Error: cannot create a community without exactly 8 cards"
        
        self.flop:  list[Card] = community_card_list[1:4]
        self.turn:  Card = community_card_list[5]
        self.river: Card = community_card_list[7]
    
    def __flop__(self) -> list[Card]:
        
        return self.flop
    
    def __turn__(self) -> Card:
        
        return self.turn
    
    def __river__(self) -> Card:
        
        return self.river
    
    def __str__(self) -> str:
        
        return f"Community: {[card.__str__() for card in self.__flop__() + [self.__turn__(), self.__river__()]]}"
    
    def get_stage_commnunity_cards(self, stage: CommunityStage) -> list[Card]:
        """Give community cards that corresponds to current phase.

        Args:
            stage (CommunityStage): current community stage

        Returns:
            list: current phase community card list
        """
        match (stage):
            
            case CommunityStage.EMPTY: return []
            case CommunityStage.FLOP:  return self.__flop__()
            case CommunityStage.TURN:  return self.__flop__() + [self.__turn__()]
            case CommunityStage.RIVER: return self.__flop__() + [self.__turn__(), self.__river__()]