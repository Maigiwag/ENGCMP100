## HSPECTRUM  Quantum Chemistry and the Hydrogen Emission Spectrum
#
# The periodic table is central to chemistry. According to Britannica,
# "Detailed understanding of the periodic system has developed along with
# the quantum theory of spectra and the electronic structure of atoms,
# beginning with the work of Bohr in 1913." In this lab assignment, a
# University of Alberta student explores the Bohr model's accuracy in
# predicting the hydrogen emission spectrum, using observed wavelengths
# from a US National Institute of Standards and Technology database.
#
# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Jason Wang (100%)
# Student CCID: jason20 - 1802598
# Others: 
#       All code is mine however i refered to the given examples 
# futhermore i also refered to online documentation of MatPlotLib for how specific functions worked
#
# To avoid plagiarism, list the names of persons, Version 0 author(s)
# excluded, whose code, words, ideas, or data you used. To avoid
# cheating, list the names of persons, excluding the ENCMP 100 lab
# instructor and TAs, who gave you compositional assistance.
#
# After each name, including your own name, enter in parentheses an
# estimate of the person's contributions in percent. Without these
# numbers, adding to 100%, follow-up questions will be asked.
#
# For anonymous sources, enter pseudonyms in uppercase, e.g., SAURON,
# followed by percentages as above. Email a link to or a copy of the
# source to the lab instructor before the assignment is due.
#
import numpy as np
import matplotlib.pyplot as plt


## MODEL SETUP
##sets up all variables needed to do calculations and find the values of everything for the graph
elecMass = 9.1093837e-31 #kg
protMass = 1.67262192e-27 #kg
fundCharge = 1.6021766e-19 #C
permOfSpace =  8.8541878e-12 #m^-3 kg^-1 s^4 A^2
planck = 6.6260702e-34 #Joule seconds
SOL =  2.9979246e8 #m/s
rydberg = (elecMass*(fundCharge**4))/(8*(permOfSpace**2)*(planck**3)*SOL)
rydberg = rydberg * (protMass/(protMass+elecMass))
rydberg = int(rydberg)
print(f"Rydberg Constant: {rydberg}", "m"+chr(8315)+chr(185)) #this now displays meter to the power to negative one

## SIMULATION/EXPERIMENT DATA       
# I combined both simulation and experiement because their both needed to help calculate bohr data
# this way all the relevant data is combined into one section of the code
#
data = [656.460,486.271,434.1692,410.2892,397.1198,389.0166,383.6485] # nm
nist = np.array(data)         #data given by lab
n = len(nist)
nf = input("Final state (nf): ")
nf = int(nf)                  #all this is doing is getting the nf form the user and using that to find ni
ni = np.arange(nf+1,nf+n+1)
waveL = 1/(rydberg*((1/nf**2)-(1/ni**2))) #using data from above to calculate bohr data
waveL = np.divide(waveL, (10**-9)) #making the data from above into nanometers this allows it to be plotted correctly

#this section gathers and calculates data used to then make the graph created in the next section


##ERROR ANALYSIS
#finds difference between nist and bohr and then finds the worst case
dif = nist - waveL
worstCaseScenario = np.max(np.abs(dif))
worstCaseScenario = np.round(worstCaseScenario, decimals=3)
print(f"Worst-case error: {worstCaseScenario} nm")


##Plotting 
plt.bar(ni,dif)
plt.title("Hydrogen Emission Spectrum")
plt.xlabel("Initial state (ni)")
plt.ylabel("Wavelength (nm)")
plt.legend(['NIST - Bohr'])
plt.show()

#i serperated the plotting into its own section because i need nf and ni
# isolated to calcualte bohr data
