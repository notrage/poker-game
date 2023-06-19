from utils.enumerations.card_value import CardValue 
from utils.enumerations.card_color import CardColor
from utils.enumerations.community_stage import CommunityStage
from utils.card import Card
from utils.card_pack import CardPack
from utils.community import Community
from utils.hand import Hand
from utils.player import Player

class Game:
    
    def __init__(self) -> None:
        
        self.card_pack: CardPack = None
        self.community: Community = None
        self.community_stage: CommunityStage = None
        self.players: list[Player] = None
        self.hands: dict = None
        self.bets: dict = None
        
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
        
        # put the right format for every Game's attribute
        card_pack = self.__card_pack__().__str__() if self.__card_pack__() else None
        community = self.__community__().__str__() if self.__community__() else None
        community_stage = self.__community_stage__().__str__() if self.__community_stage__() else None
        players = [player.__name__() for player in self.__players__()] if self.__players__() else None
        hands = {player.__name__(): hand.__str__() for (player, hand) in self.__hands__().items()} if self.__hands__() else None
        bets = {player.__name__(): value for (player, value) in self.__bets__().items()} if self.__bets__() else None
        
        return f"""
    paquet de cartes: {card_pack}
    cartes communes: {community}
    étape dans le round: {community_stage}
    joueurs: {players}
    mains: {hands}
    mises: {bets}"""
        
    def init_card_pack(self) -> None:
        """generate the Game's card_pack
        """
        
        self.card_pack: CardPack = CardPack()
        
    def init_community(self) -> None:
        """generate the Game's community
        """
        
        assert self.__card_pack__(), "Error, cannot generate the Game's community if the Game's card_pack isn't initialized"
        
        # get the cards for the community
        community_cards = self.__card_pack__().get_and_remove_random_cards(8)
        
        self.community = Community(community_cards)
        
    def init_community_stage(self) -> None:
        """initialize/reset Game's community_stage
        """

        self.community_stage = CommunityStage.EMPTY
        
    def update_community_stage(self) -> None:
        """upgrade the current Game's community_stage
        """
        
        self.community_stage: CommunityStage = self.__community_stage__().next_community_stage()
        
    def add_player(self, a_game_player: Player) -> None:
        """add a player to the Game

        Args:
            a_game_player (Player): a player to join the Game
        """
        
        # check if a player is already in the game
        if self.__players__() == None:
            self.players = [a_game_player]
        else:
            assert len(self.__players__()) < 10, "Error: cannot have more than 10 players in a Game"
            self.players.append(a_game_player)
    
    def generate_hands(self) -> None:
        """generate randoms hands for all Game's players
        """

        assert self.__card_pack__(), "Error, cannot generate the Game's hands if the Game's card_pack isn't initialized"
        
        # Initialize player and hand list
        player_list = self.__players__()
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
        self.init_community()
        self.init_community_stage()
        self.init_card_pack()

    def highest_combination(self, player: Player):
        """give the highest player cards combination he can make

        Args:
            player (Player): a Game's player
        """
        
        #TODO
        return
    
    def best_hand(self) -> list[Hand]:
        """give the best(s) Game's hand(s)

        Returns:
            list[Hand]: the best(s) Game's hand(s)
        """
        
        #TODO
        return