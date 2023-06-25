from utils.enumerations.card_value import CardValue
from utils.enumerations.card_color import CardColor
from utils.enumerations.poker_hand import PokerHand
from utils.hand import Hand
from utils.card import Card

class Combination():
    
    def __init__(self, combination_hand: Hand, combination_community_cards: list[Card]) -> None:
        
        hand_cards: list[Card] = combination_hand.__cards__()
        
        assert len(hand_cards + combination_community_cards) in {2, 5, 6, 7}, "Error, number of Combination's cards must be an element of {2, 5, 6, 7}"
        
        self.cards : list[Card] = hand_cards + combination_community_cards
        
    def __cards__(self) -> list[Card]:
        
        return self.cards
    
    def __str__(self) -> str:
        
        return f"Combination: {[card.__str__() for card in self.__cards__()]}"
    
    def __group_by_value__(self) -> dict:
        
        value_list: list[CardValue] = [card.__value__() for card in self.__cards__()]
        return {value: value_list.count(value) for value in value_list}
    
    def __group_by_value_str__(self) -> str:
        
        value_dict_to_str: dict = {value.__str__(): count for (value,count) in self.__group_by_value__().items()}
        return f"Comination ordered by value: {value_dict_to_str}"
    
    def __group_by_color__(self) -> dict:
        
        color_list: list[CardColor] = [card.__color__() for card in self.__cards__()]
        return {color: color_list.count(color) for color in color_list}
    
    def __group_by_color_str__(self) -> str:
        
        color_dict_to_str: dict = {color.__str__(): count for (color, count) in self.__group_by_color__().items()}
        return f"Combination ordered by color: {color_dict_to_str}"
    
    def __sort_by_value__(self) -> None:
        
        # Sort the Combination's cards by ascending order
        self.cards.sort(key = lambda card: card.__value__().value, reverse = True)
            
    def __is_pair__(self) -> bool:
        
        value_dict: dict = self.__group_by_value__()
        # Check if a value has an occurrence of 2
        for count in value_dict.values():
            if count == 2: return True
            
        return False
    
    def __is_two_pair__(self) -> bool:
        
        value_dict: dict = self.__group_by_value__()
        
        pair_value_list: list[CardValue] = [value for value in value_dict if value_dict[value]==2]
        # Check if there is at least two pair values
        if len(pair_value_list) >= 2:
            return True
        
        return False
    
    def __is_three_of_kind__(self) -> bool:
        
        value_dict: dict = self.__group_by_value__()
        # Check if there is an occurrence of 3
        for count in value_dict.values():
            if count == 3: return True
            
        return False
    
    def __is_straight__(self) -> bool:
        
        if len(self.__cards__()) >= 5:
            
            self.__sort_by_value__()
            value_list: list[CardValue] = [card.__value__() for card in self.__cards__()]
            
            values_in_row: int = 0
            
            for index, card_value in enumerate(value_list):
                # It's the start of iteration
                if index == 0 : values_in_row = 1
                # The next value is the same (doesn't affect straight reaserch)
                elif card_value.value == value_list[index-1].value: pass
                # The next value continue the current straight 
                elif card_value.value == value_list[index-1].value - 1: values_in_row += 1
                # The next value jump at least one value (restart the straight research)
                else: values_in_row = 0
                
                if values_in_row == 5: return True

        return False
    
    def __is_flush__(self) -> bool:
        
        #TODO
        return