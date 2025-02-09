logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bids = {}
print(logo)
print("Welcome to Silent Bidding!")
bidding_in_progress = True

while bidding_in_progress:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bids[name] = bid

    new_bidder_response = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if new_bidder_response == "no":
        bidding_in_progress = False
    print("\n" * 50)

highest_bid = 0
biggest_bidder_name = ""
for person in bids:
    highest_bid = max(bids[person], highest_bid)
    if highest_bid == bids[person]:
        biggest_bidder_name = person

print(f"The winner is {biggest_bidder_name} with a bid of ${highest_bid}.")
