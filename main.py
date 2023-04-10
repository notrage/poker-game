from enumerations import CardValue as CV, CardColor as CC
from card import Card

if __name__ == "__main__":
    
    a_card: Card = Card(card_value=CV.TEN, card_color=CC.CLUB)
    print(a_card.to_string())