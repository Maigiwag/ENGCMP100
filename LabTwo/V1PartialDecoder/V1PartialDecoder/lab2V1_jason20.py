# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: jason wang (100%)
# Student CCID: jason20
# Others: all code is my own 
#
# To avoid plagiarism, list the names of persons, Version 0 author(s)
# excluded, whose code, words, ideas, or data you used. To avoid
# cheating, list the names of persons, excluding the ENCMP 100 lab
# instructor and TAs, who gave you compositional assistance.
#
# After each name, including your own name, enter in parentheses an
# estimate of the person's contributions in percent. Without these
# numbers, adding to 100%, follow-up questions may be asked.
#
# For anonymous sources, enter pseudonyms in uppercase, e.g., SAURON,
# followed by percentages as above. Email a link to or a copy of the
# source to the lab instructor before the assignment is due.
#
import numpy as np

print('Version 1')
# ----------Students write/modify their code below here ---------------------

code = input('Please enter a code to break: ')
code = np.array(list(code),dtype=int)
if len(code) == 9: #rule 1 testing if code is 9 digits long
    oddEvenTest = code.sum()
    if oddEvenTest % 2 != 0: #rule 2 testing if code is even or odd
        day = (code[2] * code[1]) - code[0]  #calculating rule 3
        print(f"Day = {day}")  #printing result for rule 3
        place = code[2]**code[1] 
        if place % 3 == 0:                 #calculating for rule 4 if value is diisible by 3
            place = code[5] - code[4]
        else:
            place = code[4] - code[5]
        print(f"Place = {place}") #displaying place
    else:
        print("Decoy Message: Sum is even.")
else: 
    print("Decoy Message: Not a nine-digit number.")