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
    
    def add_money(self, amount: int) -> None:
        """add an amount of money to player's current money

        Args:
            amount (int): money to add
        """
        self.money += amount
        
    def sub_money(self, amount: int) -> None:
        """substract an amount of money to player's current money

        Args:
            amount (int): money to substract
        """
        self.money -= amount