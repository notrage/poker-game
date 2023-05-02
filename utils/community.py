from utils.card import Card
from utils.card_pack import CardPack

class Community():
    
    def __init__(self, community_card_list: list) -> None:
        if len(community_card_list) != 8:
            print("Error: cannot create a community without exactly 8 cards")
            exit()
            
        self.flop: list = community_card_list[1:4]
        self.turn: Card = community_card_list[5]
        self.river: Card = community_card_list[7]
        self.burnt:list = [community_card_list[0], community_card_list[4],community_card_list[6]]
    
    def __flop__(self) -> list:
        return self.flop
    
    def __turn__(self) -> Card:
        return self.turn
    
    def __river__(self) -> Card:
        return self.river
    
    def __burnt__(self) -> list:
        return self.burnt
    
    def __str__(self) -> str:
        return f"{[card.__str__() for card in self.__flop__()]} {self.__turn__().__str__()} {self.__river__().__str__()}"
    
    def get_phase_comminity(self, current_phase: int) -> list:
        
        match (current_phase):
            case 0: return []
            case 1: return self.__flop__()
            case 2: return self.__flop__() + [self.__turn__()]
            case 3: return self.__flop__() + [self.__turn__()] + [self.__river__()]
            case _: 
                print("Error: current_phase must be an element of [0,1,2,3]")
                exit()