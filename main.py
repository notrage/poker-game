from utils.game import Game
from utils.player import Player

from utils.hand import Hand
from utils.combination import Combination
from utils.card import Card as C
from utils.enumerations.card_color import CardColor as CC
from utils.enumerations.card_value import CardValue as CV
from utils.enumerations.poker_hand import PokerHand as PH

if __name__ == "__main__":
    
    debug = True
    
    while debug:
        partie = Game()
        
        partie.init_card_pack()
        partie.init_community()
        partie.init_community_stage()
        
        joueur1 = Player("roger", 10000)
        joueur2 = Player("jacques", 7000)
        joueur3 = Player("michel", 9000)
        
        partie.add_player(joueur1)
        partie.add_player(joueur2)
        partie.add_player(joueur3)
        
        partie.generate_hands()
        
        partie.add_bet(joueur1, 800)
        partie.add_bet(joueur2, 500)
        partie.add_bet(joueur3, 900)
        
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
        meilleur_combinaison_liste: list[Combination] = partie.__best_combination__()
        print("\n", [combinaison.__str__() for combinaison in meilleur_combinaison_liste], "\n")
        print([combinaison.__poker_hand__().__str__() for combinaison in meilleur_combinaison_liste])
        
        if meilleur_combinaison_liste[0].__poker_hand__() == PH.STRAIGHT_FLUSH: debug = False