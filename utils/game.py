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
        
        # Put the right format for every Game's attribute
        card_pack_str = self.__card_pack__().__str__() if self.__card_pack__() != None else None
        community_str = self.__community__().__str__() if self.__community__() != None else None
        players_str = [player.__name__() for player in self.__players__()] if self.__players__() != None else []
        hands_str = {player.__name__(): hand.__str__() for (player, hand) in self.__hands__().items()} if self.__hands__() != None else None
        bets_str = "TODO" if self.__bets__() != None else None
        
        return f"""
    paquet de cartes: {card_pack_str}
    cartes communes: {community_str}
    joueurs: {players_str}
    mains: {hands_str}
    mises: {bets_str}"""
            
    def init_card_pack(self) -> None:
        """initialize/reset the game's card pack
        """
        self.card_pack: CardPack = CardPack(Card.card_list_gen())
        
    def init_community(self) -> None:
        """generate the game's community cards
        """
        
        # Get the cards for the community
        community_cards: Community = self.__card_pack__().get_and_remove_mulitple_random_cards(8)
        
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
        elif len(self.__players__()) < 10:
            self.players.append(a_game_player)
        else:
            print("Error: cannot have more than 10 players in a Game")
            exit()
    
    def generate_hands(self) -> None:
        """generate randoms hands for all Game's players
        """
        player_list: list[Player] = self.__players__()
        hand_list: list[Hand] = len(player_list) * [Hand(self.__card_pack__().get_and_remove_mulitple_random_cards(2))]
        
        self.hands: dict = {player: hand for (player, hand) in zip(player_list, hand_list)}
        
    def add_bet(self, bet_player_name) -> None:
        """initialize bets for all Game's players
        """
        #TODO
        self.bets: dict = {player: None for player in self.__players__()}
        