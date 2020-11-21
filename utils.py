"""
Contains common functions used by other code files
"""

import pandas as pd
import cv2

"""
converts the annotations from json to csv format
"""
def json_csv():
    df = pd.read_json('annotations.json')
    df.to_csv('annotations.csv')

"""
used to convert a string to a list of integers
"""
def str_to_list(row):
    strs = row.replace('[','').split('],')
    lists = [list(map(int, s.replace(']','').split(','))) for s in strs]
    return lists[0]

"""
Given the facial locations and emotions, the emotion is written on top of the bounding boxes
"""
def annotate_emotions(locations, texts, frame):
    for location,text in zip(locations, texts):
        location = str_to_list(location)
        font                   = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = tuple(location[:2])
        fontScale              = 1
        fontColor              = (0,255,0)
        lineType               = 2

        cv2.putText(frame,text,
            bottomLeftCornerOfText,
            font,
            fontScale,
            fontColor,
            lineType)

    return frame
