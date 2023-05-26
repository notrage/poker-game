from utils.enumerations import CardValue as CV, CardColor as CC
from utils.card import Card
from utils.card_pack import CardPack
from utils.community import Community
from utils.hand import Hand
from utils.player import Player
from utils.bet import Bet

if __name__ == "__main__":
    
    paquet_de_carte: CardPack = CardPack(Card.card_list_gen())
    
    cartes_communes: Community = Community(paquet_de_carte.get_and_remove_mulitple_random_cards(8))
    
    main1: Hand = Hand(paquet_de_carte.get_and_remove_mulitple_random_cards(2))
    main2: Hand = Hand(paquet_de_carte.get_and_remove_mulitple_random_cards(2))
    main3: Hand = Hand(paquet_de_carte.get_and_remove_mulitple_random_cards(2))
    main4: Hand = Hand(paquet_de_carte.get_and_remove_mulitple_random_cards(2))
    
    joueur1: Player = Player("Maurice", 2000, main1)
    
    mise1: Bet = Bet(joueur1, 1000)
    
    print(f"le paquet de carte contient {len(paquet_de_carte.__card_list__())} cartes")
    print(f"le paquet de carte contient les cartes suivantes:\n{paquet_de_carte.__str__()}\n")

    print(f"Le flop est composé des cartes : {cartes_communes.__str__()}\n")
    
    print(f"La main1 est composé des cartes: {main1.__str__()}")
    print(f"La main2 est composé des cartes: {main2.__str__()}")
    print(f"La main3 est composé des cartes: {main3.__str__()}")
    print(f"La main4 est composé des cartes: {main4.__str__()}\n")
    
    print(f"Le joueur1 a les caractéristiques suivantes: {joueur1.__str__()}\n")
    
    print(f"La mise1 a les caractéristique suivantes: {mise1.__str__()}\n")