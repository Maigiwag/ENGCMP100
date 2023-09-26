# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: jason wang (99%)
# Student CCID: jason20
# Others: farhan zaman (1%)
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

print('Lab 2 - Version 2')
# ----------Students write/modify their code below here ---------------------

#arrays for rules 3 and 4 so that the output is written correctly

Days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
Places = ('bridge', 'library', 'river crossing', 'airport', 'bus terminal', 'hospital', 'railway station')
valid = np.arange(1,8)

code = input('Please enter a code to break: ')
code = np.array(list(code),dtype=int)
#rule 1 - checking if the given code has a length of 9 using the len() function 
if len(code) == 9:

    #rule 2 - finding the sum of everything inside of the code and then determining if it is even or odd
    #by using % 2 we can determine if a number is even by checking if there is a remainder
    oddEvenTest = code.sum()
    if oddEvenTest % 2 != 0:

        #rule 3 - multiplying the third and second term and subtracting by the first
        #then checking if that value lies within the range of 1,7 
        day = (code[2] * code[1]) - code[0]  
        if day in valid:

            #rule 4 - finding the answer of the third term to the power of the second term 
            #then using %3 like for rule 2 we can check if this number is divisible by 3
            place = code[2]**code[1] 
            if place % 3 == 0:                 
               place = code[5] - code[4]
            else:
                place = code[4] - code[5]
            if place in valid:
                #if the code had passed all 4 rules this print funtion will display the place and time 
                print(f"Rescued on {Days[day-1]} at the {Places[place-1]}") 
            
            
            #all error messages that lead to program closing 
            else:
                print("Decoy Message: Invalid rendezvous point.")
        else:
            print("Decoy Message: invalid rescue day.")
    else:
        print("Decoy Message: Sum is even.")
else: 
    print("Decoy Message: Not a nine-digit number.")