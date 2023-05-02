from utils.enumerations import CardValue as CV, CardColor as CC
from utils.card import Card
from utils.card_pack import CardPack
from utils.community import Community
from utils.hand import Hand

if __name__ == "__main__":
    
    paquet_de_carte: CardPack = CardPack(Card.card_list_gen())
    
    cartes_communes: Community = Community(paquet_de_carte.get_and_remove_mulitple_random_cards(8))
    
    main1: Hand = Hand(paquet_de_carte.get_and_remove_mulitple_random_cards(2))
    main2: Hand = Hand(paquet_de_carte.get_and_remove_mulitple_random_cards(2))
    main3: Hand = Hand(paquet_de_carte.get_and_remove_mulitple_random_cards(2))
    main4: Hand = Hand(paquet_de_carte.get_and_remove_mulitple_random_cards(2))
    
    print(f"le paquet de carte contient {len(paquet_de_carte.__card_list__())} cartes")
    print(f"le paquet de carte contient les cartes suivantes:\n{paquet_de_carte.__str__()}\n")

    print(f"Les cartes ouvertes sont: {cartes_communes.__str__()}\n")
    
    print(f"La main1 est composé des cartes: {main1.__str__()}")
    print(f"La main2 est composé des cartes: {main2.__str__()}")
    print(f"La main3 est composé des cartes: {main3.__str__()}")
    print(f"La main4 est composé des cartes: {main4.__str__()}")