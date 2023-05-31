from utils.player import Player

class Bet:
    
    def __init__(self, bet_player: Player, bet_value: int) -> None:
        
        self.player: Player = bet_player
        
        if bet_value > self.player.__money__():
            print("Error: cannot create a bet with higher amount of money that player's has")
            exit()
            
        self.value: int = bet_value
    
    def __player__(self) -> Player:
        return self.player
    
    def __value__(self) -> int:
        return self.value
    
    def __str__(self) -> str:
        return f"""
            joueur: {self.__player__().__name__()}
            mise: {self.__value__()}"""