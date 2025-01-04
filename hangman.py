import random
def hangman():
    word_list = ["python", "tshering", "dipkiran", "umesh","programmer"]
    string = random.choice(word_list)
    print("Welcome to the Hangman Game!!")
    print('Good Luck Mate!!')
    print("The word is of ",len(string), "letters")
    stages = [r"""
      -----------
      |          |
      |          O
      |         
      |         
      |         
      |
      """,
      r"""
      -----------
      |          |
      |          O
      |          |
      |          |
      |      
      |
      """,
      r"""
      -----------
      |          |
      |          O
      |         /|
      |          |
      |         
      """,
      r"""
      -----------
      |          |
      |          O
      |         /|\
      |          |
      |         
      |
      """,
      r"""
      -----------
      |          |
      |          O
      |         /|\
      |          |
      |         / 
      |
      """,
      r"""
      -----------
      |          |
      |          O
      |         /|\
      |          |
      |         / \
      |
      """
        ]
    incorrect_guess = 0
    guesses = []
    guessed_word = ['_'] * len(string)
    
    while len(stages) > 0:
        print("Current Word: ", " " .join(guessed_word))
        print("-------------------------------------------")
        user_guess = input("Enter your guess: ")
        if len(user_guess) == 1: #for a single letter guess only
            if user_guess in guesses:
                print("You already guessed that letter! ")
            else:
                guesses.append(user_guess)
                if user_guess in string:
                    print("Correct Guess!!")
                    for i in range(len(string)):
                       if string[i] == user_guess:
                            guessed_word[i] = user_guess
                else:                   
                    incorrect_guess += 1
                    if incorrect_guess <= len(stages):
                        print('Wrong Guess! Try Again!')
                        print(stages[incorrect_guess-1])
                    if incorrect_guess == len(stages):
                        print("You are out of chances..")                       
                        print("GAME OVER!")
                        break
        else:
            print("Invalid input. ")
        if "".join(guessed_word) == string:
            print("Congratulations! You guessed the word:", string)
            break   
hangman()
