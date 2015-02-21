#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
A program to (re)calculate an image's dimensions
when one of its sides is changed in size.

Copyright (c) 2015 K Kollmann <code∆k.kollmann·moe>
License: http://opensource.org/licenses/MIT The MIT License (MIT)
'''

import math
import sys

# def newdimensions():
#     ''' Calculate new width / height of an image based on
#         its current width and height, and one new value
#         (keeping intact its aspect ratio).
#     '''
#     # prompt for desired new width / height
#     w = input("New w: ")
#     h = input("New h: ")
#     # convert str input to floats
#     if w:
#         w = float(w)
#     if h:
#         h = float(h)

#     # calculate new width or height
#     # depending on which new dimension was provided by the user

#     # print out warning if user provided no values
#     if w == "" and h == "":
#         print("You didn't provide any new values! Please try again.")
#     elif w == "":
#         w = (h * width) / height
#         print("The new width of your image is {}, rounded: {}".format(round(w,2),round(w)))
#     elif h == "":
#         h = (w * height) / width
#         print("The new height of your image is {}, rounded: {}".format(round(h,2),round(h)))
#     # print out warning if user provided both new width and height
#     else:
#         print("You provided two new values instead of one! Please try again.")
#         w = ""
#         h = ""
#     return(w, h)

def calculate_newdimension(w,h):
    ''' Calculate the missing dimension of an image based on its current
        width, height and new measurement for a third dimension.
    '''
    try:
        float(w)
        float(h)
    except:
        try:
            float(w)
        except ValueError as e:
            if w == '':
                return w, h
            else:
                print(e)
        except:
            # some other error
            exctype, value = sys.exc_info()[:2]
            sys.exit((exctype, value))
        try:
            float(h)
        except ValueError as e:
            if h == '':
                return w, h
                pass
            else:
                print(e)
        except:
            # some other error
            exctype, value = sys.exc_info()[:2]
            sys.exit((exctype, value))
        sys.exit("You need to enter valid numbers for calculation new image dimensions...")

    # while True:
    print("Input (only) one new dimension:")
    new_w, new_h = calculate_newdimension(input("new w: "), input("new h: "))
    print("new w: {}, new h: {}" .format(new_w, new_h)) # debug

    # not numbers; calculations based on strings
    eins = 5 * new_w
    zwei = 4 * new_h

    return eins, zwei

if __name__ == "__main__":

    while True:
        print("Current dimensions of your image:")
        new_w, new_h = calculate_newdimension(input("w: "), input("h: "))
        print("new width: {}\nnew height: {}" .format(new_w, new_h))
        break
