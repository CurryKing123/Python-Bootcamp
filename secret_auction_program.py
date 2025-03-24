print("Welcome to the secret auction program")

more_bidders = True
bidder_list = {}
winner = ""

def add_bidder():
    global more_bidders

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    bidder_list[name] = bid
    if other_bidders == "no":
        more_bidders = False
        winner_calc()


def winner_calc():
    global winner
    winning_bid = 0

    for bidder in bidder_list:
        bid = bidder_list[bidder]
        if bid > winning_bid:
            winning_bid = bid
            winner = bidder
    print(f"The winner is {winner} with a bid of {bidder_list[winner]}")





while more_bidders == True:
    add_bidder()