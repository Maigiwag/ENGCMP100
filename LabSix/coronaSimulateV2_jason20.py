## CORONASIMULATE  Simulate coronagraph and Gerchberg-Saxton algorithm
#
# A simulation of a coronagraph and the Gerchberg-Saxton algorithm, in the
# context of NASA's Roman Space Telescope, developed to help teach ENCMP
# 100 Computer Programming for Engineers at the University of Alberta. The
# program saves output figures to PNG files for subsequent processing.
#
# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Jason Wang (90%)
# Student CCID: jason20
# Others: farhan (5%) vincent (5%)
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
import matplotlib.pyplot as plt
import numpy as np

def main():
    im = loadImage('300_26a_big-vlt-s.jpg')
    (im,Dphi), mask = opticalSystem(im,300)
    images,errors = gerchbergSaxton(im,10,Dphi,mask)
    saveFrames(images, errors)

#loads the image into a format that is able to be manipulated with code
#input: name: filename
# no outputs
def loadImage(name):
    im = plt.imread(name)/255
    if len(im.shape) > 2:
        im = (im[:,:,0]+im[:,:,1]+im[:,:,2])/3
    im[im < 0] = 0
    im[im > 1] = 1
    return im

#takes parameters and invokes other functions in order to generate the image as well as pass on data used to graph the image and error
#input: im: list, width: int
#output: (im,Dphi): tuple of lists , mask:array
def opticalSystem(im,width):
    im,mask = occultCircle(im,width)
    (IMa,IMp) = dft2(im)
    rng = np.random.default_rng(12345)
    imR = rng.random(im.shape)
    (_,Dphi) = dft2(imR)
    im = idft2(IMa,IMp-Dphi)
    return (im,Dphi), mask

#makes the input black and then returns that with the dimensions of a circle
#input: im: list, width: int
#output: im: list, mask: array
def occultCircle(im,width):
    x = int(len(im)/2)
    y = int(len(im[0])/2)
    mid = [x,y]
    mask = np.full((len(im),len(im[0])),False,dtype='bool')
    for i in range(0,len(im)):
        for r in range(0,len(im[0])):
            try:
                if np.sqrt((i-mid[0])**2+(r-mid[1])**2) <= width/2:
                    im[i][r] = 0
                    mask[i][r] = True
            except:
                pass
    return im, mask


# (IMa,IMp) = dft2(im) returns the amplitude, IMa, and phase, IMp, of the
# 2D discrete Fourier transform of a grayscale image, im. The image, a 2D
# array, must have entries between 0 and 1. The phase is in radians.
def dft2(im):
    IM = np.fft.rfft2(im)
    IMa = np.abs(IM)
    IMp = np.angle(IM)
    return (IMa,IMp)

# im = idft2(IMa,IMp) returns a grayscale image, im, with entries between
# 0 and 1 that is the inverse 2D discrete Fourier transform (DFT) of a 2D
# DFT specified by its amplitude, IMa, and phase, IMp, in radians.
def idft2(IMa,IMp):
    IM = IMa*(np.cos(IMp)+1j*np.sin(IMp))
    im = np.fft.irfft2(IM)
    im[im < 0] = 0
    im[im > 1] = 1
    return im

#this functions will take the image and specfic parameters to then create a set of images that have been refined
#inputs: im: list, maxIters: int, Dphi: list, mask:array
#outputs: images: list, error: list
#also prints out text in the console to let the user know which iteration is being computed
def gerchbergSaxton(im,maxIters,Dphi,mask):
    (IMa,IMp) = dft2(im)
    images = []
    error = []
    for k in range(maxIters+1):
        print("Iteration %d of %d" % (k,maxIters))
        im = idft2(IMa,IMp +((Dphi*k)/maxIters))
        images.append(im)
        error.append(occultError(im,mask))
    return images, error

#after the images have been processed this will save the images into the root folder
#inputs: images: list, error: list
#outputs: none
#will save and display the graphs made by matplotlib into the root folder for viewing. 
def saveFrames(images,error):
    shape = (images[0].shape[0],images[0].shape[1],3)
    image = np.zeros(shape,images[0].dtype)
    maxIters = len(images)-1
    maxError = max(error)
    yVal = []
    ax = plt.gca()
    for k in range(maxIters+1):
        image[:,:,0] = images[k]
        image[:,:,1] = images[k]
        image[:,:,2] = images[k]
        yVal.append(error[k])
        plt.imshow(image)
        plt.title('Cornograph Simulation')
        plt.plot(range(k+1),yVal,color='red')
        plt.ylim(0,maxError)
        ax.xaxis.set_tick_params(labelbottom=False)
        ax.yaxis.set_tick_params(labelleft=False)
        plt.xlabel('Iteration')
        plt.ylabel('Sum Square Error')
        plt.imshow(image,extent=(0,10,0,maxError))
        plt.gca().set_aspect(maxIters/maxError)
        plt.savefig('coronagraph'+str(k)+'.png')
        plt.show()

#calculates the errors used to plot the red error line
#inputs: im: list, mask: array 
#outputs: sum(error): int
def occultError(im,mask):
    error = []
    for i in range(0,len(mask)):
        for r in range(0,len(mask[0])):
            if mask[i][r] == True:
                error.append(im[i][r]**2)
    return sum(error)


main()
