from sys import argv
from utils.game import Game
from utils.player import Player

from utils.hand import Hand
from utils.combination import Combination
from utils.card import Card as C
from utils.enumerations.color import Color as CC
from utils.enumerations.value import Value as CV
from utils.enumerations.poker_hand_rank import PokerHandRank as PH

if __name__ == "__main__":
    
    partie = Game()
    
    print(argv)
    
    partie.init_card_pack()
    partie.init_community()
    partie.init_community_stage()
    
    joueur1 = Player("roger", 10000)
    joueur2 = Player("jacques", 7000)
    joueur3 = Player("michel", 9000)
    joueur4 = Player("jose", 9000)
    joueur5 = Player("patrick", 9000)
    joueur6 = Player("anabelle", 9000)
    
    partie.add_player(joueur1)
    partie.add_player(joueur2)
    partie.add_player(joueur3)
    partie.add_player(joueur4)
    partie.add_player(joueur5)
    partie.add_player(joueur6)
    
    partie.generate_hands()
    
    partie.add_bet(joueur1, 800)
    partie.add_bet(joueur2, 500)
    partie.add_bet(joueur3, 900)
    partie.add_bet(joueur4, 1300)
    partie.add_bet(joueur5, 200)
    partie.add_bet(joueur6, 800)
    
    #print(partie.__str__())
    
    partie.update_community_stage()
    
    partie.round_win([joueur1])
    
    #print(joueur1.__str__())
    #print(joueur2.__str__())
    #print(joueur3.__str__())
    
    #print(partie.__str__())
    partie.update_community_stage()
    partie.update_community_stage()
    partie.update_community_stage()
    
    #print(partie.__str__())
    
    partie.generate_hands()
    
    #combinaison1: Combination = partie.__player_combination__(joueur1)
    #print(combinaison1.__str__())
    #print(combinaison1.__group_by_value_str__())
    #print(combinaison1.__group_by_color_str__())
    #print(combinaison1.__poker_hand__().__str__())
    meilleur_combinaison_liste: list[Combination] = partie.best_combination()
    print("\n", [combinaison.__str__() for combinaison in meilleur_combinaison_liste], "\n")
    print([combinaison.poker_hand_rank().__str__() for combinaison in meilleur_combinaison_liste])