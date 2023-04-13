from enumerations import CardValue as CV, CardColor as CC
from card import Card

if __name__ == "__main__":
    
    a_card: Card = Card(card_value=CV.TEN, card_color=CC.CLUB)
    pack_of_card = Card.card_list_gen()
    print(type(pack_of_card[0].get_value()))