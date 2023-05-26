from utils.hand import Hand

class Player:
    
    def __init__(self, player_name: str, player_money: int, player_hand: Hand) -> None:
        
        self.name: str = player_name
        self.money: int = player_money
        self.hand: Hand = player_hand
        
    def __name__(self) -> str:
        return self.name
    
    def __money__(self) -> int:
        return self.money
    
    def __hand__(self) -> Hand:
        return self.hand
    
    def __str__(self) -> str:
        return f"nom: {self.__name__()}, argent: {self.__money__()},  main: {self.__hand__().__str__()}"