# main.py runs the game.
import cv2
import numpy as np
import sys
import requests

VIDEO_FEED_ERR = "Video feed not working. Exiting..."
url = "http://localhost:5000/"


# def video_feed_ok():
#     pass


def play_game():
    pass


def main(args):

    # connect to the phones camera
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    imgOriginalScene = cv2.imdecode(img_arr, -1)

    cv2.imshow("IPcamera", imgOriginalScene)
    cv2.namedWindow('IPcamera', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('IPcamera', 300, 300)
    # import the model

    # play the game

    # display the winner

    sys.exit()
