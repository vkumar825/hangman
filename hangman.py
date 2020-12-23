import random
import sys
win = 0
loss = 0

def start():
    print("Welcome to the game of Hangman!")
    
    while True:
        choice = input("Are you ready to begin? (Y/N): ").lower()
        if choice == 'y':
            word = get_word()
            guess_word(word)
        if choice == 'n':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid input. Please try again.")

def get_word():
    easy_words = ["cat", "dog", "bomb", "sun", "rain", 
                  "heart", "key", "hotdog", "study", "oil",
                   "music", "sing", "cry", "lose", "laugh",
                   "dinner", "cloud", "water", "ice", "fire"]

    medium_words = ["photograph", "lightsaber", "lawnmower", "gingerbread", "platypus",
                    "project", "dominoes", "helicopter", "pyramid", "stonehenge",
                    "assignment", "stockholder", "quarantine", "flotsam", "psycho",
                    "loiterer", "kilogram", "blacksmith", "stowaway", "addendum"]

    hard_words = ["juandice", "intelligence ", "unimaginatively ", "uncopyrightable ", "mississippi",
                  "pronunciation", "chiaroscurist", "sacrilegious", "accommodation", "gubernatorial",
                  "onomatopoeia", "paraphernalia", "psychotomimetic", "introduction", "accumulation",
                  "trichotillomania", "superintendent", "strikebreaker", "constellation", "civilization"]

    while True:
        difficulty = input("Difficulty (Easy/Medium/Hard): ").lower()
        if difficulty == "easy":
            return random.choice(easy_words)
        
        if difficulty == "medium":
            return random.choice(medium_words)

        if difficulty == "hard":
            return random.choice(hard_words)
        else:
            print("Invalid input. Please try again.")

def guess_word(word_choice):
    enable_hint = input('Do you want to enable hints? (Y/N): ').lower()
    if enable_hint == 'y':
        hint_check = True
    else:
        hint_check = False

    global win
    global loss
    word_letters = [char for char in word_choice]
    display_answer = []
    used_letters = []
    display_str = ''
    used = ', '
    mistake_count = 0

    for i in range(len(word_letters)):
        placeholder = ' _ '
        display_answer.append(placeholder)

    print("The word you are solving for is", len(word_choice), "letters long. Good luck!")
    while True:
        answer = input("\nGuess a letter: ").lower()
        if answer not in 'abcdefghijklmnopqrstuvwxyz':
            print("It must be a letter, try again.")

        if answer in 'abcdefghijklmnopqrstuvwxyz':
            if answer in word_letters:
                print("That's the right letter.")
                used_letters.append(answer)
            else:
                print("That's the wrong letter.")
                used_letters.append(answer)
                mistake_count += 1

            if answer not in display_answer:
                for i in range(len(word_choice)):
                    if answer == word_choice[i]:
                        display_answer[i] = answer
            else:
                print("You already used that letter.")
            
            correct_word = display_str.join(display_answer)
            print("You have used:", used.join(used_letters))
            print("The word is", correct_word)

            if correct_word in word_choice:
                print("\nYou got the right word, you win!")
                win += 1
                play_again = input('Do you want to go again? (Y/N): ').lower()
                if play_again == 'y':
                    start()
                else:
                    print("Win:", win)
                    print("Loss:", loss)
                    sys.exit(0)

        if mistake_count == 1:
            print(gallows_stages[1])

        if mistake_count == 2:
            print(gallows_stages[2])

        if mistake_count == 3:
            print(gallows_stages[3])

        if mistake_count == 4:
            print(gallows_stages[4])

        if mistake_count == 5:
            print(gallows_stages[5])

        if mistake_count == 6:
            print(gallows_stages[6])
            loss += 1
            print("Game over! You've been hanged!")
            print("The correct word was", word_choice + ".")
            play_again = input('Do you want to try again? (Y/N): ').lower()
            if play_again == 'y':
                start()
            else:
                print("Win:", win)
                print("Loss:", loss)
                sys.exit(0)

        if hint_check:
            get_hint(word_choice)

def get_hint(word_choice):
    random_letter = random.choice(word_choice)
    while True:
        hint = input("Need a hint? (Y/N): ").lower()
        if hint == 'y':
            print("You have chosen to use a hint.")
            print("The word has letter", random_letter, "in it.")
            break

        if hint == 'n':
            print("You have chosen to not use a hint.")
            break

gallows_stages = [
        """
        _______  
        |     |  
        |        
        |                   
        |        
       _|________
        """,
        """
        _______  
        |     |  
        |     O  
        |        
        |        
       _|________
        """,
        """
        _______  
        |     |  
        |     O  
        |     |  
        |        
       _|________
        """,
        """
        _______  
        |     |  
        |     O  
        |    /|  
        |        
       _|________
        """,
        """
        _______  
        |     |  
        |     O  
        |    /|\  
        |        
       _|________
        """,
        """
        _______  
        |     |  
        |     O  
        |    /|\  
        |    /  
       _|________
        """,
        """
        _______  
        |     |  
        |     O  
        |    /|\  
        |    / \ 
       _|________
        """
    ]


if __name__ == '__main__':
    start()