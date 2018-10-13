#!/usr/bin/env
'''
  _____            _
 |_   _|___ __  __| |_   _ __  ___ __   __ ___  _ __  ___   ___   _ __
   | | / _ \\ \/ /| __| | '__|/ _ \\ \ / // _ \| '__|/ __| / _ \ | '__|
   | ||  __/ >  < | |_  | |  |  __/ \ V /|  __/| |   \__ \| (_) || |
   |_| \___|/_/\_\ \__| |_|   \___|  \_/  \___||_|   |___/ \___/ |_|

'''

#Aquire user input and return it
def UserInput():
    while(True):
        try:
            usrText = input("Enter text you want to reverse: ")
            #raise Exception('Just testing..')#I was just testing how program behave if I raise exception here
            return usrText
        except:
            print("Unhandled exception")
            print("Try again:")

#Reverse text in parameter and return it
def Reversator(usrText):
    reversedText = usrText[::-1]#Beginning, end, step -> slicing operator -> it's like while cycle backwards
    return reversedText

#Display original and reverse text from parameters
def OutputDisplayer(usrText, reversedText):
    print("Original text: " + usrText)
    print("Reversed text: " + reversedText)

#Includes whole program
def Program():
    usrText = UserInput()
    reversedText = Reversator(usrText)
    OutputDisplayer(usrText, reversedText)

Program()

