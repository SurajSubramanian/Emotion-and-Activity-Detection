from __future__ import division

import os
import sys
import csv
import time
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

def activity_detector(image_name):
    result = []
    predictor = CustomImagePrediction()
    predictor.setModelPath(model_path=os.path.join(root, "action-detection-image", "action.h5"))
    predictor.setJsonPath(model_json=os.path.join(root, "action-detection-image", "model_class.json"))
    predictor.loadFullModel(num_objects=16)

    predictions, probabilities = predictor.predictImage(image_input=image_name, result_count=4)
    for prediction, probability in zip(predictions, probabilities):
        result.append([prediction, probability])
    print(result)
    return result[0][0]
