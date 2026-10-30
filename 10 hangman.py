import random

print('Welcome to Hangman!')
print('You get 5 Guesses')

words = ['thief', 'stall', 'stalk']
secret_worlds = random.choice(words)
display_word = []
for letter in secret_worlds:
   display_word += "_"
print(display_word)

num = 0
gameover = False

while not gameover:
   guess = input('Guess a letter ').lower()
   for postion in range(len(secret_worlds)):
        letter = secret_worlds[postion]
        if letter == guess:
            display_word[postion] = letter
   if guess not in secret_worlds:
       num += 1
       guesses_left = 5 - num
       print(f"You've {guesses_left} guesses left" )
       if num >= 5:
           print('You lose')
           gameover = True
   print(display_word)
   if "_" not in display_word:
       print("you win")
       gameover = True
