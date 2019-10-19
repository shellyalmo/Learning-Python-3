"""This program is my first project and simulates games of chance. Since this section in Codecademy is based on lessons of syntax, functions and control flow, the program doesn't include loops. Also, the editor in Codecademy doesn't allow using input(), therefore all the input is provided manually."""
#Every game of chance involves generating a random parameter.
import random

#The total amount to begin with.
money = 100

#This function simulates flipping a coin and calling either "Heads" or "Tails".
def coin_flipping(bet,guess):
  print("This is a flipping coin game. You need to guess Heads or Tails and mention the amount of money you're betting on. ")
  print ("Your bet is: " + str(bet))
  print ("Your guess is: " + str(guess))
  OPTIONS = ("Heads", "Tails")
  option = random.choice(OPTIONS)
  correct = option
  if guess == correct:
    print ("Congrats! The result is " + correct +"! " + "You just won " + str(bet) + " dollars!")
    return bet
  elif guess != correct:
    print("Sorry! The result is " + correct + ". You just lost " + str(bet) + " dollars.")
    return (bet * -1)

#This function simulates playing the Japanese game Cho-Han, of rolling two dice and adding the results together. The player predicts whether the sum of those dice is odd or even and wins if their prediction is correct.
def Cho_Han (bet,guess):
  print ("")
  print ("This is a Cho-Han game. You need to guess if the sum of the two dice is Even or Odd, and mention the amount of money you're betting on.")
  print ("Your bet is: " + str(bet))
  print ("Your guess is: " + str(guess))
  DICE = (1,2,3,4,5,6)
  dice_1 = random.choice(DICE)
  dice_2 = random.choice(DICE)
  print ("dice 1 is: " + str(dice_1))
  print ("dice 2 is: " + str(dice_2))
  SUM = dice_1 + dice_2
  print ("The sum is: " +str(SUM))
  
  #This 'if' statement determines if the number is even or odd.
  if SUM%2 == 0:
    correct = "even"
  elif SUM%2 != 0:
    correct = "odd"
  
  #This 'if' statement determines if the player wins or loses.
  if guess == correct:
    print ("Congrats! The result is " + correct +"! " + "You just won " + str(bet) + " dollars!")
    return bet
  elif guess != correct:
    print("Sorry! The result is " + correct + ". You just lost " + str(bet) + " dollars.")
    return (bet * -1) 

#This function simulates two players picking a card randomly from a deck of cards. The higher number wins.
def random_card(bet_player_1,bet_player_2):
  print ("")
  print ("This two-player card game is simple: the player that draws the bigger number from the deck wins. Each player needs to bet an amount of money.")
  print ("Player 1 bet: " + str(bet_player_1))
  print ("Player 2 bet: " + str(bet_player_2))
  deck_value = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
  card_1_value = random.choice(deck_value)
  card_2_value = random.choice(deck_value)
  deck_suit = ("Clubs", "Diamonds", "Hearts", "Spades")
  card_1_suit = random.choice(deck_suit)
  card_2_suit = random.choice(deck_suit)
  
  #Making sure that a card that has been drawn by player 1 is removed from the deck.
  while card_1_value == card_2_value and card_1_suit == card_2_suit:
    card_2_value = random.choice(deck_value)
    card_2_suit = random.choice(deck_suit)
  print ("Card 1 is: " + str(card_1_value) + " " + card_1_suit)
  print ("Card 2 is: " + str(card_2_value) + " " + card_2_suit)
  if card_1_value > card_2_value:
    print ("Player 1 won " + str(bet_player_1) + " dollars!")
    return bet_player_1
  elif card_2_value > card_1_value:
    print ("Player 1 lost " + str(bet_player_1) + " dollars!")
    return bet_player_1 * -1
  elif card_1_value == card_2_value:
    print ("It's a tie!")
    return 0
    
#This function simulates some rules of American roulette game. A random number is generated and determines which space the ball lands on.
def roulette(bet,guess):
  print ("")
  print ("This game is like roulette. Each player places a bet on the ball landing on an even or odd place, or the ball landing on a specific place. Also mention the amount of money you're betting on.")
  print ("The amount you bet is: " + str(bet) + " dollars.")
  print ("Your guess is: " + str(guess))
  print ("The ball landed on:")
  E_or_O = ""
  
  #The pockets of the roulette wheel are numbered from 0 to 36.
  #In number ranges from 1 to 10 and 19 to 28, odd numbers are red and even are black. In ranges from 11 to 18 and 29 to 36, odd numbers are black and even are red.
  #The green pockets are numbered 0 and 00.
  #In this program, the number -1 represents 00
  roulette_number = random.randint(-1,36)
  if (roulette_number >= 1 and roulette_number <= 10 ) or (roulette_number >= 19 and roulette_number <= 28):
    if roulette_number%2 == 0:
      E_or_O = "even"
      print ("Even number")
      print ("The color: black")
    elif roulette_number%2 != 0:
      E_or_O = "odd"
      print ("Odd number")
      print ("The color: red")
  if (roulette_number >= 11 and roulette_number <= 18) or (roulette_number >= 29 and roulette_number <= 36):
    if roulette_number%2 == 0:
      E_or_O = "even"
      print ("Even number")
      print ("The color: red")
    elif roulette_number%2 != 0:
      E_or_O = "even"
      print ("Odd number")
      print ("The color: black")
  if roulette_number == 0 and roulette_number == -1:
    print ("House - either the number 0 or 00")
    print ("Sorry, the ball landed on the pocket of the house. You just lost: " + str(bet) + " dollars.")
    print ("The color: green")
    return (bet * -1)
  else:
    print ("The number is: " + str(roulette_number))

  if guess == E_or_O:
    print ("Your guess is correct! You just won " + str(bet) + " dollars!")
    return bet
    
  #Guessing the specific number rewards the player 35 times the amount they bet.
  if guess == roulette_number:
    print ("Wow! Your guess is 100% correct! You just won " + str(bet*35) + " dollars!")
    return (bet*35)
  else: 
    print ("Sorry, you lost " + str(bet) + " dollars.")
    return (bet * -1)
    

print ("Welcome to games of chance! The amount of money you're starting with is " + str(money) + 
" dollars.")
print ("")
#Calling the functions and updating the amount of money.
money += coin_flipping(1,"Tails")
print ("The amount of money you have now is: " + str(money) + " dollars.")
money += Cho_Han(3,"even")
print ("The amount of money you have now is: " + str(money) + " dollars.")
money += random_card(1,2)
print ("The amount of money you have now is: " + str(money) + " dollars.")
money += roulette(1,24)
print ("The amount of money you have now is: " + str(money) + " dollars.")



