# bet.py

from chips import Chips
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("\nHow many chips to bet? "))
        except ValueError:
            print("\nSorry, please enter a valid bet number.")
        else:
            if chips.bet > chips.total:
                print(f"\nSorry, you dont have enough chips to bet. You have {chips.total} available.")
            else:
                break
