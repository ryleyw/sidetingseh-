import random as rand

things = ["Fortnite", "Minecraft", "Talk about my feelings", "ASK HER OUT"]

def suggestion():
    chance = rand.randint(0, 100)
    if chance <= 33:
        return things[0]
    elif chance <= 66:
        return things[1]
    elif chance <= 99:
        return things[2]
    else:
        return things[3]

print(suggestion())
    