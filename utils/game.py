from utils.enumerations.card_value  import CardValue 
from utils.enumerations.card_color import CardColor
from utils.enumerations.community_stage import CommunityStage
from utils.enumerations.poker_hand import PokerHand
from utils.card import Card
from utils.card_pack import CardPack
from utils.community import Community
from utils.combination import Combination
from utils.hand import Hand
from utils.player import Player

class Game:
    
    def __init__(self) -> None:
        
        self.card_pack: CardPack             = None
        self.community: Community            = None
        self.community_stage: CommunityStage = None
        self.players: list[Player]           = None
        self.hands: dict                     = None
        self.bets: dict                      = None
        
    def __card_pack__(self) -> CardPack:
        
        return self.card_pack
    
    def __community__(self) -> Community:
        
        return self.community
    
    def __community_stage__(self) -> CommunityStage:
        
        return self.community_stage
    
    def __players__(self) -> list[Player]:
        
        return self.players
    
    def __hands__(self) -> dict:
        
        return self.hands
    
    def __bets__(self) -> dict:
        
        return self.bets
    
    def __str__(self) -> str:
        # Put the right format for every Game's attribute
        card_pack_to_str: list[str] = self.__card_pack__().__str__() if self.__card_pack__() else None
        community_to_str: str       = self.__community__().__str__() if self.__community__() else None
        community_stage_to_str: str = self.__community_stage__().__str__() if self.__community_stage__() else None
        players_to_str: list[str]   = [player.__name__() for player in self.__players__()] if self.__players__() else None
        hands_to_str: dict          = {player.__name__(): hand.__str__() for (player, hand) in self.__hands__().items()} if self.__hands__() else None
        bets_to_str: dict           = {player.__name__(): value for (player, value) in self.__bets__().items()} if self.__bets__() else None
        
        return f"Game's card pack: {card_pack_to_str}\nGame's community cards: {community_to_str}\nGame's community stage: {community_stage_to_str}\nGame's players: {players_to_str}\nGame's player's hands: {hands_to_str}\nGame's player's bets: {bets_to_str}\n"
        
    def init_card_pack(self) -> None:
        """generate the Game's card_pack
        """
        
        self.card_pack = CardPack()
        
    def init_community(self) -> None:
        """generate the Game's community
        """
        
        assert self.__card_pack__(), "Error, cannot generate the Game's community if the Game's card_pack isn't initialized"
        # Get the cards for the community
        community_cards: list[Card] = self.__card_pack__().get_and_remove_random_cards(8)
        
        self.community = Community(community_cards)
        
    def init_community_stage(self) -> None:
        """initialize/reset Game's community_stage
        """

        self.community_stage = CommunityStage.EMPTY
        
    def update_community_stage(self) -> None:
        """upgrade the current Game's community_stage
        """
        
        self.community_stage = self.__community_stage__().next_community_stage()
        
    def add_player(self, a_game_player: Player) -> None:
        """add a player to the Game

        Args:
            a_game_player (Player): a player to join the Game
        """
        # check if a player is already in the game
        if not self.__players__():
            self.players = [a_game_player]
        else:
            assert len(self.__players__()) < 10, "Error: cannot have more than 10 players in a Game"
            self.players.append(a_game_player)
    
    def generate_hands(self) -> None:
        """generate randoms hands for all Game's players
        """

        assert self.__card_pack__(), "Error, cannot generate the Game's hands if the Game's card_pack isn't initialized"
        # Initialize player and hand list
        player_list: list[Player] = self.__players__()
        hand_list: list[Hand] = [Hand(self.__card_pack__().get_and_remove_random_cards(2)) for i in range (len(player_list))]
        
        self.hands = {player: hand for (player, hand) in zip(player_list, hand_list)}
        
    def add_bet(self, bet_player: Player, bet_amount: int) -> None:
        """initialize bets for a given Game's players
        """
        
        assert bet_amount <= bet_player.__money__(), "Error, cannot bet a higher value than the player's money"
        
        # Check if the bets dictionnary is already initialized
        if not self.__bets__():
            self.bets = {player: None for player in self.__players__()}
            
        self.bets[bet_player] = bet_amount
        
    def round_win(self, player_win_list: list[Player]) -> None:
        """update players's money amount after a round

        Args:
            player_win_list (list[Player]): list of winning players
        """
        
        money_win: int = sum(self.__bets__().values()) / len(player_win_list)

        for player in self.__players__():
            
            player.sub_money(self.__bets__()[player])
            if player.__money__() <= 0:
                
                print(f"The player {player.__name__()} is out, his amount of money has decreased to 0")
                self.players.remove(player)
            
        for player in player_win_list:
            
            player.add_money(money_win)
        
        self.hands = None
        self.bets = None
        self.init_card_pack()
        self.init_community()
        self.init_community_stage()

    def __player_combination__(self, player: Player) -> Combination:
        """give Game's player's card combination

        Args:
            player (Player): a Game's player

        Returns:
            _type_: Game's player's card combination
        """
        
        assert self.__hands__(), "Error, cannot get Game's player's combination if hands isn't initialized"
        # Get current's community cards
        current_community_cards: list[Card] = self.__community__().get_stage_commnunity_cards(self.__community_stage__())
        
        return Combination(self.__hands__()[player], current_community_cards)

    def __highest_combination__(self, player: Player):
        """give the highest player cards combination he can make

        Args:
            player (Player): a Game's player
        """
        
        #TODO
        return
    
    def __best_hand__(self) -> list[Hand]:
        """give the best(s) Game's hand(s)

        Returns:
            list[Hand]: the best(s) Game's hand(s)
        """
        
        #TODO
        return