import random
from words import word_list

# Get a random word from the words.py file.


def get_word():
  selected_word = (random.choice(word_list))
  return selected_word.upper()

# Based on the stage of the game, the correct hangman illustration will be shown.


def display_hangman(tries):
  stages = {0: "\
    |------\n\
    |    O\n\
    | ---|---\n\
    |   / \\ \n\
    |  /   \\ \n\
    |_____",  1: "\
    |------\n\
    |    O\n\
    | ---|---\n\
    |   /  \n\
    |  /    \n\
    |_____",  2: "\
    |------\n\
    |    O\n\
    | ---|---\n\
    |      \n\
    |       \n\
    |_____",  3: "\
    |------\n\
    |    O\n\
    | ---|   \n\
    |      \n\
    |       \n\
    |_____",  4: "\
    |------\n\
    |    O\n\
    |    |   \n\
    |      \n\
    |       \n\
    |_____",  5: "\
    |------\n\
    |    O\n\
    |        \n\
    |      \n\
    |       \n\
    |_____",  6: "\
    |------\n\
    |     \n\
    |        \n\
    |      \n\
    |       \n\
    |_____"}

  return stages[tries]


def display_current_progress(tries,word_completion):
  print(display_hangman(tries))
  print(word_completion)
  print("\n")

def play(selected_word):
  word_completion = "." * len(selected_word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  # Print out message to the user.
  print("Let's play some Hangman!")
  display_current_progress(tries,word_completion)

  while not guessed and tries > 0:
    #Ask user for initial guess.
    guess = input("Please guess a letter or word: ").upper()
    
    #Check to see if guess is a single character.
    if len(guess) == 1 and guess.isalpha():
      
      #Check to see if this letter has already been guessed.
      if guess in guessed_letters:
        print("You already guessed this letter")
      
      #If guessed letter is not in word, reduce tries variable by 1 and add it to guessed letters. 
      elif guess not in selected_word:
        print(guess, "is not in the word.")
        tries -= 1
        guessed_letters.append(guess)

      #If the guessed letter is in the word, let the user know and add it to the guessed letters list.
      #Fill in word completion with guessed letter.
      else:
        print("Good job,", guess, "is in the word!")
        guessed_letters.append(guess)
        word_as_list=list(word_completion)
        indices= [i for i, letter in enumerate(selected_word) if letter == guess]
        for index in indices:
            word_as_list[index]=guess
        word_completion="".join(word_as_list)
       
        #If they've guessed it correctly, change guessed condition to True. 
        if "." not in word_completion:
            guessed = True
    
    #If they're guessing a whole word and it's not the correct length let them know. 
    elif len(guess) != len(selected_word) and guess.isalpha():
      print("Guess is not the correct length")
    
    #If the guessed word is the correct length.
    elif len(guess) == len(selected_word) and guess.isalpha():
      
      #If they've already guessed this word then let them know. 
      if guess in guessed_words:
        print("You already guess the word", guess)
      
      #If they've guessed incorrectly, let them know and add it to guessed words. Also decrease tries variable.
      elif guess !=selected_word:     
        print(guess,"is not the word.")
        tries-=1
        guessed_words.append(guess)
      
      #If they've guessed it correctly, change guessed variable to True  and update word completion.
      else:
        guessed=True
        word_completion=selected_word
    
    #If they haven't entered a valid guess let them know. 
    else:
      print("Not a valid guess.")
  
    display_current_progress(tries,word_completion)


  if guessed:
    print("Congrats, you did it!")
  else:
    print("Sorry, you lost. The word was " + selected_word)

# Run the code and ask if the individual would like to run again.
def main():
  word=get_word()
  play(word)
  while input("Play Again? (Y/N) ").upper()=="Y":
    word=get_word()
    play(word)

if __name__ == "__main__":
  main()



