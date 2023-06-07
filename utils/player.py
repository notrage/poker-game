from utils.hand import Hand

class Player:
    
    def __init__(self, player_name: str, player_money: int) -> None:
        
        self.name: str = player_name
        self.money: int = player_money
        
    def __name__(self) -> str:
        return self.name
    
    def __money__(self) -> int:
        return self.money
    
    def __str__(self) -> str:
        return f"""
    nom: {self.__name__()}
    argent: {self.__money__()}"""