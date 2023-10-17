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

#----VARIABLES----#

#creating all the variables needed to do all necessary calculations 

saving = [2000]
artTuit = [5550]
sciTuit = [6150]
engTuit = [6550]
years = np.arange(0,19)
artFinalTuit = 0
sciFinalTuit= 0
engFinalTuit = 0

#---SAVING CALCULATION---#

#This section uses a for loop that will calculate the savings per month for the 18 years
#by repeating this calculation 216 times we are able to calculate the final savings balance after 18 years (216 months)

for i in range(215):
    saving += [(saving[i]+(saving[i]*(0.0625/12)))+200]

#---TUITION CALCULATION---#

#Similar to how saving calculations is done this section loops 22 times to calculate the 
#tution cost for the next 22 years.  

for i in range(21):
    artTuit += [artTuit[i]+(artTuit[i]*0.07)]
    sciTuit += [sciTuit[i]+(sciTuit[i]*0.07)]
    engTuit += [engTuit[i]+(engTuit[i]*0.07)]

#Using the data calculated above this section takes the last 4 calculations and adds them together onto a new variable
# This variable represents the total cost of the program which can be displayed on the graph

for i in range(4):
    i = (i+1)*-1
    
    artFinalTuit += artTuit[i]
    sciFinalTuit += sciTuit[i]
    engFinalTuit += engTuit[i]

#---PRINTING EVERYTHING TO USER---#

#displays all the information calculated above in a nice format to the user

print(f'''The savings amount is ${format(saving[-1], '.2f')}
The cost of the Arts program is ${format(artFinalTuit,'.2f')}
The cost of the Science program is ${format(sciFinalTuit, '.2f')}
The cost of the Engg program is ${format(engFinalTuit, '.2f')}
''')


###---VERSION 2---###
print("Version 2 - Solution")

#---VARIABLES---#

#creation of more variables needed for the verison 2 solution 
monthCont = 0
choice = 0
optiSav = [2000]
programTuit = [artFinalTuit, sciFinalTuit, engFinalTuit]
programName = ["Arts", "Science", "Engineering"]
valid = False
foundOpti = False

#---USER INPUT---#

#A bit of code that makes sure the user has inputted a valid option to then proceed with the optimization

while not valid: 
    if choice < 1 or choice > 3:  #makes sure the user picked a number between 1 and 3 
        try:
            choice = int(input("Enter a program 1.Arts, 2.Science, 3.Engineering : ")) 
        except:
            print("Please enter a valid input") 
    else:
        valid = True 

#---OPTIMIZATION---#

#to optimtize the monthly contribution we run the savings calculation over and over with a changing monthly contribution amount
#When we reach a monthly contribution amount that fufills the tuition requirement it will save that amount and display it to the user

while not foundOpti: 
        if optiSav[-1] <= programTuit[choice-1]: 
            optiSav = [2000] 
            monthCont += 1 #adds one to the monthly contribution and reruns the calculation
            for i in range(215): 
                optiSav += [(optiSav[-1]+(optiSav[-1]*(0.0625/12)))+monthCont] 
                #instead of a monthly contribution of 200 this uses our optimal monthly contribution amount defined earlier
        else:
            foundOpti = True

if saving[-1] >= programTuit[choice-1]: #if the REAL savings amount exceeds or is greater than the tuiton amount
    print(f"Congratulation!!! You have saved enough for the {programName[choice-1]} program")
else: #if the final REAL savings amount is less than the tution amount
    print(f"Unfortunately!!! You do not have enough saved for the {programName[choice-1]} program")
print(f"The optimal monthly contribution amount is ${monthCont}") 


#---PLOT---#

#All this code is used for displaying all the relevant information onto the graph 

fig,ax = plt.subplots()  #this command is used so we are able to plot the tuition onto a single line
ax.plot(saving) 
ax.hlines(artFinalTuit,0 ,216, colors = 'orange')
ax.hlines(sciFinalTuit,0 ,216, colors = 'g') 
ax.hlines(engFinalTuit,0 ,216, colors = 'r') 
plt.title("Savings Vs Tuition") 
plt.axis([0,217,0,100000]) #gets rid of white lines on the side
ax.set(xticks= range(0,217,12), xticklabels=years) #sets the bottom to increase in years instead of months 
plt.xlabel("Years") 
plt.ylabel("Amount $") 
plt.legend(['Savings Balance', 'Arts', 'Science', 'Engineering'], loc = 'lower right') 
plt.show()  


