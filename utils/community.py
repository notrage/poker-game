from utils.card import Card

class Community():
    
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
        
        return f"{[card.__str__() for card in self.__flop__() + [self.__turn__(), self.__river__()]]}"
    
    def get_phase_comminity_cards(self, phase: int) -> list[Card]:
        """give community cards that corresponds to current phase

        Args:
            current_phase (int): a number in {0,1,2,3}

        Returns:
            list: current phase community card list
        """
        
        assert phase in {0, 1, 2, 3}, "Error: current_phase must be an element of {0,1,2,3}"
        
        match (phase):
            case 0: return []
            case 1: return self.__flop__()
            case 2: return self.__flop__() + [self.__turn__()]
            case 3: return self.__flop__() + [self.__turn__(), self.__river__()]
            
    def __phase_comminity_cards_str__(self, phase: int) -> str:
        
        return f"{[card.__str__() for card in self.get_phase_comminity_cards(phase)]}"