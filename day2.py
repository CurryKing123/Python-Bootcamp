print("Welcome to the tip calculator!")
total = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? ")) / 100
split = int(input("How many people to split the bill? "))

pay = round(((float(total) + float(tip)) / split), 2)

print(f"Each person should pay: ${pay}")