import os
import random
from time import sleep

#hey guys! thanks for playing, and if you enjoyed, consider subscribing to my youtube:
# https://www.youtube.com/@squair./
# https://www.youtube.com/@Glixedyoutube/

#database
a = '☐'
b = '☐'
c = '☐'
d = '☐'
e = '☐'
store = 0
lead00 = "Glixed"
day = 1
outside = 0
name = ""
achivementout = 0
achivementsleep = 0
achivementdays = 0
achivementstore = 0
achivementcovid = 0
achieved = 0
cred = " view credits (u wont)"
secret = False
word_list = [
    "the", "at", "there", "some", "my", "of", "be", "use", "her", "than",
    "and", "this", "an", "would", "a", "have", "each", "make", "water", "to",
    "from", "which", "like", "been", "in", "or", "she", "is", "one", "do",
    "into", "who", "you", "had", "how", "time", "him", "call", "oil", "that",
    "by", "their", "has", "first", "its", "it", "word", "if", "look", "now",
    "he", "but", "will", "two", "find", "was", "not", "up", "more", "long",
    "for", "what", "other", "on", "all", "about", "code", "alphabet", "write",
    "down"
]
fortscript0 = "You log on Fortnite, but none of yor friends are online."

#opt.5
def game5():
  global cred
  os.system('clear')
  game5ch = int(
      input(
          f"1. {cred}\n2. Change name.\n3. Reset score.\n4. Check leaderboards.\n"
      ))
  if game5ch == 1:
    os.system('clear')
    print("Credits:")
    sleep(0.6)
    print('Lead designer:\n@GlixedYouTube\n')
    sleep(0.6)
    print('Lead coder:\n@GlixedYouTube\n')
    sleep(0.6)
    print('Idea via:\n@GlixedYouTube\n')
    sleep(0.6)
    print('Lead designer:\n@GlixedYouTube\n')
    sleep(0.6)
    print('so yeah i basically did everything.')
    sleep(0.6)
    print('oh wait i forgot something;')
    sleep(0.6)
    print('Lead supporter:\nJoey (@thatcringyguy)\n =] thx bro')
    sleep(2)
    cred = "5. view credits (yay u did)"
    gamecodes()
  elif game5ch == 2:
    os.system('clear')
    global name
    name = input("set new name:\n\n")
    if name == "glixed=]":
      koolbot()
      gamecodes()
    else:
      print("Your name has been changed to ", name)
      gamecodes()
  elif game5ch == 3:
    os.system('clear')
    global day, outside, achieved, achivementsleep, achivementdays, achivementcovid, achivementstore
    achieved = 0
    day = 1
    outside = 0
    achivementsleep = 0
    achivementdays = 0
    achivementcovid = 0
    achivementstore = 0
    a = '☐'
    b = '☐'
    c = '☐'
    d = '☐'
    e = '☐'
    print("Your data has been reset.")
    sleep(1)
    gamecodes()
  elif game5ch == 4:
    os.system('clear')
    print(f"Leaderboards:\n\n  Most days:\n\n    1. {lead00}\n    2. Joey")
    print(
        'to submit a leaderboard, comment a screenshot of your days, and wait for a response.'
    )
    sleep(2)
    gamecodes()


def koolbot():
  global secret
  global achieved
  global name
  print("nice. you found me.")
  achieved = 99999999999999999999999999999999999
  name = "s3cr3t"
  global outside
  outside = 99999999999999999999999999999999999
  secret = True
  sleep(0.9)
  print("adding infinite score...")


#checks if letter is in the word
def letterCheck(letter, word, wordGuessed, counter):

  found = False
  #tests for letter in word
  for i in range(len(word)):
    if letter == word[i]:
      temp = list(wordGuessed)
      temp[i] = letter
      wordGuessed = ''.join(temp)
      found = True

  #if the letter is not found, the user has one less try
  if not found:
    counter += 1
    print(f"{10 -counter} tries left")

  return wordGuessed, counter


#function for game
def starthang():

  print("HANGMAN guess letters to complete the word")

  word = random.choice(word_list)
  wordGuessed = ""
  print(wordGuessed)
  for _q in range(len(word)):
    wordGuessed += "_"

  #already guessed letters
  alreadyGuessed = []
  #count for tries
  counter = 0

  #sets tries for user
  while counter < 11:

    #user inputs letter
    guess = input("Guess letter: ").lower()
    #check if input is valid (one single letter)
    if guess.isalpha() and len(guess) == 1:

      #if the letter is already guessed, it will say already guessed, else, it will add the letter to alreadyGuessed, then it will run letterCheck
      if guess in alreadyGuessed:
        print("already guessed.")
      else:
        alreadyGuessed.append(guess)
        wordGuessed, counter = letterCheck(guess, word, wordGuessed, counter)
        print(wordGuessed)

      #if the user finished the word, it will say Yay!..., if user did not finish word, it will say GAME OVER
      if wordGuessed == word:
        print("Yay! \nYou have completed the hangman")
        break
      if counter == 10:
        print("You have ran out of tries.\nGAME OVER")

        break

    else:
      print("that's not one letter!")

  #shows the word at the end of the program
  print(f"The word was: {word}!")

  #if user wants to play again, the program loops, if not, the program ends.
  question = input("Do you want to play again?\n1. Yes\n2. No\n")
  if question == "1":
    os.system('clear')
    starthang()
  else:
    gamecodes()


# start of game
def reboot():
  print("rebooting...")
  sleep(0.4)
  print("starting main.py\nstarting function start()...")
  start()


winComb = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)],
           [(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 1), (2, 2)],
           [(0, 2), (1, 1), (2, 0)], [(0, 0), (1, 0), (2, 0)],
           [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]


#function for making the fancy grid
def printGrid(grid):
  print(grid[0])
  print(grid[1])
  print(grid[2])


#checks for a winning comination
def checkWin(grid):
  for comb in winComb:

    #converts winning cominations into varibles
    winComb1 = grid[comb[0][0]][comb[0][1]]
    winComb2 = grid[comb[1][0]][comb[1][1]]
    winComb3 = grid[comb[2][0]][comb[2][1]]
    #checks if winning cominations are in the grid
    if winComb1 == winComb2 == winComb3 and winComb1 != "":
      if grid[comb[0][0]][comb[0][1]] == "X":
        print("Player 1 wins!")
      else:
        print("Player 2 wins!")
      return True

  return False


def playTicTacToe():
  #grid for tic tac toe
  grid = [["", "", ""], ["", "", ""], ["", "", ""]]

  os.system('clear')
  printGrid(grid)

  turn = 0
  #Game loop
  while True:
    #determines the player's turn
    if (turn % 2) == 0:
      print("Player 1's turn.")
      symbol = "X"
    else:
      print("Player 2's turn.")
      symbol = "O"

    error = True
    #boolean loop for error
    while error:
      try:
        row = int(input("Enter your row number: ")) - 1
        col = int(input("Enter your column number: ")) - 1
      except:
        print("You cannot enter a letter.\n")
      else:
        error = False

      #if there is an invalid number
    while row > 2 or row < 0 or col > 2 or col < 0:
      print("Not a valid number.\n")
      break
    else:
      if grid[row][col] == "":
        #enters the symbol on the grid
        grid[row][col] = symbol
        #clears the screen
        os.system('clear')
        printGrid(grid)
        if checkWin(grid):
          break
        else:

          tie = True
          for row in grid:
            if "" in row:
              tie = False
          #if there is a tie
          if tie:
            print("Tie game! No one wins!")
            break

        turn += 1

      else:
        print("There is already a symbol there.\n")


playAgain = False
while playAgain:
  playTicTacToe()
  #if player(s) want to play again
  if input("\nDo you want to play again? [yes / no] ").lower() != "yes":
    print("Ok! PLEASE RE-RUN 2020.")
    playAgain = False
  else:
    os.system('clear')


#fort
def fortplay():
  os.system('cls')
  print('Fortnite graphics here')
  sleep(1)
  os.system('cls')


#end of tictactoe
def daycheck():
  global day
  global b
  global achieved
  if day == 10:
    print(
        f"ACHIVEMENT COMPLETE! congrats, {name}, you have played 2020 for 10 in-game days!"
    )
    sleep(2)
    achieved += 1
    b = "☑"
  else:
    pass


def storecheck():
  global achivementstore
  global achieved
  global c
  if achivementstore == 1:
    print(
        f"ACHIVEMENT COMPLETE! congrats, {name}, you have gone to the store to the first time!"
    )
    sleep(2)
    achieved += 1
    c = "☑"
    achivementstore = 9
  else:
    pass


def sleepcheck():
  global achieved
  global d
  global achivementsleep
  sleep(2)
  os.system('clear')
  if achivementsleep == 1:
    print(
        f"ACHIVEMENT COMPLETE! congrats, {name}, you have slept for the first time!"
    )
    sleep(2)
    achieved += 1
    d = "☑"
    achivementsleep = 9
  else:
    pass


def covidcheck():
  global achivementcovid
  global e
  global achieved
  if achivementcovid == 1:
    print(
        f"ACHIVEMENT COMPLETE! congrats, {name}, you have caught covid for the first time!... thats not a good thing..."
    )
    sleep(2)
    achieved += 1
    e = "☑"
    achivementcovid = 9
  else:
    pass


def outcheck():
  global achivementout
  global achieved
  if achivementout == 1:
    print(
        f"ACHIVEMENT COMPLETE! congrats, {name}, you went outside for the first time!"
    )
    sleep(2)
    achieved += 1
    achivementout = 9
    a = "☑"
  else:
    pass


def sleepfunc():
  global day
  global achivementsleep
  achivementsleep += 1
  day += 1
  os.system('clear')
  print(f"You chose to go to sleep. You will now skip to day {day}.")
  sleep(2)

  print(f"goodnight, {name}.")
  sleep(1)
  os.system('clear')
  print(f"[{name}] Zzz")
  sleep(0.5)
  os.system('clear')
  print(f"[{name}] Zzz.")
  sleep(0.5)
  os.system('clear')
  print(f"[{name}] Zzz..")
  sleep(0.5)
  os.system('clear')
  print(f"[{name}] Zzz...")
  sleep(0.5)
  os.system('clear')
  print("You have now slept, and one day has been added.")
  sleep(1)
  os.system('clear')
  gamecodes()


def storerun():
  global day
  global outside
  global store
  global achivementstore
  global achivementcovid
  achivementstore += 1
  os.system('clear')
  day += 1
  outside += 1
  store += 1
  chance = random.randint(1, 2)
  if chance == 1:
    storechoose = int(
        input(
            "You walk into the store and find out that there is a huge group of people surrounding one specific thing. You have 2 choices;\n1. Go and see what's happening (getting a chance of catching covid-19)\n2. walk away\n"
        ))
    if storechoose == 1:
      chance = random.randint(1, 5)
      print(
          "You walk over to see, turns out, they are fighting for toilet paper like there is no tomorrow.\nYou back up and start shopping as you normally would."
      )
      if chance == 1:
        os.system('clear')
        achivementcovid += 1
        print(
            "as you finish your shopping, you head home and you start feeling a little nauseous. You take a covid test, and you have covid. You will be stuck at home for 14 more days."
        )
        day += 14
        gamecodes()
      else:
        print("you finish shopping and you start heading home.")
        print("heading home...")
        sleep(2)
        gamecodes()
    else:
      print("You ignore the crowd and continue with your shopping.")
      print("heading home...")
      sleep(2)
      gamecodes()
  else:
    print("there is nobody inside the store, so you shop until the day ends.")
    print("heading home...")
    sleep(2)
    gamecodes()


def outsidehouse():
  global day
  global outside
  global achivementcovid
  global a
  global achivementout

  print(
      "    |-| |-| |-| |---| |    |---| |--| |---------| |---|          |-----| |--|                                      ++      ++     ++  \n    | |_| |_| | |-|   |    |     |  | | |-| |-| | |-|              | |   |  |                                     ++++    ++++   ++++ \n    |_________| |---| |___ |---| |__| |_| |_| |_| |---|            |_|   |--|                                    ++++++  ++++++ ++++++\n    |-----| |-|_|-| |---|        |--| |-| |-| |-----| |---| |---| |---|  |---|                                    ++++    ++++   ++++ \n      | |   | |_| | |-|          |  | | |_| |   | |   |__|   | |  |    | |-|                                       ||      ||     ||  \n      |_|   |_| |_| |---|        |__| |_____|   |_|   ___|  |___| |___|  |---|                                   __||______||_____||__"
  )
  print("loading...")
  sleep(1.9)
  print("loaded.")
  sleep(0.5)
  os.system('clear')
  outchoice = int(
      input(
          f"welcome outside, {name}. You have 2 options currently;\n1. Go for a walk\n2. Go to the store\n\n"
      ))
  if outchoice == 1:
    os.system('clear')
    print("you chose to go on a walk.")
    outside += 1
    achivementout = 1
    print("walking in the park...")
    chance = random.randint(1, 3)
    if chance == 1:
      os.system('clear')
      dodge = int(
          input(
              "you see someone walikng towards you ahead. what should you do?\n1. Move to the side a little\n2. Stay 2 meters (3 feet) away\n3. Run into them\n"
          ))
      if dodge == 2:
        print("Good. You have sucessfully avoided a person.")
      else:
        achivementcovid += 1
        print(
            "Turns out that that person has caught covid. You have now caught it by getting too close to them. You will go into quarintine for 14 days."
        )
        day += 14
        achivementout = 1
        gamecodes()
    else:
      print(
          "you sucessfully went on a peaceful walk without bumping into anyone, you wil now be sent home."
      )
      sleep(2.2)
      day += 1
      gamecodes()
  if outchoice == 2:
    print(
        "|-----------------------------------------|\n|   |---|      |-|      |--|     |----|   |\n|   |____      | |_     |  |     |____|   |\n|   ----|      |_|_|    |__|     |        |\n|                                         |\n|                  |--|                   |\n|                  | .|                   |\n|__________________|__|___________________|"
    )
    sleep(2)
    storerun()


def stats():
  print(
      f"Welcome back, {name}. Here are your stats.\n\nACHIVEMENTS: {achieved}/5 achievements complete"
  )
  print(
      f"{a} Go outside\n{b} 10 in-game days\n{c} Go to the store\n{d} Sleep\n{e} Catch covid"
  )
  backtomenu = input(f"\n\nYou have gone outside {outside} times.\nIt is day {day}.\nYou have been to the store {store} times.\n\nType 1 to go back\n")
  if backtomenu == 1:
    gamecodes()
  else:
    gamecodes()


def gamecodes():
  global day
  global achieved
  outcheck()
  daycheck()
  storecheck()
  sleepcheck()
  covidcheck()
  gamechoice = int(
      input(
          "welcome to 2020. We have 'lots' of things to do. for example:\n1. play a game or two.                                         |---| |----|  |---| |----|\n2. go outside.                                                  -/ | |    |   -/ | |    |\n3. go to sleep.                                                |  /  |    |  |  /  |    |\n4. check your stats.                                           |___| |____|  |___| |____|\n5. Options and Leaderboards.\nYou can type 1, 2, 3, 4 or 5 to choose your option.\n\n"
      ))
  if gamechoice == 1:
    gamein = int(
        input(
            "choose a game you would like to play, 1 for tic tac toe (two player), or 2 for hangman.\n\n"
        ))
    if gamein == 1:
      playTicTacToe()
    else:
      starthang()
  if gamechoice == 2:
    outsidehouse()
  if gamechoice == 3:
    sleepfunc()
  if gamechoice == 4:
    stats()
  if gamechoice == 5:
    game5()
  else:
    print("Nice try, not a valid number.")


def start():

  print("Starting (or restarting) the game...")
  sleep(0.5)
  print("REMEMBER TO ENTER FULLSCREEN.")
  sleep(1.5)
  os.system('clear')
  print("\033[1;34")
  print(
      "\n BY:    GlixedYouTube ON YOUTUBE\nPUBLISHED: this game is in beta\nCREATED:   9 JUNE, 2023\nUPDATED:   Nov. 19, 2023\nA GAME ABOUT THE OUTBREAK.\nversion: orgi-1.1\n|---| |----|  |---| |----|\n -/ | |    |   -/ | |    |\n|  /  |    |  |  /  |    |\n|___| |____|  |___| |____|"
  )

  sleep(2)

  gamecodes()


print("\033[0;35;40m")
name = input(
    "|---| |----|  |---| |----|\n -/ | |    |   -/ | |    |\n|  /  |    |  |  /  |    |\n|___| |____|  |___| |____|\nPLEASE ENTER A NAME:\n\n"
)
if name == "glixed=]":
  koolbot()
  start()
else:
  start()
if achivementcovid >= 1:
  covidrand = random.randint(1,5)
  if covidrand == 1:
    print("you start to feel worse and worse over time, and you evntually pass away from covid.")
  else:
    pass
else:
  pass

start()
