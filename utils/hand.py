from utils.card import Card

class Hand():
    
    def __init__(self, hand_card_list) -> None:
        if len(hand_card_list) != 2:
            print("Error: cannot create a hand of cards without exactly 2 cards")
            exit()
            
        self.card_list = hand_card_list
        
    def __card_list__(self) -> list[Card]:
        return self.card_list
    
    def __str__(self) -> str:
        return f"{self.__card_list__()}"
    