# main.py

from deck import Deck
from hand import Hand
from chips import Chips
from bet import take_bet
from display_cards import show_some, show_all
from hit import hit, hit_or_stand
from win_cons import player_busts, player_wins, dealer_busts, dealer_wins, push

# Set Up Player Chips (Persistent Chip Count)
player_chips = Chips()

def main():
    while True:
        print("\nWelcome to BlackJack!")

        # Create and Shuffle Deck
        deck = Deck()
        deck.shuffle()

        # Set Up Player Hand
        player_hand = Hand()
        player_hand.add_card(deck.deal())   # Deal 1st Player Card
        player_hand.add_card(deck.deal())   # Deal 2nd Player Card
        
        # Set Up Dealer Hand
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())   # Deal 1st Dealer Card
        dealer_hand.add_card(deck.deal())   # Deal 2nd Dealer Card

        # Prompt Player for Bet
        take_bet(player_chips)

        # Show Cards (Hide Dealer's 1st Card)
        show_some(player_hand, dealer_hand)

        playing = True
        while playing:
            # Prompt Player to Hit or Stand
            playing = hit_or_stand(deck, player_hand)

            # Show Cards (Hide Dealer's 1st Card)
            show_some(player_hand, dealer_hand)

            # If Player's Hand Value > 21, Player Busts!
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break
        
        # If Player Hand Value <= 21, Play Dealer Hand Until Dealer Hand Value = ~17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            
            # Show All Cards
            show_all(player_hand, dealer_hand)

            # Run Different Winning Scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        # Show Player's Chip Total
        print(f"\nPlayer's Total Chips: {player_chips.total}")

        # Ask to Play Again
        new_game = input("\nPlay Again? 'Y' or 'N': ")

        if new_game[0].upper() == 'Y':
            playing = True
        else:
            print("\nThank you for playing!")
            break

if __name__ == "__main__":
    main()
