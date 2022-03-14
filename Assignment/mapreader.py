#!/usr/bin/env python3

'''

CE866 - Assignment 1

Registration Number - 2100972
The following script presents the assignment 1 for Computer Vision module.

'''
import cv2, sys, numpy
#-------------------------------------------------------------------------------
# Main program.

# Ensure we were invoked with a single argument.
try:
    if len (sys.argv) != 2:
        print ("Usage: %s <image-file>" % sys.argv[0], file=sys.stderr)
        exit (1)

    print ("The filename to work on is %s." % sys.argv[1])
    xpos = 0.5
    ypos = 0.5
    hdg = 45.1


    # Output the position and bearing in the form required by the test harness.
    print ("POSITION %.3f %.3f" % (xpos, ypos))
    print ("BEARING %.1f" % hdg)

except:
    if len (sys.argv) != 2:
        print("The program was invoked incorrectly. \n")
        print(" The program requires an argument and should be involked in the following way. \n")
        print("         python3 maapreader.py image.png")
#-------------------------------------------------------------------------------

# Segment the map from the blue background in the original image and extract it into a separate image
# in a way that makes the map edges match those of the extracted image.

def mainRun():
    threshold = 100
    mask_size = 9

