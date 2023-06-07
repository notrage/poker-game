from utils.card import Card

class Hand():
    
    def __init__(self, hand_cards: list[Card]) -> None:
        
        assert len(hand_cards) == 2, "Error: cannot create a hand of cards without exactly 2 cards"
            
        self.cards = hand_cards
        
    def __cards__(self) -> list[Card]:
        
        return self.cards
    
    def __str__(self) -> str:
        
        return f"{[card.__str__() for card in self.__cards__()]}"
    