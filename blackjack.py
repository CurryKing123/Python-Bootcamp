import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
all_cards = []
my_cards = []
e_cards = []
my_total = 0
e_total = 0

def new_deck():
    global all_cards
    all_cards = []
    for card in cards:
        add_cards = True
        count = 0
        while add_cards == True:
            all_cards.append(card)
            count += 1
            if count > 3:
                add_cards = False
    random.shuffle(all_cards)


def draw_card():
    global my_total
    global e_total

    my_card = all_cards[0]
    my_cards.append(my_card)
    del all_cards[0]

    if e_total < 17:
        e_card = all_cards[0]
        del all_cards[0]
    else:
        e_card = 0

    if my_card == 11 and my_card + my_total > 21:
        my_card == 1
    
    if e_card == 11 and e_card + e_total > 21:
        e_card == 1

    my_total = my_total + my_card
    e_total = e_total + e_card

    if my_total > 21:
        print(f"Your total is {my_total}, You Lose")
    else:
        card_prompt = input(f"Your current total is {my_total}, your opponent's current total is {e_total} would you like to draw another? ('y' or 'n'): ")
        if card_prompt == "y":
            draw_card()
        elif card_prompt == "n":
            if my_total > e_total:
                print("You Win")
            elif my_total == e_total:
                print("Tie")
            else:
                print("You Lose")


def new_game():
    new_deck()
    draw_card()
    
new_game()