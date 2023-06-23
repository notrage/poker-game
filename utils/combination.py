from hand import Hand
from card import Card

class Combination():
    
    def __init__(self, combination_hand: Hand, combination_community_cards: list[Card]) -> None:
        
        self.cards : list[Card] = combination_hand.__cards__() + combination_community_cards
        
    def __cards__(self) -> list[Card]:
        
        #TODO
        return
    
    