from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
auction_log = [
{
  "name": " ",
  "bid": 0,
},
]

#Nesting Dictionary in a List
def add_new_bidder(name, bid):
  new_bidder = {
    "name": name,
        "bid":   bid,
    }
  
  auction_log.append(new_bidder)

auction_contiues_answer = int(input("Would you like to add a bidder?, Type 1 for yes or 0 for no "))
if auction_contiues_answer == 1:
  auction_contiues = True
  while auction_contiues:
    name = input("What's your full name ")
    bid = input("What's your Bid? ")
    add_new_bidder(name, bid)
    auction_contiues = int(input("Would you like to add a bidder?, Type 1 for yes or 0 for no "))
    
    

# Initialize max_bid to a starting value
max_bid = 0
# Initialize highest_bidder to None (no bidder with the highest bid yet)
highest_bidder = None

# Use a loop to iterate over each bidder in auction_log

for bidder in auction_log:
  # Access the bidder's bid using bidder["bid"]
  current_bid = int(bidder["bid"])
  # Check if the current bid is higher than the maximum bid
  if current_bid > max_bid:
    # Update the maximum bid
    max_bid = current_bid
    # Update the highest bidder's information
    highest_bidder = bidder
    
# Print the information of the highest bidder after the loop    
print(f"Congratulations your the Winner: {highest_bidder}" )
