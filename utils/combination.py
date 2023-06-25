from utils.enumerations.card_value import CardValue
from utils.enumerations.card_color import CardColor
from utils.enumerations.poker_hand import PokerHand
from utils.hand import Hand
from utils.card import Card

class Combination():
    
    def __init__(self, combination_hand: Hand, combination_community_cards: list[Card]) -> None:
        
        assert len(combination_hand.__cards__() + combination_community_cards) in {2, 5, 6, 7}, "Error, number of Combination's cards must be an element of {2, 5, 6, 7}"
        
        self.cards : list[Card] = combination_hand.__cards__() + combination_community_cards
        
    def __cards__(self) -> list[Card]:
        
        return self.cards
    
    def __str__(self) -> str:
        
        return f"Combination: {[card.__str__() for card in self.__cards__()]}"
    
    def __order_by_value__(self) -> dict:
        
        value_list: list[CardValue] = [card.__value__() for card in self.__cards__()]
        return {value: value_list.count(value) for value in value_list}
    
    def __order_by_value_str__(self) -> str:
        
        value_dict_to_str: dict = {value.__str__(): count for (value,count) in self.__order_by_value__().items()}
        return f"Comination ordered by value: {value_dict_to_str}"
    
    def __order_by_color__(self) -> dict:
        
        color_list: list[CardColor] = [card.__color__() for card in self.__cards__()]
        return {color: color_list.count(color) for color in color_list}
    
    def __order_by_color_str__(self) -> str:
        
        color_dict_to_str: dict = {color.__str__(): count for (color, count) in self.__order_by_color__().items()}
        return f"Combination ordered by color: {color_dict_to_str}"
    
    def __is_pair__(self) -> bool:
        
        # TODO
        return