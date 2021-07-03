from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bids = {}
is_finished = False


def highest_bidder(record):
  highest_bid = 0
  winner = ""
  for bidder in record:
    bid_amount = record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while not is_finished:
  name = input("What is your name? ")
  price = int(input("What is your bid? $"))
  bids[name] = price
  answer = input("Are there any other bidders? Type 'yes' or 'no'\n")
  if answer == "yes":
    is_finished = False
    clear()

  elif answer == "no":
    is_finished = True
    highest_bidder(bids)



