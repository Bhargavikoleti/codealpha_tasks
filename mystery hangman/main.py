import random
from words import easy_words, medium_words, hard_words
def save_score(score):
    with open("score.txt", "a") as file:
        file.write(str(score) + "\n")
def choose_word():
    print("\nChoose Difficulty")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter choice: ")
    if choice == "1":
        return random.choice(easy_words)
    elif choice == "2":
        return random.choice(medium_words)
    else:
        return random.choice(hard_words)
score = 0
wins = 0
losses = 0
while True:
    word = choose_word()
    guessed_letters = []
    attempts = 6
    print("\nHint: First letter is", word[0])
    while attempts > 0:
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print("\nWord:", display)
        print("Guessed letters:", guessed_letters)
        print("Attempts left:", attempts)
        if "_" not in display:
            print("\nCongratulations! You guessed the word.")
            score += 10
            wins += 1
            break
        guess = input("Enter a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1
            print("Wrong Guess!")
    if attempts == 0:
        print("\nGame Over!")
        print("Correct word was:", word)
        losses += 1
    print("\nCurrent Score:", score)
    print("Wins:", wins)
    print("Losses:", losses)
    save_score(score)
    play_again = input("\nPlay Again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("\nThanks for playing Mystery Hangman Arena")