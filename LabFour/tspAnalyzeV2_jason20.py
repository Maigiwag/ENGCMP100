## TSPANALYZE  Geomatics and the Travelling Sales[person] Problem
#
# According to the ISO/TC 211, geomatics is the "discipline concerned
# with the collection, distribution, storage, analysis, processing, [and]
# presentation of geographic data or geographic information." Geomatics
# is associated with the travelling salesman problem (TSP), a fundamental
# computing problem. In this lab assignment, a University of Alberta
# student completes a Python program to analyze, process, and present
# entries, stored in a binary data file, of the TSPLIB, a database
# collected and distributed by the University of Heidelberg.
#
# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: jason wang (99%) 
# Student CCID: jason 20
# Others: vincent(1%)
#   MatPlotLib Documentation was also referenced
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

##---VERSION TWO---##

import scipy.io as io
import numpy as np
import matplotlib.pyplot as plt


def main():
    tsp = io.loadmat('tspData.mat',squeeze_me=True)
    tsp = np.ndarray.tolist(tsp['tsp'])
    file = open('tspAbout.txt','r')
    print(file.read())
    file.close()
    choice = menu() 
    while choice != 0:
        if choice == 1:
            tspPrint(tsp)
        elif choice == 2:
            minVal,maxVal = tspMinMax(tsp)
            tsp = tspLimit(tsp,minVal,maxVal)
        elif choice == 3:
            tspPlot(tsp)

        choice = menu()


# Menu function displays all the necessary input information to the user 
# [INPUT] N/A 
# [RETURN] choice = INT 
# SIDE EFFECTS: prints the menu for the user to interact with 
def menu():
        numError = True
        print()
        print("MAIN MENU")
        print("0. Exit program")
        print("1. Print database")
        print("2. Limit dimension")
        print("3. Plot one tour")
        print()
        while numError == True or choice < 0 or choice > 3: 
            choice = input("Choice (0-3)? ")
            choice,numError = checkInt(choice)
        return choice

#this funciton will display all avaliable datasets to attempt to create a plot with
# [INPUT] tsp = LIST 
# [RETURN] N/A 
# SIDE EFFECTS: prints all the data in "tsp"
def tspPrint(tsp):
    print()
    print("NUM  FILE NAME  EDGE TYPE  DIMENSION  COMMENT")
    for k in range(1,len(tsp)):
        name = tsp[k][0]
        edge = tsp[k][5]
        dimension = tsp[k][3]
        comment = tsp[k][2]
        print("%3d  %-9.9s  %-9.9s  %9d  %s"
            % (k,name,edge,dimension,comment))

#asks the user for a specific dataset to attempt to create a plot for 
# [INPUT] tsp = LIST
# [RETURN] N/A
# SIDE EFFECTS: If the user input is a valid data set it will pass the correct info to "PlotEuc2D"
def tspPlot(tsp):
        numError = True
        while numError == True or num < 1 or num > (len(tsp)-1):
            num = input("Number (EUC_2D)? ")
            num,numError = checkInt(num)
        edge = tsp[num][5]
        tsp1 = tsp[num]
        if edge == 'EUC_2D':
            plotEuc2D(tsp1[10],tsp1[2],tsp1[0])
            print("See tspPlot.png")
        else:
            print("Invalid (%s)!!!" % edge)

#plots the given information using matplotlib and then stores the plot as a png
# [INPUT] coord = LIST , comment = Str , name = Str
# [RETURN] N/A 
# SIDE EFFECTS: After drawing the graph in matplotlib it will save it as a png for viewing
def plotEuc2D(coord, comment, name):
    xPlot = []
    yPlot = []
    for i in range(len(coord)):
        xPlot += [coord[i][0]]
        yPlot += [coord[i][1]]
    plt.plot(xPlot,yPlot,'o-', ms=3)
    plt.plot([xPlot[0],xPlot[-1]],[yPlot[0],yPlot[-1]], 'r-')
    plt.title(comment)
    plt.xlabel("x-Cordinate")
    plt.ylabel("y-Cordinate")
    plt.legend([name])
    plt.savefig('tspPlot.png')
    plt.clf()

# Calculates the minimum and maximum values of the TSP data set
# [INPUT] tsp = LIST
# [RETURN] minVal = INT, maxVal = INT 
# SIDE EFFECTS: it will also display the MINIMUM and MAXIMUM values to the user
def tspMinMax(tsp):
    minVal = int(tsp[1][3])
    maxVal = int(tsp[1][3])
    for i in range(1,len(tsp)):
        val = int(tsp[i][3])
        if val > maxVal:
            maxVal = val
        elif val < minVal:
            minVal = val 
    print(f'''Min dimension: {minVal}
Max dimension: {maxVal}''')   
    return minVal,maxVal

# Asks the user for a number to limit the data set to and then modifys TSP to that limit
# [INPUT] tsp = LIST , minVal = INT , maxVal = INT 
# [RETURN] newtsp = LIST 
# SIDE EFFECTS: based on the user input it will bound the TSP data to the LIMIT value and then set TSP to the limited TSP 
def tspLimit(tsp,minVal,maxVal):
    newtsp = [tsp[0]]
    numError = True
    while numError == True or limit < minVal or limit > maxVal:
        limit = input("Limit value? ")
        limit,numError = checkInt(limit)
    maxVal = limit
    for k in range(1,len(tsp)):
        val = int(tsp[k][3])
        if val <= maxVal:
            newtsp.append(tsp[k])
    return newtsp


#this funciton will check if a input is a valid integer so that the program will not crash
#[INPUT] num = anything
#[RETURN] num = INT,  error = BOOL 
# *will only return int IF the INPUT was able to be int()
def checkInt(num):
    try:
        num = int(num)
        error = False
    except:
        error = True
    return num,error
            


main()