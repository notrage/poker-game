from utils.enumerations import CardValue as CV, CardColor as CC
from utils.card import Card
from utils.card_pack import CardPack
from utils.community import Community
from utils.hand import Hand
from utils.player import Player
from utils.bet import Bet

class Game:
    
    def __init__(self) -> None:
        
        self.card_pack: CardPack = None
        self.community: Community = None
        self.players: list[Player] = None
        self.hands: dict = None
        self.bets: dict = None
        
    def __card_pack__(self) -> CardPack:
        return self.card_pack
    
    def __community__(self) -> Community:
        return self.community
    
    def __players__(self) -> list[Player]:
        return self.players
    
    def __hands__(self) -> dict:
        return self.hands
    
    def __bets__(self) -> dict:
        return self.bets
    
    def __str__(self) -> str:
        return f"""
            paquet de cartes: {self.__card_pack__().__str__()}
            cartes communes: {self.__community__().__str__()}
            joueurs: {self.__players__().__str__()}
            mains: {self.__hands__()}
            mises: {self.__bets__()}"""
            
    def init_card_pack(self) -> None:
        """initialize/reset the game's card pack
        """
        self.card_pack = Card.card_list_gen()
        
    def init_community(self) -> None:
        """generate the game's community cards
        """
        
        # Get the cards for the community
        community_cards: list[Card] = self.card_pack.get_and_remove_mulitple_random_cards(8)
        
        # Generate the game's community
        self.community = Community(community_cards)
        
    def add_player(self, a_game_player: Player) -> None:
        """add a player to the game

        Args:
            a_game_player (Player): a player to join the game
        """
        
        # Check if a player is already in the game
        if self.__players__() == None:
            self.players = [a_game_player]
        else:
            self.players.append(a_game_player)
    
    def generate_hands(self) -> None:
        
        player_hands: dict = #TODO
        
        