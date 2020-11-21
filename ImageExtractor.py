import os
import cv2
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils import str_to_list
root = os.getcwd()

"""
Extracts all the faces from the image to a separate directory 'extracted' using their annotations in a csv file
"""
def image_extractor(input_name):
    if 'extracted' in os.listdir():
        shutil.rmtree('extracted')
    os.mkdir('extracted')
    df = pd.read_csv('annotations.csv')
    frame = cv2.imread(input_name)
    for img_no, label in enumerate(df['bbox']):
        img_name = input_name.split('.')[0] + '.' + str(img_no)+'.jpg'
        x,y,w,h = str_to_list(label)
        x,y,w,h = max(0, x), max(0, y), max(0, w), max(0, h)
        img = frame[y:h, x:w]
        cv2.imwrite(os.path.join(root, 'extracted', img_name), img)

def yolo_extractor(input_name):
    if 'yolo-extracted' in os.listdir():
        shutil.rmtree('yolo-extracted')
    os.mkdir('yolo-extracted')
    df = pd.read_csv('yolo.csv')
    frame = cv2.imread(input_name)
    for img_no, label in enumerate(df['corners']):
        img_name = input_name.split('.')[0] + '.' + str(img_no)+'.jpg'
        x1,y1,x2,y2 = str_to_list(label)
        x1,y1,x2,y2 = max(0, x1), max(0, y1), max(0, x2), max(0, y2)
        img = frame[y1:y2, x1:x2]
        cv2.imwrite(os.path.join(root, 'yolo-extracted', img_name), img)
