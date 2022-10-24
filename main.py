import random

words = []
length = 5
sentinel = True

class colours:
    CORRECT = '\033[1;32;32m'
    CONTAINS = '\033[1;32;33m'
    END = '\033[1;m'
    ERROR = '\033[1;31m'
    BLUE = '\033[1;32;34m'
    PURPLE = '\033[1;32;35m'
    CYAN = '\033[1;32;36m'

def word_list(words, length:int):
    f = open("words.txt", "r")
    for line in f:

        if len(line.strip()) == length:
            words.append(line)
    f.close()
    return words

def random_choice(words):
    word = random.choice(words)
    return word[:-1]

def user_input(length, random_word):

    guess = input("\n \n").lower()
    if guess == "q":
      print("Unlucky! The word was", random_word)
      quit()
      

    if len(guess) != length:
        print(colours.ERROR, "Please enter a", length, " letter word", colours.END)
        return user_input(length, random_word)

    f = open("words.txt", "r")

    words = [line[:-1] for line in f]

    if guess in words:
        return guess
    else:
        print(colours.ERROR, "Invalid word", colours.END)
        return user_input(length, random_word)

def compare(guess:str, random_word, sentinel, attempts):

    while sentinel == True:
        attempts += 1
        for count, value in enumerate(guess):

            if value == random_word[count]:
                print(colours.CORRECT, value.upper(), colours.END, end = " ")
                if count == len(random_word)-1 and guess == random_word:
                    print(f"\n \n{colours.ERROR} Co{colours.CONTAINS}ng{colours.CORRECT}ra{colours.CORRECT}tu{colours.CYAN}lat{colours.BLUE}io{colours.PURPLE}ns{colours.END}! You got the wordle in", attempts)
                    return

            elif value in random_word:
                print(colours.CONTAINS, value.upper(), colours.END, end = " ")

            else:
                print("" ,value.upper(), end = "  ")

        print("\n _________________")

        guess = user_input(length, random_word)


print("Welcome to bootleg Wordle! - Enter Q when if you give up! ")
word_list(words, length)
random_word = random_choice(words)
guess = user_input(length, random_word)
compare(guess, random_word, True, 0)


