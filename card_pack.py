import random
from typing import Any 
from card import Card


class CardPack(Card):
    
    def __init__(self, card_pack_card_list: list) -> None:
        
        self.card_list: list = card_pack_card_list
    
    def __card_list__(self) -> list:
        
        return self.card_list
    
    def __str__(self) -> str:
        
        return f"{[card.__str__() for card in self.card_list]}"
    
    def __get_random_card__(self) -> Card:
        
        return random.choice(self.card_list)
    
    def __remove_card__(self, card: Card) -> None:
        
        self.card_list.remove(card)
        
    def __get_and_remove_random_card__(self) -> Card:
        
        a_card: Card = self.__get_random_card__()
        self.__remove_card__(self, a_card)
        #TODO