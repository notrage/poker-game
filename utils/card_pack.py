import random

from utils.card import Card

class CardPack(Card):
    
    def __init__(self) -> None:
        
        self.card_list: list[Card] = Card.card_list_gen()
    
    def __card_list__(self) -> list[Card]:
        
        return self.card_list
    
    def __str__(self) -> str:
        
        return f"{[card.__str__() for card in self.card_list]}"
    
    def __get_random_card__(self) -> Card:
        
        return random.choice(self.card_list)
    
    def __remove_card__(self, card: Card) -> None:
        
        assert self.__card_list__() != [], "Error: cannot remove card from an empty CardPack"
        self.card_list.remove(card)
        
    def __get_and_remove_random_card__(self) -> Card:
        
        a_card: Card = self.__get_random_card__()
        self.__remove_card__(a_card)
        return a_card
    
    def get_and_remove_random_cards(self, n: int) -> list[Card]:
        """remove n cards from the CardPack's cards and return them

        Args:
            n (int): number of card to get out

        Returns:
            list[Card]: list of n cards from CardPack
        """
        
        assert n < len(self.__card_list__()), "Error: n value is too high for this CardPack"
        return [self.__get_and_remove_random_card__() for i in range(n)]