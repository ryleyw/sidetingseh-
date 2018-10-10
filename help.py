import random as rand
import time

def love():
    print("she loves me")

def not_love():
    print("she loves me not")

def does_she_love_me(i, state):
    time.sleep(1)
    if i is 0:
        time.sleep(2)
        print("So it's settled...")
        time.sleep(2)
        print("SHE LOVES ME!") if state is True else print("she loves me not... :(")
    else:
        love() if state is True else not_love()
        does_she_love_me(i - 1, not state)

does_she_love_me(rand.randint(5, 18), True)
