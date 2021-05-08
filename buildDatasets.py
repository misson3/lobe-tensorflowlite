# May09, 2021, ms
# buildDatasets.py

# history
# 1 build_face_dataset.py from Adrian Rosebrock's page, ref (0)
# 2 build_dataset.py: my prototyping code

# USAGE
# python3 buildDatasets.py --output <path to dir>

'''
refs
(0) https://www.pyimagesearch.com/2018/06/11/\
    how-to-build-a-custom-face-recognition-dataset/
(1) cv2.waitKey(): https://stackoverflow.com/questions/51143458/\
    difference-in-output-with-waitkey0-and-waitkey1/51143586
'''

from imutils.video import VideoStream
import argparse
import cv2
import imutils
import os
import time

# argument parsing
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
                help="path to output directory")
args = vars(ap.parse_args())
# print(type(args))  # <class 'dict'>
# print(type(ap.parse_args()))  # <class 'argparse.Namespace'>

# initialize the video stream, allow the camera sensor to warm up,
# and initialize the total number of example faces written to disk
# thus far
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
total = 0

# loop over the frames from the video stream
while True:
    frame = vs.read()  # 640 x 480
    orig = frame.copy()  # orig will be saved when k is pressed
    frame = imutils.resize(frame, width=400)  # to display

    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF  # learn what this line is doing.  see ref (1)

    # if the `k` key was pressed, write the *original* frame to disk
    if key == ord("k"):
        p = os.path.sep.join([args["output"], "{}.png".format(
            str(total).zfill(5))])
        cv2.imwrite(p, orig)
        total += 1

    # if the `q` key was pressed, break from the loop
    elif key == ord("q"):
        break

# do a bit of cleanup
print("[INFO] {} images stored".format(total))
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop()
