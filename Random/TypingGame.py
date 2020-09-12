#!/usr/bin/env python3

def round(speed,text,result):
#speed~typingSpeed #text~typingText #result~result

        #getting the player ready
        uselessVariable = input("Below are some quotes from a TV Show.\nHit the keys right and you get the flag.\nYou only have {} seconds max for each quote to give your shot.\nIf you score 5 points, you win.\n   you lose twice, you're out.\n   you are lucky, you win in the first 5 tries\nElse, have a Good Luck.\nHit Enter when READY.\n".format(speed))

        #starting the timer
        beginTime = default_timer()

        #Text to be typed
        playerInput = input("{}\n".format(text)) #\n to avoid side-by-side typing

        #stopping the timer after enter is pressed
        endTime = default_timer()
        totalTime = endTime - beginTime

        #scores
        if totalTime <=speed and playerInput == text:
                print("\nGood Going! A few more to go.")
                result[0] = result[0] + 1

        else:
                print("You need a lot of practice.\n")
                result[1] = result[1] + 1

        #final Output
        return result

#### Main fn from here.
from timeit import default_timer
import random #random library to generate random numbers

#scoreboard
result = [0,0]

list = ['We are Fun Society.', 'Your privacy has been deleted.', 'You hack people, I hack time.', 'The 1% Of The 1%', 'Are you a 1 or a Zero?', 'When we lose, we invite chaos.', 'We live in a kingdom of bullshit.', 'Annihilation is always the answer.'] #text to be typed

#game loop
while True:
        if result[0] == 5 or result[1] == 2:
                if result[0] ==  5:
                        print("Good Job Kiddo!")
                        print("Here you go:\nflag{f4st_typ1ng_1s_th3_k3y}")
                if result[1] == 2:
                        print("Shoooo away Kiddo!\nYou lost.")
                break
        else:
                typingSpeed = random.randint(8,9) #time enter the texts
                a = random.randint(0,7)
                typingText = list[a] #copying the random int a from the list

                result = round(typingSpeed, typingText, result) #function calling the game round
                print("Points Won: {}".format(result[0]))
                print("Points Lost: {}\n".format(result[1]))
