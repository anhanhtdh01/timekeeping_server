from __future__ import division, print_function, absolute_import
import sys
import os
import time
import cv2
import os
import argparse

def parse_arguments(argv):
    ''' Input parameters. '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="path to image output folder",
                        default="./frames/")
    return parser.parse_args(argv)

args = parse_arguments(sys.argv[1:])

name = input("Nhập tên: ")
id = input("Nhập id: ")

name_folder = name + "_" + str(id)

#Create a folder to save frame
frame_folder = os.path.join(args.output, name_folder)

if not os.path.exists(frame_folder):
    os.makedirs(frame_folder)

cap = cv2.VideoCapture(0)

frames_index = 0
while(cap.isOpened()):
    ret, frame = cap.read()   
    if ret == False:
        break
      
    # Save frame to disk
    cv2.imwrite(os.path.join(frame_folder, name_folder + "_" + str(frames_index) + '.jpg'), frame)
    frames_index += 1

    cv2.imshow('video', frame)
    # Press Q to stop!
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    elif frames_index == 200:
        break


cap.release()
cv2.destroyAllWindows()