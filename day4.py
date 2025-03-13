import random

# randint = random.randint(1, 10)
# print(randint)

# randnum = random.random() * 10
# print(randnum)

# randfloat = random.uniform(1, 10)
# print(randfloat)

# rand_int = random.randint(1, 2)
# if rand_int == 1:
#     print("Heads")
# else:
#     print("Tails")

# people = ["Jo", "Mo", "Wulagard"]
# print(random.choice(people))

rpslist = ["rock", "paper", "scissors"]
rps = rpslist[int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors"))]
opponent = random.choice(rpslist)

if rps == "rock":
    if opponent == "rock":
        print(f"Opponent chose: {opponent}, it's a tie")
    elif opponent == "paper":
        print(f"Opponent chose: {opponent}, you lose")
    else:
        print(f"Opponent chose: {opponent}, you win")
if rps == "paper":
    if opponent == "rock":
        print(f"Opponent chose: {opponent}, you win")
    elif opponent == "paper":
        print(f"Opponent chose: {opponent}, it's a tie")
    else:
        print(f"Opponent chose: {opponent}, you lose")
if rps == "scissors":
    if opponent == "rock":
        print(f"Opponent chose: {opponent}, you lose")
    elif opponent == "paper":
        print(f"Opponent chose: {opponent}, you win")
    else:
        print(f"Opponent chose: {opponent}, it's a tie")