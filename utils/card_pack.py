import random

from utils.card import Card

class CardPack(Card):
    
    def __init__(self, card_pack_card_list: list[Card]) -> None:
        
        self.card_list: list = card_pack_card_list
    
    def __card_list__(self) -> list[Card]:
        return self.card_list
    
    def __str__(self) -> str:
        return f"{[card.__str__() for card in self.card_list]}"
    
    def __get_random_card__(self) -> Card:
        return random.choice(self.card_list)
    
    def __remove_card__(self, card: Card) -> None:
        if self.__card_list__() == []: 
            print("Error: cannot remove card from an empty CardPack")
            exit()
            
        self.card_list.remove(card)
        
    def __get_and_remove_random_card__(self) -> Card:
        a_card: Card = self.__get_random_card__()
        self.__remove_card__(a_card)
        return a_card
    
    def get_and_remove_mulitple_random_cards(self, n: int) -> list[Card]:
        """Give and remove n random cards from CardPack

        Args:
            n (int): number of card to get out

        Returns:
            list: list of n cards from CardPack
        """
        if n > len(self.__card_list__()):
            print("Error: n variable to high for this CardPack"); exit()
        
        cards: list[Card] = []
        for i in range(n):
            cards.append(self.__get_and_remove_random_card__())
        return cards