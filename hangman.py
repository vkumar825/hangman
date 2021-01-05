import random
from hangman_stages import stages
win = 0
loss = 0

def get_word():
    with open('wordlist.txt') as words_file:
        word_list = words_file.read().splitlines()
    
    easy_words = []
    medium_words = []
    hard_words = []

    for word in word_list:
        if len(word) < 6:
            easy_words.append(word)
        elif len(word) < 12:
            medium_words.append(word)
        else:
            hard_words.append(word)

    while True:
        difficulty = input("Difficulty (Easy/Medium/Hard): ").lower()
        if difficulty == "easy":
            return random.choice(easy_words)

        if difficulty == "medium":
            return random.choice(medium_words)

        if difficulty == "hard":
            return random.choice(hard_words)


def game(word_choice):
    enable_hint = input('Do you want to enable hints? (Y/N): ').lower()
    if enable_hint == 'y':
        hint_check = True
    else:
        hint_check = False

    global win, loss
    mistake_count = 0
    hint_used = 0
    display_answer = []
    used_letters = []
    word_letters = [letters for letters in word_choice]
    display_str = ''
    used = ', '

    for i in range(len(word_letters)):
        placeholder = ' _ '
        display_answer.append(placeholder)

    print("The word you are solving for is", len(word_choice), "letters long. Good luck!")
    while True:
        answer = input("\nGuess a letter: ").lower()
        if answer not in 'abcdefghijklmnopqrstuvwxyz':
            print("Invalid input, it must be a letter. Please try again.")

        if answer in 'abcdefghijklmnopqrstuvwxyz':
            if answer in word_letters:
                print("Correct! That's the right letter.")
                used_letters.append(answer)
            else:
                print("Wrong! That's the incorrect letter.")
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
                    word = get_word()
                    game(word)
                else:
                    print("Win:", win)
                    print("Loss:", loss)
                    break

        if mistake_count == 1:
            print(stages[1])

        elif mistake_count == 2:
            print(stages[2])

        elif mistake_count == 3:
            print(stages[3])

        elif mistake_count == 4:
            print(stages[4])

        elif mistake_count == 5:
            print(stages[5])

        else:
            print(stages[6])
            loss += 1
            print("Game over! You've been hanged!")
            print("The correct word was", word_choice + ".")
            play_again = input('Do you want to try again? (Y/N): ').lower()
            if play_again == 'y':
                word = get_word()
                game(word)
            else:
                print("Win:", win)
                print("Loss:", loss)
                break

        if hint_check:
            get_hint(word_choice)

def get_hint(word_choice):
    word_letters = [letters for letters in word_choice]
    random_letter = random.choice(word_letters)
    while True:
        hint = input("Need a hint? (Y/N): ").lower()
        if hint == 'y':
            print("You have chosen to use a hint.")
            print("The word has letter", random_letter, "in it.")
            break

        if hint == 'n':
            print("You have chosen to not use a hint.")
            break

if __name__ == '__main__':
    print("Welcome to the game of Hangman!")
    while True:
        choice = input("Are you ready to begin? (Y/N): ").lower()
        if choice == 'y':
            word = get_word()
            game(word)
        if choice == 'n':
            print("Goodbye!")
            break