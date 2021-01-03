from random import random

def flip_coin():
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"

print(flip_coin())
print(flip_coin())
print(flip_coin())

# redefining same function overwrites existing function
def flip_coin():
    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"

print(flip_coin())
print(flip_coin())
print(flip_coin())

