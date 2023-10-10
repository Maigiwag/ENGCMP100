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
The cost of the Engineering program is ${format(engFinalTuit, '.2f')}
''')


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


