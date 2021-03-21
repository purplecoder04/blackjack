import random 
from replit import clear
from art import logo
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(hand):
  if sum(hand) == 21 and len(hand) == 2:
    return 0
  if 11 in hand and sum(hand) > 21:
    hand.remove(11)
    hand.append(1)
    return sum(hand)
  else:
    return sum(hand)
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# want_to_play = input("Do you want to play a game of Blackjack?\n type 'y' or 'n':" )
# print(want_to_play)
def compare(player1, player2):
  if player1 > 21 and player2 > 21:
    return"you went over you lose"

  if player1 == player2:
    return "It's a Draw"
  elif player2 == 0:
    return "You lost"
  elif player1 == 0 :
    return " You won" 
  elif player1 > 21:
    return 'you lose'
  elif player2 > 21:
    return "you won"
  elif player1> player2:
    return "You Win"
  else:
    return "you lose bro"

def play_game():
  print(logo)
  player=[]
  computer=[]
  is_game_over = False
  for _ in range(2):
    player.append(deal_card())
    computer.append(deal_card())
  while not is_game_over:
    player_score = calculate_score(player)
    computer_score = calculate_score(computer)
    print(f"Your cards are :{player}, current score: {player_score}")
    print(f"computer first card :{computer[0]}")
    if player_score == 0 or  computer_score== 0 or player_score > 21:
      is_game_over = True
    else:
      another_card= input("Type 'y to get another card, Type 'n to pass: ").lower()
      if another_card == "y":
        player.append(deal_card())
      else:
        is_game_over = True 
      
  while computer_score != 0 and computer_score < 17:
    computer.append(deal_card())
    computer_score = calculate_score(computer)
  print(f" Your final hand: {player}, final score: {player_score}")
  print(f" Computer final hand: {computer}, final score: {computer_score}")

  print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
  clear()
  play_game()