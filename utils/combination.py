from utils.enumerations.community_stage import CommunityStage
from utils.enumerations.card_value import CardValue
from utils.enumerations.card_color import CardColor
from utils.enumerations.poker_hand import PokerHand
from utils.hand import Hand
from utils.card import Card
from utils.community import Community

class Combination():
    
    def __init__(self, combination_hand: Hand, combination_comuunity: Community, combination_community_stage: CommunityStage) -> None:
        
        self.hand_card_list: list[Card] = combination_hand.__cards__()
        self.community_card_list: list[Card] = combination_comuunity.get_stage_commnunity_cards(combination_community_stage)
        
        assert len(self.hand_card_list + self.community_card_list) in {2, 5, 6, 7}, "Error, number of Combination's cards must be an element of {2, 5, 6, 7}"
        
        self.card_list : list[Card] = self.hand_card_list + self.community_card_list
        
    def __hand_card_list__(self) -> list[Card]:
        
        return self.hand_card_list
    
    def __community_card_list__(self) -> list[Card]:
        
        return self.community_card_list
        
    def __cards__(self) -> list[Card]:
        
        return self.card_list
    
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
        self.card_list.sort(key = lambda card: card.__value__().value, reverse = True)
            
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
            if ( all(card in self.__str__() for card in ["AC", "2C", "3C", "4C", "5C"]) or
                 all(card in self.__str__() for card in ["AD", "2D", "3D", "4D", "5D"]) or
                 all(card in self.__str__() for card in ["AH", "2H", "3H", "4H", "5H"]) or
                 all(card in self.__str__() for card in ["AS", "2S", "3S", "4S", "5S"]) ):
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
        
        # Check if we are in one of first straight case (with ACE as ONE)
        if ( all(card in self.__str__() for card in ["AC", "KC", "QC", "JC", "10C"]) or
             all(card in self.__str__() for card in ["AD", "KD", "QD", "JD", "10D"]) or
             all(card in self.__str__() for card in ["AH", "KH", "QH", "JH", "10H"]) or
             all(card in self.__str__() for card in ["AS", "KS", "QS", "JS", "10S"]) ):
            return True
            
        return False
    
    def __poker_hand__(self) -> PokerHand:
        
        if self.__is_royal_flush__():    return PokerHand.ROYAL_FLUSH
        if self.__is_straight_flush__(): return PokerHand.STRAIGHT_FLUSH
        if self.__is_four_of_kind__():   return PokerHand.FOUR_OF_KIND
        if self.__is_full_house__():     return PokerHand.FULL_HOUSE
        if self.__is_flush__():          return PokerHand.FLUSH
        if self.__is_straight__():       return PokerHand.STRAIGHT
        if self.__is_three_of_kind__():  return PokerHand.THREE_OF_KIND
        if self.__is_two_pair__():       return PokerHand.TWO_PAIR
        if self.__is_pair__():           return PokerHand.PAIR
        
        return PokerHand.HIGH_CARD
    
    
    