from utils.card import Card

class Community():
    
    def __init__(self, community_card_list: list[Card]) -> None:
        if len(community_card_list) != 8:
            print("Error: cannot create a community without exactly 8 cards")
            exit()
            
        self.flop: list = community_card_list[1:4]
        self.turn: Card = community_card_list[5]
        self.river: Card = community_card_list[7]
    
    def __flop__(self) -> list[Card]:
        return self.flop
    
    def __turn__(self) -> Card:
        return self.turn
    
    def __river__(self) -> Card:
        return self.river
    
    def __str__(self) -> str:
        return f"{[card.__str__() for card in self.__flop__() + [self.__turn__(), self.__river__()]]}"
    
    def get_phase_comminity(self, current_phase: int) -> list[Card]:
        """Give community cards that corresponds to current phase

        Args:
            current_phase (int): a number in {0,1,2,3}

        Returns:
            list: current phase community card list
        """
        match (current_phase):
            case 0: return []
            case 1: return self.__flop__()
            case 2: return self.__flop__() + [self.__turn__()]
            case 3: return self.__flop__() + [self.__turn__()] + [self.__river__()]
            case _: 
                print("Error: current_phase must be an element of {0,1,2,3}")
                exit()