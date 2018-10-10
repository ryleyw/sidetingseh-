import random

FILE_NAME = "words.txt"
words_list = []
actions = ["eating", "loving", "smelling", "worshiping"]

with open(FILE_NAME, 'r') as f:
    for line in f:
        for word in line.split():
            words_list.append(word)

str = "You're a {} {} {} {}!".format(random.choice(words_list), random.choice(actions), random.choice(words_list), random.choice(words_list))

print(str)