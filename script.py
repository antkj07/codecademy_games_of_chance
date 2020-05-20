import random

my_money = 100

#Write your game of chance functions here    
def coin_flip(guess, bet):
  print("Coin Flip:")
  if bet <= 0:
    print("You must place a bet to play!")
    return 0
  if guess == "Heads" or "heads" or "Heads!":
    guess = 1
    print("Your guess: Heads")
  elif guess == "tails":
    guess = 2
    print("Your guess: Tails")
  else:
    print("You must place a guess to play!")
    return 0 

  num = random.randint(1, 2)
  if num == 1:
    print("Result: Heads")
  else:
    print("Result: Tails")  
  if num == guess:
    print("Congrats! You won $" + str(bet))
    return bet
  else:
    print("Better luck next time! You lost $" + str(bet))
    return -bet


def cho_han(guess, bet):
  print("\nCho-Han:")
  if bet <= 0:
    print("You must place a bet to play!")
    return 0

  num = random.randint(1,6) + random.randint(1,6)
  print("You've guessed: " + guess)
  if num % 2 == 0:
    num = "Even"
    print("Result: Even")
  else:
    num = "Odd" 
    print("Result: Odd")
  if num == guess:
    print("Congrats! You won $" + str(bet))
    return bet
  else:
    print("Better luck next time! You lost $" + str(bet))
    return -bet


def high_card(bet):
  player_1 = random.randint(1,13)
  player_2 = random.randint(1,13)

  print("\nWar: \nYour Card: " + str(player_1) + " \nOpponent: " + str(player_2))

  if player_1 > player_2:
    print("Congrats! You won $" + str(bet))
    return bet
  elif player_2 > player_1:
    print("Better luck next time! You lost $" + str(bet))
    return -bet
  else: 
    print("It was a tie! Your wager has been returned")
    return 0


def roulette(guess, bet):
  number = random.randint(0,37)
  print("\nRoulette: \nThe wheel is spinning....")
  print("You've placed: " + str(guess))
  if number == 37:
    print("The number is: 00")
  else: 
    print("The number is: " + str(number))
  if number == guess:
    print("Congrats! You won $" + str(bet*35))
    return bet * 35
  else:
    print("Better luck next time! You lost $" + str(bet))
    return -bet
  


#Call your game of chance functions here
my_money += coin_flip("Heads", 10)
my_money += cho_han("Even", 10)
my_money += high_card(10)
my_money += roulette(17, 20)
print(my_money)
