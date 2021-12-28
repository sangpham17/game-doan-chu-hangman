import random

print("""GAME ĐOÁN CHỮ (HANGMAN)
******************************************************
Điền vào các ô trống bên dưới""")

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
wordList = '''ant baboon badger bat bear beaver camel cat clam cobra cougar 
        coyote crow deer dog donkey duck eagle ferret fox frog goat 
        goose hawk lion lizard llama mole monkey moose mouse mule newt 
        otter owl panda parrot pigeon python rabbit ram rat raven 
        rhino salmon seal shark sheep skunk sloth snake spider 
        stork swan tiger toad trout turkey turtle weasel whale wolf 
        wombat zebra '''.split()

randomWord = (random.choice(wordList))

print(randomWord)

dapAn = []

for blank in range(len(randomWord)):
    dapAn.append("_")

print(' '.join(dapAn))

life = 7

while('_' in dapAn):
    guess = input('Bạn đoán chữ nào: ')

    if(guess in randomWord):

        for c in range(len(randomWord)):

            if(guess == randomWord[c]):
                dapAn[c] = guess

        print(' '.join(dapAn))
    else:
        print(f"sai, còn lại {life-1} mạng")
        print(HANGMANPICS[-life])
        life -= 1

        if(life == 0):
            break

if('_' in dapAn):
    print("You lose!!")
else:
    print("You win!!")

print("\nKết thúc")
