from utils.enumerations.card_value import CardValue
from utils.enumerations.card_color import CardColor
from utils.card import Card
from utils.card_pack import CardPack
from utils.community import Community
from utils.hand import Hand
from utils.player import Player
from utils.game import Game

if __name__ == "__main__":
    
    partie = Game()
    
    partie.init_card_pack()
    partie.init_community()
    
    joueur1 = Player("roger", 10000)
    joueur2 = Player("jacques", 7000)
    
    partie.add_player(joueur1)
    partie.add_player(joueur2)
    
    partie.generate_hands()
    
    partie.add_bet(joueur1, 1000) 
    partie.add_bet(joueur2, 500)
    partie.add_bet(joueur1, 800)
    
    print(partie.__str__())