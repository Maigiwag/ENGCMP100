## PERIHELION  Mercury's perihelion precession and general relativity
#
# In this lab assignment, a student completes a Python program to test with
# data an accurate prediction of Einstein’s theory, namely the perihelion
# precession of Mercury. Mercury’s orbit around the Sun is not a stationary
# ellipse, as Newton’s theory predicts when there are no other bodies. With
# Einstein’s theory, the relative angle of Mercury’s perihelion (position
# nearest the Sun) varies by about 575.31 arcseconds per century.
#
# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Jason Wang (91%)
# Student CCID: jason20
# Others: farhan(9%) - helped with the refine function 
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
from scipy import stats
import matplotlib.pyplot as plt
import csv
import os

def main():
    data = loaddata('horizons_results')
    data = locate(data) # Perihelia
    data = select(data,25,('Jan','Feb','Mar'))
    data = refine(data, "horizons_results")
    makeplot(data,'horizons_results')
    savedata(data,'horizons_results')

#This functions opens the horizon results data set and then fileters tht data correctly to then be passed onto the main program 
# [INPUTS] filename = FILE 
# [OUTPUTS] data = LIST 
# SIDE EFFECTS: also prints the file name and number of lines ot the user 
def loaddata(filename):
    file = open(filename+'.txt','r')
    lines = file.readlines()
    file.close()
    noSOE = True
    num = 0
    data = []
    for line in lines:
        if noSOE:
            if line.rstrip() == "$$SOE":
                noSOE = False
        elif line.rstrip() != "$$EOE":
            num = num+1
            if num % 10000 == 0:
                print(filename,":",num,"line(s)")
            datum = str2dict(line)
            data.append(datum) 
        else:
            break # for
    if noSOE:
        print(filename,": no $$SOE line")
    else:
        print(filename,":",num,"line(s)")
    return data

#takes the raw data and then breaks it apart into into a dictionary that is returned 
# [INPUTS] line = STR 
# [OUTPUTS] a dictionary containting: numdate, strdate, coord 
def str2dict(line):
    lineList = line.split(',')
    lineList.pop(5)
    for i in range(4):
        lineList[-i] = float(lineList[-i])
    numdate = lineList[0]
    strdateAD = lineList[1].split(' ')
    strdate = strdateAD[2]
    coord = (lineList[2],lineList[3],lineList[4])
    return {'numdate':numdate,'strdate':strdate,
            'coord':coord}

#using the COORD dictionary in the dataset it processes that data and then returns the processed data 
# [INPUT] data1 = LIST 
# [OUTPUT] data2 = LIST 
def locate(data1):
    dist = [] # Vector lengths
    for datum in data1:
        coord = np.array(datum['coord'])
        dot = np.dot(coord,coord)
        dist.append(np.sqrt(dot))
    data2 = []
    for k in range(1,len(dist)-1):
        if dist[k] < dist[k-1] and dist[k] < dist[k+1]:
            data2.append(data1[k])
    return data2

# filters out all data in the dataset with the parameters of ystep and month and then returns only the data that satisys all conditions
# [INPUT] data = LIST, ystep = INT, month = LIST
# [OUTPUT] newData = LIST 
def select(data,ystep,month):
    newData = [] 
    for i in range(len(data)):
        strData = data[i]["strdate"]
        splitData = strData.split("-")
        splitData[0] = int(splitData[0])
        if splitData[1] in month  and (splitData[0]%ystep) == 0:
             newData.append(data[i])
    return newData

#locates files within this folder and looks for valid files to process, create new data based on this refined data
# [INPUT] data = LIST, filename = str
# [OUTPUT] newData = LIST 
# SIDE EFFECTS: accesses files in the folder this python file is contained within 
def refine(data, filename):
    content = []
    newData = []
    for i in os.listdir(os.getcwd()):  
        if filename in i and ".txt" in i and len(i.split("_")) == 3:
            temp = i.replace('.txt','')
            temp = temp.split('_')[2]
            content.append(temp)
    for i in data:
        if i['strdate'] in content:
            temp = locate(loaddata(filename+'_'+i['strdate']))[0]
            newData.append(temp)
    return newData
        
#creates the plot and saves it as a png 
# [INPUT] data = LIST , filename = str
# [OUTPUT] n/a 
# SIDE EFFECTS: displays and saves graphs as png files 
def makeplot(data,filename):
    (numdate,strdate,arcsec) = precess(data)
    plt.plot(numdate,arcsec,'bo')
    plt.xticks(numdate,strdate,rotation=45)
    add2plot(numdate,arcsec)
    plt.savefig(filename+'.png',bbox_inches='tight')
    plt.show()

# calculates the perihelions based on the inputtted data
# [INPUT] data = LIST 
# [OUTPUT] tuple of LISTS 
def precess(data):
    numdate = []
    strdate = []
    arcsec = []
    v = np.array(data[0]['coord']) # Reference (3D)
    for datum in data:
        u = np.array(datum['coord']) # Perihelion (3D)
        ratio = np.dot(u,v)/np.sqrt(np.dot(u,u)*np.dot(v,v))
        if np.abs(ratio) <= 1:
            angle = 3600*np.degrees(np.arccos(ratio))
            numdate.append(datum['numdate'])
            strdate.append(datum['strdate'])
            arcsec.append(angle)
    return (numdate,strdate,arcsec)

#plots the labels and line of best fit onto the graph 
# [INPUT] numdate = LIST , actual = LIST 
# [OUTPUT] n/a 
def add2plot(numdate,actual):
    r = stats.linregress(numdate,actual)
    bestfit = []
    for k in range(len(numdate)):
        bestfit.append(r[0]*numdate[k]+r[1])
    plt.plot(numdate,bestfit,'b-')
    slope = r[0]*365.25*100
    plt.xlabel("Perihelion date")
    plt.ylabel("Precession (arcsec)")
    plt.title("Slope of best fit line: %.2f arcsec/cent" % slope)
    plt.legend(["Actual data","Best fit line"], loc = 'upper left')

#saves the data used to plot the graph into a CSV file for external viewing 
# [INPUT] data = LIST, filename = str
# [OUTPUT] n/a 
# SIDE EFFECTS: opens a csv file writes new data into that csv file and then saves that file externally 
def savedata(data, filename):
    filename+=".csv"
    with open(filename, 'w') as file:
        headers = ["NUMDATE", "STRDATE", "XCOORD", "YCOORD", "ZCOORD"]
        write = csv.DictWriter(file, fieldnames = headers)
        write.writeheader()
        for i in data:
            tempData = {
                "NUMDATE" : '%.6f' % i['numdate'],
                "STRDATE" : i["strdate"],
                "XCOORD" : '%.6f' % i['coord'][0],
                "YCOORD" : '%.6f' % i['coord'][1],
                "ZCOORD" : '%.6f' % i['coord'][2]
            }
            write.writerow(tempData)
    file.close()




main()
