# win_cons.py

def player_busts(player, dealer, chips):
    print("Player BUSTS!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer BUSTS!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer WINS!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and Player Tie! PUSH!")
