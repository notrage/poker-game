import logging

class Player:
    """Represent a poker player."""
    
    def __init__(self, player_name: str, player_money: int) -> None:
        
        self.name: str = player_name
        self.money: int = player_money
        
    def __name__(self) -> str:
        
        return self.name
    
    def __money__(self) -> int:
        
        return self.money
    
    def __str__(self) -> str:
        
        return f"Player's name: {self.__name__()}\Player's money: {self.__money__()}\n"
    
    def update_money(self, amount: int) -> None:
        """Update player's money

        Args:
            amount (int): money to add
        """
        self.money += amount
        logging.info(f"Player's money updated by {amount}")