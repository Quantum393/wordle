import random

words = []
length = 5
sentinel = True
correct = 0
class colours:
    CORRECT = '\033[1;32;32m'
    CONTAINS = '\033[1;32;33m'
    END = '\033[1;m'
    
def word_list(words, length:int):
    f = open("words.txt", "r")
    for line in f:
        
        if len(line.strip()) == length:
            words.append(line)
    f.close()
    return words

def random_choice(words):
    word = random.choice(words)
    print(word[:-1])
    return word[:-1]

def user_input(length):
 
  guess = input("   \n")
  if len(guess) != length:
    print("Please enter a 5 letter word")
    return user_input(length)

  f = open("words.txt", "r")

  words = []
  for line in f.readlines():
    words.append(line[:-1])
 
  if guess in words:
    return guess
  else:
    print("Invalid word")
    return user_input(length)
  
def compare(guess:str, random_word, sentinel, correct):
   
    correct = 0
    while sentinel == True:
      for count, value in enumerate(guess):
          
        
            if value == random_word[count]:
                print(colours.CORRECT, value.upper(), colours.END, end = " ")
                correct += 1
                
                if correct == len(random_word):
                  
                  return
                  
            elif value in random_word:
                print(colours.CONTAINS, value.upper(), colours.END, end = " ")
            
            else:
                print("" ,value.upper(), end = " ")
            
      guess = user_input(length)
      correct = 0

word_list(words, 5)
random_word = random_choice(words)
guess = user_input(length)
compare(guess, random_word, True, correct)


