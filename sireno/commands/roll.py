import random

def rollDice(dice):
    match dice:
        case "d20":
            return random.randrange(1, 20)
        case "d8":
            return random.randrange(1, 8)
        case "d6":
            return random.randrange(1, 6)
        case "d4":
            return random.randrange(1, 4)
        case _:
            return -1