# File: hw5b.py
# Author: Sam Waggoner
# Date: 10/22/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Write a program to make a simplified version of the card game war.
# Collaboration:
# I worked by myself.

# Note: I assumed that if a four of clubs is drawn, the player who drew it would
# lose all their points and that even if the other player's card was larger than
# a four, they would not get a point. (This could be changed by replacing the elif
# statements after line 127 to if statements.) I assumed the same thing with sevens--
# if a seven is drawn then the player gains a point and their opponent loses all
# their points WITHOUT an opportunty to gain one point if their card is larger than 
# the seven. I also added a line that prevented the whole game from just printing
# out, instead requiring initiation from the user so that the user can be involved
# in the game as it plays out, and they can also quit it mid-game. A version without
# that line is quoted out at the bottom.

import random

def main():

    def drawcard():
        p1card = random.randint(2,14)
        p2card = random.randint(2,14)
        p1suit = random.randint(1,4)
        p2suit = random.randint(1,4)
        return(p1card,p2card,p1suit,p2suit)

    def p1printcards(a,b):
        # card number
        if a == 1:
            a = "one"
        if a == 2:
            a = "two"
        if a == 3:
            a = "three"
        if a == 4:
            a = "four"
        if a == 5:
            a = "five"
        if a == 6:
            a = "six"
        if a == 7:
            a = "seven"
        if a == 8:
            a = "eight"
        if a == 9:
            a = "nine"
        if a == 10:
            a = "ten"
        if a == 11:
            a = "jack"
        if a == 12:
            a = "queen"
        if a == 13:
            a = "king"
        if a == 14:
            a = "ace"
        # suit
        if b == 1:
            b = "clubs"
        if b == 2:
            b = "diamonds"
        if b == 3:
            b = "hearts"
        if b == 4:
            b = "spades"
        return "Player 1 draws the "+a+" of "+b+"."
    def p2printcards(a,b):
        # card number
        if a == 1:
            a = "one"
        if a == 2:
            a = "two"
        if a == 3:
            a = "three"
        if a == 4:
            a = "four"
        if a == 5:
            a = "five"
        if a == 6:
            a = "six"
        if a == 7:
            a = "seven"
        if a == 8:
            a = "eight"
        if a == 9:
            a = "nine"
        if a == 10:
            a = "ten"
        if a == 11:
            a = "jack"
        if a == 12:
            a = "queen"
        if a == 13:
            a = "king"
        if a == 14:
            a = "ace"
        # suit
        if b == 1:
            b = "clubs"
        if b == 2:
            b = "diamonds"
        if b == 3:
            b = "hearts"
        if b == 4:
            b = "spades"
        return "Player 2 draws the "+a+" of "+b+"."

    p1pts = 0
    p2pts = 0
    while p1pts < 10 and p2pts < 10 and input("Press any key to initiate the round (quit to end): ") != "quit":
        cards = drawcard()
        print(p1printcards(cards[0],cards[2]))
        print(p2printcards(cards[1],cards[3]))
        if cards[0] == cards[1] and cards[0] == 7:
            print("Two sevens! Both players reset to one point!")
            p1pts = 1
            p2pts = 1
        if cards[0] == 4 and cards[2] == 1 and cards[1] == 4 and cards[3] == 1:
            print("Two fours of clubs! Both players lose all their points!")
            p1pts = 0
            p2pts = 0
        else:
            if cards[0] == 4 and cards[2] == 1:
                print("Four of clubs! Player 1 loses all their points!")
                p1pts = 0
            elif cards[1] == 4 and cards[3] == 1:
                print("Four of clubs! Player 2 loses all their points!")
                p2pts = 0
            elif cards[0] == 7:
                print("Seven! Player 1 earns one point while Player 2 loses all their points!")
                p1pts += 1
                p2pts = 0
            elif cards[1] == 7:
                print("Seven! Player 1 earns one point while Player 2 loses all their points!")
                p2pts += 1
                p1pts = 0
            else:
                if cards[0] > cards[1]:
                    print("Player 1 wins this round.")
                    p1pts += 1
                if cards[1] > cards[0]:
                    print("Player 2 wins this round.")
                    p2pts += 1
                if cards[0] == cards[1]:
                    if cards[2] > cards[3]:
                        print("Player 1 wins this round.")
                        p1pts += 1
                    if cards[3] > cards[2]:
                        print("Player 2 wins this round.")
                        p2pts += 1
                    if cards[2] == cards[3]:
                        print("Tie; both players lose one point.")
                        p1pts -= 1
                        p2pts -= 1
        print("P1 pts:",p1pts,"--- P2 pts:",p2pts)
    if p1pts == 10:
        print("Congratulations, Player 1 wins!")
        print("♪┏(・o･)┛♪┗ (･o･ )┓♪")
    if p2pts == 10:
        print("Congratulations, Player 2 wins!")
        print("♪┏(・o･)┛♪┗ (･o･ )┓♪")

main()

# This version does not have the user-dictated new round.

"""
import random

def main():

    def drawcard():
        p1card = random.randint(2,14)
        p2card = random.randint(2,14)
        p1suit = random.randint(1,4)
        p2suit = random.randint(1,4)
        return(p1card,p2card,p1suit,p2suit)

    def p1printcards(a,b):
        # card number
        if a == 1:
            a = "one"
        if a == 2:
            a = "two"
        if a == 3:
            a = "three"
        if a == 4:
            a = "four"
        if a == 5:
            a = "five"
        if a == 6:
            a = "six"
        if a == 7:
            a = "seven"
        if a == 8:
            a = "eight"
        if a == 9:
            a = "nine"
        if a == 10:
            a = "ten"
        if a == 11:
            a = "jack"
        if a == 12:
            a = "queen"
        if a == 13:
            a = "king"
        if a == 14:
            a = "ace"
        # suit
        if b == 1:
            b = "clubs"
        if b == 2:
            b = "diamonds"
        if b == 3:
            b = "hearts"
        if b == 4:
            b = "spades"
        return "Player 1 draws the "+a+" of "+b+"."
    def p2printcards(a,b):
        # card number
        if a == 1:
            a = "one"
        if a == 2:
            a = "two"
        if a == 3:
            a = "three"
        if a == 4:
            a = "four"
        if a == 5:
            a = "five"
        if a == 6:
            a = "six"
        if a == 7:
            a = "seven"
        if a == 8:
            a = "eight"
        if a == 9:
            a = "nine"
        if a == 10:
            a = "ten"
        if a == 11:
            a = "jack"
        if a == 12:
            a = "queen"
        if a == 13:
            a = "king"
        if a == 14:
            a = "ace"
        # suit
        if b == 1:
            b = "clubs"
        if b == 2:
            b = "diamonds"
        if b == 3:
            b = "hearts"
        if b == 4:
            b = "spades"
        return "Player 2 draws the "+a+" of "+b+"."

    p1pts = 0
    p2pts = 0
    while p1pts < 10 and p2pts < 10:
        cards = drawcard()
        print(p1printcards(cards[0],cards[2]))
        print(p2printcards(cards[1],cards[3]))
        if cards[0] == cards[1] and cards[0] == 7:
            print("Two sevens! Both players reset to one point!")
            p1pts = 1
            p2pts = 1
        if cards[0] == 4 and cards[2] == 1 and cards[1] == 4 and cards[3] == 1:
            print("Two fours of clubs! Both players lose all their points!")
            p1pts = 0
            p2pts = 0
        else:
            if cards[0] == 4 and cards[2] == 1:
                print("Four of clubs! Player 1 loses all their points!")
                p1pts = 0
            elif cards[1] == 4 and cards[3] == 1:
                print("Four of clubs! Player 2 loses all their points!")
                p2pts = 0
            elif cards[0] == 7:
                print("Seven! Player 1 earns one point while Player 2 loses all their points!")
                p1pts += 1
                p2pts = 0
            elif cards[1] == 7:
                print("Seven! Player 1 earns one point while Player 2 loses all their points!")
                p2pts += 1
                p1pts = 0
            else:
                if cards[0] > cards[1]:
                    print("Player 1 wins this round.")
                    p1pts += 1
                if cards[1] > cards[0]:
                    print("Player 2 wins this round.")
                    p2pts += 1
                if cards[0] == cards[1]:
                    if cards[2] > cards[3]:
                        print("Player 1 wins this round.")
                        p1pts += 1
                    if cards[3] > cards[2]:
                        print("Player 2 wins this round.")
                        p2pts += 1
                    if cards[2] == cards[3]:
                        print("Tie; both players lose one point.")
                        p1pts -= 1
                        p2pts -= 1
        print("P1 pts:",p1pts,"--- P2 pts:",p2pts)
    if p1pts == 10:
        print("Congratulations, Player 1 wins!")
        print("♪┏(・o･)┛♪┗ (･o･ )┓♪")
    if p2pts == 10:
        print("Congratulations, Player 2 wins!")
        print("♪┏(・o･)┛♪┗ (･o･ )┓♪")

main()
"""

# work problems:



#biglist = []
#for i in range (3):
#    for j in range (3):
#        newlist = []
#        newlist.append(0)
#    biglist.append(newlist)
#print(biglist)
#
#def factors():
#    inputnum = int(input("Number: "))
#    factorlist = []
#   for i in range (inputnum):
#        if inputnum % i == 0:
#            factorlist.append(inputnum)
#    print(factorlist)
#
#myList = [1,4,5,5,6,7,12]
# print the second half
#half = len(myList)/2
#print(myList[int(half):])
# print every third element
#print(myList[0 :-1,3])

#???????????