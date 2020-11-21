"""
Execute application as follows :
    python main.py input_img.jpg (or) python main.py input_video.mp4 (or) python main.py
"""

import sys
from EmotionRecognition import emotion_detector
from ActivityDetectionFrontend import *

# input_name = ""
# if len(sys.argv) == 2:
#     input_name = sys.argv[1]
# # when image/video name is not passed as a command line argument
# else:
#     input_name = input("Enter name of image/video :")

def main(input_name):
	emotion_detector(input_name)
	result = activity_detector(input_name)
	image = Image.open('emotion.png')
	color = 'rgb(255,20,147)'
	_,w,_ = cv2.imread('emotion.png').shape
	(x, y) = (w//2-1, 0)
	# change the font supported in your system
	font = ImageFont.truetype('Comic Sans MS', size=45)
	draw = ImageDraw.Draw(image)
	draw.text((x, y), result, fill=color, font=font)
	image.save('emotion-activity.png')

# if '.mp4' in input_name:
#     activity_detector_video(input_name)
# else:
#     activity_detector(input_name)
