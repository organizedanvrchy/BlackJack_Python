# display_cards.py

from hand import Hand

def show_some(player, dealer):
    print("\nDealer's Hand: ")
    print("<card hidden>")      # Hide First Card
    print(dealer.cards[1])      # Show Second Card

    print(f"Dealer's Hand = {dealer.value}")

    
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)

    print(f"Player's Hand = {player.value}")

def show_all(player, dealer):
    print("\nDealer's Hand:")
    for card in dealer.cards:
        print(card)

    print(f"Dealer's Hand = {dealer.value}")

    print("\nPlayer's Hand:")
    for card in player.cards:
        print(card)

    print(f"Player's Hand = {player.value}")
