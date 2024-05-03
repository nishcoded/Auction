def highest_bidder():
    highest_bid = 0
    winner = ""
    for name in all_bids:
        bid = all_bids[name]
        if bid > highest_bid:
            highest_bid = bid
            winner = name
    print(f"This auction's winner is {winner} with bid amount of ${highest_bid}")


bidding_on = True
all_bids = {}

while bidding_on:
    name = input("What is your name? ")
    bid = int(input("How much would you like to bid? $"))
    all_bids[name] = bid

    more_bidder = input("Are there any more bidders? Type Y/N: ").upper()
    
    if more_bidder == "N":
        bidding_on = False
        highest_bidder()
