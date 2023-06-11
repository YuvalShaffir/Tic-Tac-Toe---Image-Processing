# main.py runs the game.
import cv2
import numpy as np
import sys
import requests
import imutils


VIDEO_FEED_ERR = "Video feed not working. Exiting..."
url = "http://10.10.1.152:8080/shot.jpg"


# def video_feed_ok():
#     pass


def play_game():
    pass


def main(args):

    # connect to the phone's camera
    # While loop to continuously fetching data from the Url
    while True:
        try:
            img_resp = requests.get(url)
            # Process the response if the connection is successful
            print(img_resp.status_code)
        except requests.ConnectionError:
            # Handle connection-related errors
            raise Exception("A connection error occurred.")
        except requests.Timeout:
            # Handle timeout error
            raise Exception("The request timed out.")
        except requests.TooManyRedirects:
            # Handle too many redirects error
            raise Exception("Too many redirects occurred.")
        except requests.RequestException:
            # Handle other request-related errors
            raise Exception("An error occurred during the request.")
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        img = imutils.resize(img, width=1000, height=1800)
        cv2.imshow("Phone Camera - (Press Esc to exit)", img)

        # Press Esc key to exit
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()

    # import the model

    # play the game

    # display the winner

    sys.exit()


if __name__ == '__main__':
    main(sys.argv)