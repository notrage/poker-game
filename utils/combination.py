from utils.enumerations.poker_hand_rank import PokerHandRank
from utils.enumerations.value import Value
from utils.enumerations.color import Color
from utils.card import Card

class Combination():
    """Represent a playing card combination."""
    
    def __init__(self, combination_card_list: list[Card]) -> None:
        
        self.card_list : list[Card] = combination_card_list
        
    def __card_list__(self) -> list[Card]:
        
        return self.card_list
    
    def __str__(self) -> str:
        
        return f"{[card.__str__() for card in self.__card_list__()]}"
    
    def value_list(self) -> list[Value]:
        """Return a Combination's value list, a list of every Card's value."""
        return [card.__value__() for card in self.__card_list__()]
    
    def group_by_value(self) -> dict:
        """Return a Combination's grouped value dict, having the count of each Card's value."""
        value_list: list[Value] = self.value_list()
        return {value: value_list.count(value) for value in value_list}
    
    def group_by_color(self) -> dict:
        """Return a Combination's grouped color dict, having the count of each Card's color."""
        color_list: list[Color] = [card.__color__() for card in self.__card_list__()]
        return {color: color_list.count(color) for color in color_list}
    
    def sort_by_value(self) -> None:
        """Sort the Combination's card_list by descending value order."""
        self.card_list.sort(key = lambda card: card.__value__().value, reverse = True)
   
    @staticmethod
    def remove_value_occurences(list: list[Value], value: Value) -> list[Value]:
        """Return a Combination's value excluded list."""
        return [v for v in list if v != value]
    
    def is_pair(self) -> bool:
        """Return if the Combination is a pair or not."""
        for count in self.group_by_value().values():
            
            if count == 2: return True
            
        return False
    
    def is_two_pair(self) -> bool:
        """Return if the Combination is a two pair or not."""
        value_dict: dict = self.group_by_value()
        pair_value_list: list[Value] = [value for value in value_dict if value_dict[value] == 2]

        return True if len(pair_value_list) >= 2 else False
    
    def is_three_of_kind(self) -> bool:
        """Return if the Combination is a three of kind or not."""
        for count in self.group_by_value().values():
            
            if count == 3: return True
            
        return False
    
    def is_straight(self) -> bool:
        """Return if the Combination is a straight or not."""
        if len(self.__card_list__()) >= 5:
            
            self.sort_by_value()
            value_list: list[Value] = self.value_list()
            # Check if we are in the first straight case (with ACE as ONE)
            if all(value in value_list for value in [Value.ACE, Value.TWO, Value.THREE, Value.FOUR, Value.FIVE]):
                
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
    
    def is_flush(self) -> bool:
        """Return if the Combination is a flush or not."""
        for count in self.group_by_color().values():
            
            if count >= 5: return True
            
        return False
    
    def is_full_house(self) -> bool:
        """Return if the Combination is a full house or not."""
        if (self.is_pair() or self.is_two_pair()) and self.is_three_of_kind(): 
            
            return True
        
        return False
    
    def is_four_of_kind(self) -> bool:
        """Return if the Combination is a four of kind or not."""
        for count in self.group_by_value().values():
            
            if count == 4: return True
            
        return False
    
    def is_straight_flush(self) -> bool:
        """Return if the Combination is a straight flush or not."""
        if self.is_flush():
            
            # Check if we are in one of first straight case (with ACE as ONE)
            if ( all(card in self.__str__() for card in ["AC", "2C", "3C", "4C", "5C"]) or
                 all(card in self.__str__() for card in ["AD", "2D", "3D", "4D", "5D"]) or
                 all(card in self.__str__() for card in ["AH", "2H", "3H", "4H", "5H"]) or
                 all(card in self.__str__() for card in ["AS", "2S", "3S", "4S", "5S"]) ):
                return True
            
            self.sort_by_value()
            color_dict: dict = self.group_by_color()
            
            flush_cards: list[Card] = [card for card in self.__card_list__() if color_dict[card.__color__()] >= 5]
            
            flush_value_list: list[Value] = [card.__value__() for card in flush_cards]       
            values_in_row: int = 0
            
            for index, card_value in enumerate(flush_value_list):
                
                value_rank: int = card_value.value
                previous_value_rank: int = flush_value_list[index-1].value
                # It's the start of iteration
                if index == 0 : values_in_row = 1
                # The value is the same than previous one (doesn't affect straight reaserch)
                elif value_rank == previous_value_rank: pass
                # The value continue the current straight research
                elif value_rank == previous_value_rank - 1: values_in_row += 1
                # The value jump at least the previous one by one value (restart the straight research)
                else: values_in_row = 0
                
                if values_in_row == 5: return True
            
        else: return False
    
    def is_royal_flush(self) -> bool:
        """Return if the Combination is a royal flush or not."""
        # Check if we are in one of first straight case (with ACE as ONE)
        if ( all(card in self.__str__() for card in ["AC", "KC", "QC", "JC", "10C"]) or
             all(card in self.__str__() for card in ["AD", "KD", "QD", "JD", "10D"]) or
             all(card in self.__str__() for card in ["AH", "KH", "QH", "JH", "10H"]) or
             all(card in self.__str__() for card in ["AS", "KS", "QS", "JS", "10S"]) ):
            return True
            
        return False
    
    def poker_hand_rank(self) -> PokerHandRank:
        """Return what PokerHandRank the Combination is."""
        if self.is_royal_flush():    return PokerHandRank.ROYAL_FLUSH
        if self.is_straight_flush(): return PokerHandRank.STRAIGHT_FLUSH
        if self.is_four_of_kind():   return PokerHandRank.FOUR_OF_KIND
        if self.is_full_house():     return PokerHandRank.FULL_HOUSE
        if self.is_flush():          return PokerHandRank.FLUSH
        if self.is_straight():       return PokerHandRank.STRAIGHT
        if self.is_three_of_kind():  return PokerHandRank.THREE_OF_KIND
        if self.is_two_pair():       return PokerHandRank.TWO_PAIR
        if self.is_pair():           return PokerHandRank.PAIR
        
        return PokerHandRank.HIGH_CARD
    
    def value_to_compares(self) -> list[Value]:
        """Return the most important card_list, depending of Combination's PokerHandRank"""
        self.sort_by_value()
        value_list: list[Value] = self.value_list()

        match (self.poker_hand_rank()):
        
            case PokerHandRank.HIGH_CARD: 
                
                return [card_value.value for card_value in value_list[0:5]]
            
            case PokerHandRank.PAIR: 
                
                value_dict: dict = self.group_by_value()
                # Getting the pair CardValue's
                pair_value_list: list[Value] = [value for value, count in value_dict.items() if count == 2]
                # Getting out the pair from CardValue's list                
                value_list = self.remove_value_occurences(value_list, pair_value_list[0])
                
                return [card_value.value for card_value in pair_value_list + value_list[0:3]]
                
            case PokerHandRank.TWO_PAIR: 
                
                value_dict: dict = self.group_by_value()
                # Getting the pairs CardValue's
                pair_value_list: list[Value] = [value for value, count in value_dict.items() if count == 2]
                # If there is 3 pairs
                if len(pair_value_list) == 3: pair_value_list = pair_value_list[0:2]
                # Getting out the pairs from CardValue's list
                for pair_value in pair_value_list:
                    
                    value_list = self.remove_value_occurences(value_list, pair_value)
                        
                return [card_value.value for card_value in pair_value_list + [value_list[0]]]
                    
            case PokerHandRank.THREE_OF_KIND: 
                
                value_dict: dict = self.group_by_value()
                # Getting the three of kind CardValue's
                three_of_kind_value_list: list[Value] = [value for value, count in value_dict.items() if count == 3]
                # Getting out the three of kind from CardValue's list
                value_list = self.remove_value_occurences(value_list, three_of_kind_value_list[0])
                                
                return [card_value.value for card_value in three_of_kind_value_list + value_list[0:2]]
                
            case PokerHandRank.STRAIGHT:
                
                # Check if we are in the first straight case (with ACE as ONE)
                if all(value in value_list for value in [Value.ACE, Value.TWO, Value.THREE, Value.FOUR, Value.FIVE]):
                    return [Value.FIVE.value]
                
                values_in_row: int = 0
                highest_straight_value: Value = Value.TWO
                
                for index, card_value in enumerate(value_list):
                    
                    value_rank: int = card_value.value
                    previous_value_rank: int = value_list[index-1].value
                    # It's the start of iteration
                    if index == 0 : values_in_row, highest_straight_value = 1, card_value
                    # The value is the same than previous one (doesn't affect straight reaserch)
                    elif value_rank == previous_value_rank: pass
                    # The value continue the current straight research
                    elif value_rank == previous_value_rank - 1: values_in_row += 1
                    # The value jump at least the previous one by one value (restart the straight research)
                    else: values_in_row, highest_straight_value = 0, card_value                        
                    
                    if values_in_row == 5: return [highest_straight_value.value] 
            
            case PokerHandRank.FLUSH: 
                
                color_dict: dict = self.group_by_color()
                
                for card in self.__card_list__():
                    
                    for color, count in color_dict.items():
                        
                        if card.__color__() == color and count >= 5: return [card.__value__().value]
            
            case PokerHandRank.FULL_HOUSE: 
                
                value_dict: dict = self.group_by_value()
                # Getting the three of kind CardValue's
                three_of_kind_value_list: list[Value] = [value for value, count in value_dict.items() if count == 3]
                # If there is 2 three of kind
                if len(three_of_kind_value_list) == 2: three_of_kind_value_list = [three_of_kind_value_list[0]]
                # Getting the pair CardValue's it can also be a three of kind value that count as pair in the full house
                pair_value_list: list[Value] = [value for value, count in value_dict.items() if count >= 2]
                
                return [card_value.value for card_value in three_of_kind_value_list + [pair_value_list[0]]]
            
            case PokerHandRank.FOUR_OF_KIND: 
                
                value_dict: dict = self.group_by_value()
                # Getting the four of kind CardValue's
                four_of_kind_value_list: list[Value] = [value for value, count in value_dict.items() if count == 4]
                # Getting out the four of kind from CardValue's list
                value_list = self.remove_value_occurences(value_list, four_of_kind_value_list[0])
                
                return [card_value.value for card_value in four_of_kind_value_list + [value_list[0]]]
            
            case PokerHandRank.STRAIGHT_FLUSH:
                
                # Check if we are in one of first straight case (with ACE as ONE)
                if ( all(card in self.__str__() for card in ["AC", "2C", "3C", "4C", "5C"]) or
                     all(card in self.__str__() for card in ["AD", "2D", "3D", "4D", "5D"]) or
                     all(card in self.__str__() for card in ["AH", "2H", "3H", "4H", "5H"]) or
                     all(card in self.__str__() for card in ["AS", "2S", "3S", "4S", "5S"]) ):
                     return [Value.FIVE.value]
                
                color_dict: dict = self.group_by_color()
                flush_cards: list[Card] = [card for card in self.__card_list__() if color_dict[card.__color__()] >= 5]
                
                flush_value_list: list[Value] = [card.__value__() for card in flush_cards]       
                values_in_row: int = 0
                
                for index, card_value in enumerate(value_list):
                    
                    value_rank: int = card_value.value
                    previous_value_rank: int = flush_value_list[index-1].value
                    # It's the start of iteration
                    if index == 0 : values_in_row = 1
                    # The value is the same than previous one (doesn't affect straight reaserch)
                    elif value_rank == previous_value_rank: pass
                    # The value continue the current straight research
                    elif value_rank == previous_value_rank - 1: values_in_row += 1
                    # The value jump at least the previous one by one value (restart the straight research)
                    else: values_in_row = 0
                    
                    if values_in_row == 5: 
                        
                        return [flush_value_list[index-4].value]

            case PokerHandRank.ROYAL_FLUSH: return [Value.ACE.value]