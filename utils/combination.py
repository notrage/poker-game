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
        # Check if a value has an occurrence of 2
        for count in self.__group_by_value__().values():
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
        # Check if there is an occurrence of 3
        for count in self.__group_by_value__().values():
            if count == 3: return True
            
        return False
    
    def __is_straight__(self) -> bool:
        
        if len(self.__cards__()) >= 5:
            
            self.__sort_by_value__()
            value_list: list[CardValue] = [card.__value__() for card in self.__cards__()]
            
            # Check if we are in the first straight case (with ACE as ONE)
            if all(value in value_list for value in [CardValue.ACE, CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE]):
                return True
            
            values_in_row: int = 0
            
            for index, card_value in enumerate(value_list):
                
                value_rank: int = card_value.value
                previous_value_rank: int = value_list[index-1].value
                # It's the start of iteration
                if index == 0 : values_in_row = 1
                # The value is the same than previous one (doesn't affect straight reaserch)
                elif value_rank == previous_value_rank: pass
                # The value continue the current straight research
                elif value_rank == previous_value_rank - 1: values_in_row += 1
                # The value jump at least the previous one by one value (restart the straight research)
                else: values_in_row = 0
                
                if values_in_row == 5: return True

        return False
    
    def __is_flush__(self) -> bool:
        # Check if a color has an occurrence of 5
        for count in self.__group_by_color__().values():
            if count == 5: return True
            
        return False
    
    def __is_full_house__(self) -> bool:
        # Check if the Comination contain both pair and three of kind (with differents values)
        if (self.__is_pair__() or self.__is_two_pair__()) and self.__is_three_of_kind__():
            return True
        
        return False
    
    def __is_four_of_kind__(self) -> bool:
        # Check if a value has and occurence of 4
        for count in self.__group_by_value__().values():
            if count == 4: return True
            
        return False
    
    def __is_straight_flush__(self) -> bool:
        
        if len(self.__cards__()) >= 5:
            
            # Check if we are in one of first straight case (with ACE as ONE)
            #TODO c'est pas au point du tout
            if (all(card in self.__cards__() for card in [Card(CardValue.ACE, CardColor.CLUB), Card(CardValue.TWO, CardColor.CLUB), Card(CardValue.THREE, CardColor.CLUB), Card(CardValue.FOUR, CardColor.CLUB), Card(CardValue.FIVE, CardColor.CLUB)]) or
                all(card in self.__cards__() for card in [Card(CardValue.ACE, CardColor.DIAMOND), Card(CardValue.TWO, CardColor.DIAMOND), Card(CardValue.THREE, CardColor.DIAMOND), Card(CardValue.FOUR, CardColor.DIAMOND), Card(CardValue.FIVE, CardColor.DIAMOND)]) or
                all(card in self.__cards__() for card in [Card(CardValue.ACE, CardColor.HEART), Card(CardValue.TWO, CardColor.HEART), Card(CardValue.THREE, CardColor.HEART), Card(CardValue.FOUR, CardColor.HEART), Card(CardValue.FIVE, CardColor.HEART)]) or
                all(card in self.__cards__() for card in [Card(CardValue.ACE, CardColor.SPADE), Card(CardValue.TWO, CardColor.SPADE), Card(CardValue.THREE, CardColor.SPADE), Card(CardValue.FOUR, CardColor.SPADE), Card(CardValue.FIVE, CardColor.SPADE)]) ):
                return True
            
            self.__sort_by_value__()
            
            for index, card in enumerate(self.__cards__()):
                
                value_rank: int = card.__value__().value
                if index: previous_value_rank: int = current_straight_flush[-1].__value__().value
                # It's the start of iteration
                if index == 0: current_straight_flush: list[Card] = [card]
                # The value is the same than previous one (doesn't affect straight reaserch)
                elif value_rank == previous_value_rank: pass
                # The value continue the current straight research
                elif value_rank == previous_value_rank - 1:
                    # The color continue the current flush research
                    if card.__color__() == current_straight_flush[-1].__color__(): current_straight_flush.append(card)
                    # The color isn't the same than previous one (restart the flush research)
                    else: current_straight_flush = [card]
                # The value jump at least the previous one by one value (restart the straight research)
                else: current_straight_flush = [card]
                    
                if len(current_straight_flush) == 5: return True     
                    
        return False
    
    def __is_royal_flush__(self) -> bool:
        
        #TODO
        return