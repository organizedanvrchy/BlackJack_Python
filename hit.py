# hit.py

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    while True:
        x = input("\nHit or Stand? Enter 'H' or 'S': ")

        if x[0].upper() == 'H':
            hit(deck, hand)
            return True
        elif x[0].upper() == 'S':
            print("\nPlayer Stands. Dealer's Turn.")
            return False
        else:
            print("\nSorry, please enter 'H' or 'S' only.")
