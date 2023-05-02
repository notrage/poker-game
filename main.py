from enumerations import CardValue as CV, CardColor as CC
from card import Card
from card_pack import CardPack

if __name__ == "__main__":
    
    a_card: Card = Card(card_value=CV.TEN, card_color=CC.CLUB)
    a_card_pack = CardPack(card_pack_card_list=Card.card_list_gen())
    