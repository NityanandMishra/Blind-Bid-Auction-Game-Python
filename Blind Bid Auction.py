from art import logo
print(logo)

def find_highest_bidder(bid_recorder):
    highest_bid = 0
    winner = ""
    for bidder in bid_recorder:
        bid_amount = bid_recorder[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Your Highest bid winner is {winner} with a bid of ${price}")
bids = {}
continue_bid = True
while continue_bid:
    name = input("Enter your Name: ")
    price = int(input("Enter your bid price $ : "))
    bids[name] = price
    should_continue = input("Do you want to continue ? Type 'yes' or 'no' \n").lower()
    if should_continue == 'no':
        continue_bid = False
        find_highest_bidder(bids)
        print("\n"* 20)
        
