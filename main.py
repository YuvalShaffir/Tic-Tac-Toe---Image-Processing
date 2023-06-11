# main.py runs the game.
import cv2
import numpy as np
import sys
import requests
import imutils

# Constants
ESC_BOTTON = 27

# Error messages
VIDEO_READ_ERR = "Failed to read video frame"
VIDEO_CAPTURE_ERR = "Failed to open video capture"

# GUI messages
WINDOW_TITLE = "Phone Camera - (Press Esc to exit)"
WINNER_MESSAGE = "The winner is: "

# URL to connect to the phone's camera using the app "IP Webcam"
URL = "http://10.10.1.152:8080/shot.jpg"



def play_game(img_resp):
    """Manages the game play."""

    while True:
        # Capture the video frame by frame and show it to the user
        ret, frame = img_resp.read()
        if not ret:
            raise AttributeError(VIDEO_READ_ERR)

        frame = imutils.resize(frame, width=1000, height=1800)
        cv2.imshow( WINDOW_TITLE, frame )


        # Press Esc key to exit
        if cv2.waitKey(1) == ESC_BOTTON:
            break


def main(args):
    # import the model

    # connect to the phone's camera
    # While loop to continuously fetching data from the Url
    img_resp = cv2.VideoCapture(URL)
    if not vid.isOpened():
        raise OSError(VIDEO_CAPTURE_ERR)

    # display the winner
    result = play_game(img_resp)
    print(WINNER_MESSAGE, result)

    img_resp.release()
    cv2.destroyAllWindows()
    sys.exit()


if __name__ == '__main__':
    main(sys.argv)