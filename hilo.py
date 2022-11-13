import random

class Card:
  #initializes the instance of a class with a value for a card, and the used values to make sure it goes through all 13 before resetting
  def __init__(self):
    self.value = 0
    self.used = []

  #selects a random number 1-13 and if it hasn't been used sets that as the value or reruns to get a value that hasn't been used. It will also reset once all 13 cards have been drawn
  def getCard(self):
    num = random.randint(1, 13)

    if len(self.used) >= 13:
        self.used = [num]
        self.value = num
    elif num in self.used:
      self.getCard()
    else:
      self.value = num
      self.used.append(num)
        
      return self.value

class Game:
  #initializes the instance of the game. It keeps track of user points, the current card, and the next card.
  def __init__(self):
    self.points = 0
    self.current = 0
    self.next = 0

  #starts the game, starting user at correct points and setting the current card value
  def startGame(self, card):
    card.getCard()

    self.points = 300
    self.current = card.value

  #the takeTurn function will be used to calculate the next turn. It updates next value, then checks if the use correctly guessed higher or lower. If the user has more than 0 points, it will update the current and next values, then allow another turn
  def takeTurn(self, guess, card):
    card.getCard()

    print(guess, self.current, card.value, card.used)
    self.next = card.value
    if guess == 'higher':
      if self.current < self.next:
        self.points += 100
        self.current = card.value
      else:
        self.points -= 75
        self.current = card.value
    elif guess == 'lower':
      if self.current > self.next:
        self.points += 100
        self.current = card.value
      else:
        self.points -= 75
        self.current = card.value
    else:
      print('Not a valid input, try again.')

def main():
  game = Game()
  card = Card()

  print('Welcome to Hilo!')
  print('Your starting score is: 300')

  game.startGame(card)

  while(True):
    print(f'The current card is: {game.current}')
    guess = input('Will the next card be higher or lower?(higher/lower) ')

    game.takeTurn(guess, card)

    print(f'The next card was {game.next}')
    print(f'Your score is: {game.points}')

    if game.points <= 0:
      print('\nYou are out of points. Game Over!')
      break

    playAgain = input('Would you like to play again?(y/n): ')

    if playAgain == 'y':
      print('')
    else:
      print('Thanks for playing!')
      print(f'Your final score is: {game.points}')
      break



  # print(game, card)

if __name__ == '__main__':
  main()