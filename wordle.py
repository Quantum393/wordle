import random


words = []

class colours:
    CORRECT = '\033[1;32;32m'
    END = ''

def word_list(words, length:int):
    f = open("words.txt", "r")
    for line in f:
        if len(line.strip()) == length:
            words.append(line)
    return words

def random_choice(words):
    word = random.choice(words)
    print(word[:-1])
    return word[:-1]


def compare(user_input:str, random_word):
    for count, value in enumerate(user_input):

        if value == random_word[count]:
            print(colours.CORRECT, "hello", "red")
        elif value in random_word:
            print(value, "in!")
        else:
            print("nope")



word_list(words, 5)
random_word = random_choice(words)
compare("abcde", "abced")


