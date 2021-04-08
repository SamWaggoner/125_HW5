# File: hw5b.py
# Author: Sam Waggoner
# Date: 10/22/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Create palindromes with the smallest number of characters possible.
# Collaboration:
# I worked by myself.

# Pseudocode I made before writing the code:

# start
# get input for string, check it doesn't equal quit
# call palindrome function:
# for each length of string, <10, check if it is a palindrome
# if it's a palindrome, then return the original string
# if it's not a palindrome,
# find if there are repeating chars at the end of it, return correct palindrome
# find if the characters wrap back on themselves, return correct palindrome
# ^(this happens around every letter starting from -1 to the letter before the middle)
# repeat function until string is quit
# end
import string
def main():

    def palendromize():
        if len(string) == 1:
            return string
        if len(string) == 2:
            if string[0] == string[-1]:
                return string
            # if no wraps or repeats at end
            else:
                return string+string[0]
        if len(string) == 3:
            if string[0] == string[-1]:
                return string
            if string[1] ==string[-1]:
                return string+string[0]
            # if no wraps or repeats at end
            else:
                return string+string[1]+string[0]
        if len(string) == 4:
            # repeats
            if string[0] == string[-1] and string[1] == string[-2]:
                return string
            if string[1] == string[2] == string[3]:
                return string+string[0]
            if string[2] == string[3]:
                return string+string[1]+string[0]
            # wraps
            if string[-3] == string[-1]:
                return string+string[0]
            # if no wraps or repeats at end
            else:
                return string+string[2]+string[1]+string[0]
        if len(string) == 5:
            # repeats
            if string[0] == string[-1] and string[1] == string[-2]:
                return string
            if string[1] == string[2] == string[3] == string[4]:
                return string+string[0]
            if string[2] == string[3] == string[4]:
                return string+string[1]+string[0]
            if string[3] == string[4]:
                return string+string[2]+string[1]+string[0]
            # wraps
            if string[-1] == string[-3]:
                return string+string[1]+string[0]
            # if no wraps or repeats at end
            else:
                return string+string[3]+string[2]+string[1]+string[0]
        if len(string) == 6:
            # repeats
            if string[0] == string[-1] and string[1] == string[-2] and string[2] == string[-3]:
                return string
            if string[1] == string[2] == string[3] == string[4] == string[5]:
                return string+string[0]
            if string[2] == string[3] == string[4] == string[5]:
                return string+string[1]+string[0]
            if string[3] == string[4] == string[5]:
                return string+string[2]+string[1]+string[0]
            if string[4] == string[5]:
                return string+string[3]+string[2]+string[1]+string[0]
            # wraps
            if string[-1] == string[-3]:
                return string+string[2]+string[1]+string[0]
            if string[-4] == string[-2] and string[-1] == string[-5]:
                return string+string[0]
            # if no wraps or repeats at end
            else:
                return string+string[4]+string[3]+string[2]+string[1]+string[0]
        if len(string) == 7:
            # repeats
            if string[0] == string[-1] and string[1] == string[-2] and string[2] == string[-3]:
                return string
            if string[1] == string[2] == string[3] == string[4] == string[5] == string[6]:
                return string+string[0]
            if string[2] == string[3] == string[4] == string[5] == string[6]:
                return string+string[1]+string[0]
            if string[3] == string[4] == string[5] == string[6]:
                return string+string[2]+string[1]+string[0]
            if string[4] == string[5] == string[6]:
                return string+string[3]+string[2]+string[1]+string[0]
            if string[5] == string[6]:
                return string+string[4]+string[3]+string[2]+string[1]+string[0]
            # wraps
            if string[-1] == string[-3]:
                return string+string[3]+string[2]+string[1]+string[0]
            if string[-4] == string[-2] and string[-1] == string[-5]:
                return string+string[2]+string[1]+string[0]
            # if no wraps or repeats at end
            else:
                return string+string[5]+string[4]+string[3]+string[2]+string[1]+string[0]
        if len(string) == 8:
            # repeats
            if string[0] == string[-1] and string[1] == string[-2] and string[2] == string[-3] and string[3] == string[-4]:
                return string
            if string[1] == string[2] == string[3] == string[4] == string[5] == string[6] == string[7]:
                return string+string[0]
            if string[2] == string[3] == string[4] == string[5] == string[6] == string[7]:
                return string+string[1]+string[0]
            if string[3] == string[4] == string[5] == string[6] == string[7]:
                return string+string[2]+string[1]+string[0]
            if string[4] == string[5] == string[6] == string[7]:
                return string+string[3]+string[2]+string[1]+string[0]
            if string[5] == string[6] == string[7]:
                return string+string[4]+string[3]+string[2]+string[1]+string[0]
            if string[6] == string[7]:
                return string+string[5]+string[4]+string[3]+string[2]+string[1]+string[0]
            # wraps
            if string[-1] == string[-3]:
                return string+string[4]+string[3]+string[2]+string[1]+string[0]
            if string[-4] == string[-2] and string[-1] == string[-5]:
                return string+string[2]+string[1]+string[0]
            if string[-6] == string[-2] and string[-1] == string[-7] and string[-5] == string[-3]:
                return string+string[0]
            # if no wraps or repeats at end
            else:
                return string+string[6]+string[5]+string[4]+string[3]+string[2]+string[1]+string[0]
        if len(string) == 9:
            # repeats
            if string[0] == string[-1] and string[1] == string[-2] and string[2] == string[-3] and string[3] == string[-4]:
                return string
            if string[1] == string[2] == string[3] == string[4] == string[5] == string[6] == string[7] == string[8]:
                return string+string[0]
            if string[2] == string[3] == string[4] == string[5] == string[6] == string[7] == string[8]:
                return string+string[1]+string[0]
            if string[3] == string[4] == string[5] == string[6] == string[7] == string[8]:
                return string+string[2]+string[1]+string[0]
            if string[4] == string[5] == string[6] == string[7] == string[8]:
                return string+string[3]+string[2]+string[1]+string[0]
            if string[5] == string[6] == string[7] == string[8]:
                return string+string[4]+string[3]+string[2]+string[1]+string[0]
            if string[6] == string[7] == string[8]:
                return string+string[5]+string[4]+string[3]+string[2]+string[1]+string[0]
            if string[7] == string[8]:
                return string+string[6]+string[5]+string[4]+string[3]+string[2]+string[1]+string[0]
            if string[-1] == string[-3]:
                return string+string[4]+string[3]+string[2]+string[1]+string[0]
            if string[-4] == string[-2] and string[-1] == string[-5]:
                return string+string[2]+string[1]+string[0]
            # wraps
            if string[-1] == string[-3]:
                return string+string[5]+string[4]+string[3]+string[2]+string[1]+string[0]
            if string[-4] == string[-2] and string[-1] == string[-5]:
                return string+string[3]+string[2]+string[1]+string[0]
            if string[-6] == string[-2] and string[-1] == string[-7] and string[-5] == string[-3]:
                return string+string[1]+string[0]
            # if no wraps or repeats at end
            else:
                return string+string[7]+string[6]+string[5]+string[4]+string[3]+string[2]+string[1]+string[0]
            

    string = input("String that you would like to palindromize (fewer than 10 \
characters, type quit to end the program): ")
    if string != "quit":
        result = palendromize()
        print(result.lower())
    while string != "quit":
        string = input("String that you would like to palindromize: ")
        if string != "quit":
            result = palendromize()
            print(result.lower())

main()