print("Welcome to the tip calculator!")
try:
    total_bill = float(input("What was the total bill? "))
    tip = int(input("How much tip would you like to give (%)? 10, 12, or 15? "))

    if tip not in [10, 12, 15]:
        print("Invalid tip amount.")
        tip = int(input("How much tip would you like to give (%)? 10, 12, or 15? "))

    people = int(input("How many people will split the bill? "))
except ValueError:
    raise ValueError("Please input valid amounts!")

total_bill +=  total_bill * (tip / 100)
split_amount = total_bill / people

print(f"Each person should pay: {round(split_amount, 2)}")