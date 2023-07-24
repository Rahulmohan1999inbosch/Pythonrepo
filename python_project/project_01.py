###Slot machine##########
MAX_LINES=3  #This is a constant
MAX_BET=100
MIN_BET=1
def deposit():
    while True:
        amount=input("What would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
              break
            else:
              print("enter amount greater than 0")
        else:
           print("enter a valid amount")
    return amount

def lines():
    while True:
      line=input(f"Enter the number of line you want to bet on between the range (1-{MAX_LINES})? :-")
      if line.isdigit():
         line=int(line)
         if 1 <= line <= 3:
            break
         else:
            print("enter the content with in the range")
      else:
         print("Enter number only")
    return line

def get_bets():
   while True:
      bet=input(f"The the amount of bet between the range( {MIN_BET}--{MAX_BET}")
      if bet.isdigit():
         bet=int(bet)
         if MIN_BET <= bet <=MAX_BET:
            break
         else:
            print("enter the amount with in the range ")
      else:
         print("enter a valid range")
      return bet
  
    
def main():
   balance=deposit()
   line=lines()
   bet=get_bets()
   Total_amount=bet*line
   print ("fThe amount of bet invested is {Total_bets}")
   

main()



