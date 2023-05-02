from utils.enumerations import CardValue as CV, CardColor as CC
from utils.card import Card
from utils.card_pack import CardPack
from utils.community import Community

if __name__ == "__main__":
    
    a_card: Card = Card(card_value=CV.TEN, card_color=CC.CLUB)
    a_card_pack = CardPack(card_pack_card_list=Card.card_list_gen())
    a_community = Community(a_card_pack.get_and_remove_mulitple_random_cards(8))
    print([card.__str__() for card in a_community.get_phase_comminity(3)])
