import random

def shuffle(list):
    random.shuffle(list)
    for x in range(0, 5):
        list1.pop(1)
    return list1


def userguess():
    for x in range(0, 4):
        Guess.append(input("Enter the colors one by one: "))


def game():

    for i in range(0, len(list1)):
        if list1[i] == Guess[i]:
            endList.append("correct")
        elif Guess[i] in list1:
            endList.append("close")
        elif list1[i] != Guess[i]:
            endList.append("WRONG XD")
    print(endList)
    endList.clear()
    Guess.clear()


######################################################################################################################

endList = []
list1 = ["blue", "red", "white", "purple", "yellow", "green", "black", "orange", "pink"]
Guess = []
trials = 1

######################################################################################################################
print("###############################################################################################################")
print("""WHEN YOU GUESS, CORRECT MEANS YOU GOT IT RIGHT,

WRONG XD MEANS YOU GOT IT WRONG AND

CLOSE MEANS YOU GOT THE COLOR BUT IT'S IN THE WRONG POSITION!!!!""")

print("###############################################################################################################")
print("""HERE ARE THE COLORS YOU HAVE TO GUESS FROM


blue, red, white, purple, yellow, green, black, orange, pink


IT IS CASE SENSITIVE!!!!!!!!!""")
print("###############################################################################################################")

######################################################################################################################

shuffle(list1)
userguess()

if list1 == Guess and trials == 1:
    print('')
    print("You are so lucky wow XDDDDD")

while Guess != list1:
    game()
    userguess()
    trials = trials + 1
    if trials >= 10:
        print('')
        print("wow you are fucking stupid")
        break

if list1 == Guess and trials != 1:
    print('')
    print("You finally guessed it")
    print("it took you " + str(trials) + " tries")


