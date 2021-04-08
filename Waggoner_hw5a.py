# File: hw5a.py
# Author: Sam Waggoner
# Date: 10/22/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Write a program to generate random poitical slogans.
# Collaboration:
# I went to VJ's office hours to find out how to get rid of get rid of the 
# parentheses and quotation in my print statement. (He suggested using concatenation
# instead of commas.)

import random

def main():
    names = ("Hulk", "Spock", "Daenerys", "Aaron Burr", "The Cowardly Lion", "Cinderella", \
        "Black Panther", "Merida", "Uhuru", "Freya", "Frodo")
    verbs = ("Leading", "Serving", "Building", "Creating", "Putting", "Fighting", "Taking", \
        "Cleaning up", "Protecting", "Putting", "Smashing", "Working", "Incinerating")
    direct_objects = ("the future", "our community", "jobs", "education", "corruption", \
        "action", "families", "change", "progress", "government", "results", "our enemies")
    adverb_phrases = ("with integrity", "for you", "first", "safe", "for the future", \
        "for a change", "for Maine", "with experience", "with vision")

    def make_slogan():

        numnames = random.randint(0,(len(names))-1)
        name = names[numnames]
        numverbs = random.randint(0,(len(verbs))-1)
        verb = verbs[numverbs]
        numdirect_objects = random.randint(0,(len(direct_objects))-1)
        direct_object = direct_objects[numdirect_objects]
        numadverb_phrases = random.randint(0,(len(adverb_phrases))-1)
        adverb_phrase = adverb_phrases[numadverb_phrases]
        catchphrase = name+":"+" "+verb+" "+direct_object+" "+adverb_phrase
        return catchphrase

    for i in range(int(input("How many slogans would you like? "))):
        print(make_slogan())

main()