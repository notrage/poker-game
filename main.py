from utils.game import Game
from utils.player import Player

from utils.hand import Hand
from utils.combination import Combination
from utils.card import Card as C
from utils.enumerations.card_color import CardColor as CC
from utils.enumerations.card_value import CardValue as CV

if __name__ == "__main__":
    
    found: bool = False
    
    while not found:
        
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
        
        combinaison1: Combination = partie.__player_combination__(joueur1)
        combinaison2: Combination = Combination(Hand([C(CV.THREE, CC.CLUB), C(CV.ACE, CC.CLUB)]), [C(CV.TWO, CC.CLUB), C(CV.FOUR, CC.CLUB), C(CV.FIVE, CC.CLUB), C(CV.ACE, CC.DIAMOND), C(CV.EIGHT, CC.CLUB)])
        
        cartes = combinaison2.__cards__()
        print(combinaison2.__str__())
        print(combinaison2.__is_straight_flush__())
        
        #print(combinaison1.__str__())
        #print(combinaison1.__group_by_value_str__())
        #print(combinaison1.__group_by_color_str__())
        
        #if combinaison1.__is_straight__(): 
        found = True
        #    print(combinaison1.__str__())
        #print(combinaison1.__is_straight__())