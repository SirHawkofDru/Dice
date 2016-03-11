import random

def pause():
    question = raw_input("Would you like to roll again? ").lower()
    if question == 'yes' or question == 'y':
        generate()
    else:
        print "Thank you for playing."
        exit(0)

def dice():
    try:
        dice = int(input("Please enter the number of dice you would like to roll: "))
        return dice
    except:
        dice()

def roll():
    number_of_dice = []
    for n in range(1, dice() + 1):
        number_of_dice.append(n)
    return number_of_dice

def sides(n):
    try:
        sides = input("How many sides on die %r? " % n)
        return sides
    except:
        sides()

def generate():
    number_of_dice = roll()
    sides_per_die = {}
    for n in number_of_dice:
        sides_per_die[str(n)] = str(sides(n))

    for k, v in sorted(sides_per_die.items()):
        result = random.randint(1, int(v))
        print "Die %s, which has %s sides, landed on %i" % (k, v, result)
    pause()

generate()