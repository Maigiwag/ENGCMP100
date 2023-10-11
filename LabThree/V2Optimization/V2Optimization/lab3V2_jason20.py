# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: jason wang (98%)
# Student CCID: jason20
# Others: Farhan Zaman (2%)
#   MatPlotLib Documentation was also refferecned to create the x axis
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
import matplotlib.pyplot as plt
import numpy as np

print('Version 1 - Solution')
# ------------Students edit/write their code below here--------------------------

#----CREATING ALL VARIABLES----#
Saving = [2000]
artTuit = [5550]
sciTuit = [6150]
engTuit = [6550]
years = np.arange(0,19)
artFinalTuit = 0
sciFinalTuit= 0
engFinalTuit = 0

#---SAVING CALCULATION---#
for i in range(215):
    Saving += [(Saving[i]+(Saving[i]*(0.0625/12)))+200]

#---TUITION CALCULATION---#
for i in range(21):
    artTuit += [artTuit[i]+(artTuit[i]*0.07)]
    sciTuit += [sciTuit[i]+(sciTuit[i]*0.07)]
    engTuit += [engTuit[i]+(engTuit[i]*0.07)]

for i in range(4):
    i = (i+1)*-1
    
    artFinalTuit += artTuit[i]
    sciFinalTuit += sciTuit[i]
    engFinalTuit += engTuit[i]

#---PRINTING EVERYTHING TO USER---#
print(f'''The savings amount is ${format(Saving[-1], '.2f')}
The cost of the Arts program is ${format(artFinalTuit,'.2f')}
The cost of the Science program is ${format(sciFinalTuit, '.2f')}
The cost of the Engg program is ${format(engFinalTuit, '.2f')}
''')


###---VERSION 2---###
print("Version 2 - Solution")

#---VARIABLES---#
monthcont = 0
choice = 0
optiSav = [2000]
valid = False
foundOpti = False

#---USER INPUT---#
while not valid: 
    if choice < 1 or choice > 3:
        try:
            choice = int(input("Enter a program 1.Arts, 2.Science, 3.Engineering : "))
        except:
            print("Please enter a valid input")
    else:
        valid = True

#---OPTIMIZATION---#
if choice == 1:
    while not foundOpti:
        if optiSav[-1] <= artFinalTuit:
            optiSav = [2000]
            monthcont += 1
            for i in range(215):
                optiSav += [(optiSav[-1]+(optiSav[-1]*(0.0625/12)))+monthcont]
        else:
            foundOpti = True
    if Saving[-1] >= artFinalTuit:
        print("Congratulation!!! You have saved enough for the arts program")
    else:
        print("Unfortunately!!! You do not have enough saved for the arts program")
    print(f"The optimal monthly contribution amount is ${monthcont}")
elif choice == 2:
    while not foundOpti:
        if optiSav[-1] <= sciFinalTuit:
            optiSav = [2000]
            monthcont += 1
            for i in range(215):
                optiSav += [(optiSav[-1]+(optiSav[-1]*(0.0625/12)))+monthcont]
        else:
            foundOpti = True
    if Saving[-1] >= sciFinalTuit:
        print("Congratulation!!! You have saved enough for the science program")
    else:
        print("Unfortunately!!! You do not have enough saved for the science program")
    print(f"The optimal monthly contribution amount is ${monthcont}")
else:
    while not foundOpti:
        if optiSav[-1] <= engFinalTuit:
            optiSav = [2000]
            monthcont += 1
            for i in range(215):
                optiSav += [(optiSav[-1]+(optiSav[-1]*(0.0625/12)))+monthcont]
        else:
            foundOpti = True
    if Saving[-1] >= engFinalTuit:
        print("Congratulation!!! You have saved enough for the engineering program")
    else:
        print("Unfortunately!!! You do not have enough saved for the engineering program")
    print(f"The optimal monthly contribution amount is ${monthcont}")



#---PLOT---#
fig,ax = plt.subplots()
ax.plot(Saving)
ax.hlines(artFinalTuit,0 ,216, colors = 'orange')
ax.hlines(sciFinalTuit,0 ,216, colors = 'g')
ax.hlines(engFinalTuit,0 ,216, colors = 'r')
plt.title("Savings Vs Tuition")
plt.axis([0,217,0,100000])
ax.set(xticks= range(0,217,12), xticklabels=years)
plt.xlabel("Years")
plt.ylabel("Amount $")
plt.legend(['Savings Balance', 'Arts', 'Science', 'Engineering'], loc = 'lower right')
plt.show()


