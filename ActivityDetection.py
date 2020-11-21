from __future__ import division
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import os
import sys
import cv2
import csv
import time
import pandas as pd
import datetime
import argparse
import shutil
from PIL import Image
import operator

import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torch.autograd import Variable

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import NullLocator
from ImageExtractor import *
from utils import *
from imageai.Prediction.Custom import ModelTraining, CustomImagePrediction
from PIL import Image, ImageDraw, ImageFont

root = os.getcwd()

def run_predict(image_name):
    result = []
    predictor = CustomImagePrediction()
    predictor.setModelPath(model_path=os.path.join(root, "action-detection-image", "action.h5"))
    predictor.setJsonPath(model_json=os.path.join(root, "action-detection-image", "model_class.json"))
    predictor.loadFullModel(num_objects=16)

    predictions, probabilities = predictor.predictImage(image_input=image_name, result_count=4)
    for prediction, probability in zip(predictions, probabilities):
        result.append([prediction, probability])
    print(result)
    return result

def activity_detector(image_name):
    result = run_predict('frame.jpg')[0][0]
    image = Image.open(image_name)
    color = 'rgb(0, 0, 0)'
    _,w,_ = cv2.imread(image_name).shape
    (x, y) = (w//2-1, 0)
    font = ImageFont.truetype('Comic Sans MS', size=45)
    draw = ImageDraw.Draw(image)
    draw.text((x, y), result, fill=color, font=font)
    image.save('activity.png')

def activity_detector_video(video_name):
    vs = cv2.VideoCapture(video_name)
    writer = None
    (W, H) = (None, None)
    activities = []
    while True:
        start = time.time()
        (grabbed, frame) = vs.read()
        print("grabbed :", grabbed)
        if grabbed == True:
            cv2.imwrite('action-temp.jpg', frame)
            activity_detector('action-temp.jpg')
            result = run_predict('action-temp.jpg')[0][0]
            frame = cv2.imread('activity.png')
            activities.append(result)
            if writer is None:
                fourcc = cv2.VideoWriter_fourcc(*"MP4V")
                output_name = video_name.split('.')[0] + '(activity).mp4'
                writer = cv2.VideoWriter(output_name, fourcc, 30, (frame.shape[1], frame.shape[0]), True)
            writer.write(frame)
        else:
            break
        
    writer.release()
    vs.release()
    print("Activities in order :", activities)
    dic = {activity : activities.count(activity) for activity in set(activities)}
    d = sorted(dic.items(),key=operator.itemgetter(1),reverse=True)
    print("dict :", d)
    print("Top 3 Activities involved :\n")
    for i,(key,value) in enumerate(d):
        if i > 3:
            break
        print(key, value)
