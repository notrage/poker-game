from random import choice as random_choice
from utils.card import Card

class CardPack(Card):
    """Represent a playing card pack."""
    
    def __init__(self) -> None:
        
        self.card_list: list[Card] = Card.card_list_gen()
    
    def __card_list__(self) -> list[Card]:
        
        return self.card_list
    
    def __str__(self) -> str:
        
        return f"CardPack: {[card.__str__() for card in self.__card_list__()]}"
    
    def get_random_card(self) -> Card:
        """Return a random CardPack's card."""        
        return random_choice(self.card_list)
    
    def remove_card(self, card: Card) -> None:
        """Remove a given CardPack's card.

        Args:
            card (Card): card to remove
        """
        assert card in self.__card_list__(), "Error: cannot remove a card that isn't in CardPack"
        self.card_list.remove(card)
        
    def get_and_remove_random_card(self) -> Card:
        """Return a random removed CardPack's card"""
        card: Card = self.get_random_card()
        self.remove_card(card)
        return card
    
    def get_and_remove_multiple_random_card(self, n: int) -> list[Card]:
        """Remove n cards from the CardPack's cards and return them.

        Args:
            n (int): number of card to get out

        Returns:
            list[Card]: list of n cards from CardPack
        """
        assert n < len(self.__card_list__()), "Error: n value is too high for this CardPack"
        return [self.get_and_remove_random_card() for i in range(n)]