import cv2
import os
import csv
import json
import time
import pandas as pd
from glob import glob
from tqdm import tqdm
import imutils
from retinaface.utils import vis_annotations
from retinaface.pre_trained_models import get_model
from utils import *
from ImageExtractor import image_extractor
from FacialExpression.predictor import emotion_predictor
from ActivityDetection import *

root = os.getcwd()
# loading retinaface model
model = get_model("resnet50_2020-07-20", max_size=2048)
model.eval()

"""
Function reads the image/video and annotates the facial locations with boudning boxes and also finds their emotions
"""
def emotion_detector(input_name):
    # input is a video
    if '.mp4' in input_name:
        # loading video
        vs = cv2.VideoCapture(input_name)
        writer = None
        (W, H) = (None, None)
        try:
            prop = cv2.cv.CV_CAP_PROP_FRAME_COUNT if imutils.is_cv2() else cv2.CAP_PROP_FRAME_COUNT
            prop = 5
            total = int(vs.get(prop))
            print("[INFO] {} total frames in video".format(total))

        except:
            print("[INFO] could not determine # of frames in video")
            print("[INFO] no approx. completion time can be provided")
            total = -1
        i_ = 0
        # processing the video frame by frame
        while True:
            print(str(i_) + ' th frame')
            i_ += 1
            start = time.time()
            (grabbed, frame) = vs.read()
            if not grabbed:
                break
            # predicting annotations using retinaface model
            annotations = model.predict_jsons(frame)
            cv2.imwrite('frame.jpg', frame)
            if annotations != [{'bbox': [], 'score': -1, 'landmarks': []}]:
                frame = vis_annotations(frame, annotations)
                with open('annotations.json', 'w') as f:
                    json.dump(annotations, f)
                cv2.imwrite('temp.jpg', frame)
                json_csv()
                # extract each face from the frame and storing it in a separate directory 'extracted'
                image_extractor('temp.jpg')
            
            # predicting emotions of all the faces in the frame
            with open('emotions.csv', 'w')  as f:
                writer1 = csv.writer(f)
                writer1.writerow(['image_name', 'emotion'])
                for img in sorted(os.listdir('extracted')):
                    img_path = os.path.join(root, 'extracted' , img)
                    emotion = emotion_predictor(img_path)
                    writer1.writerow([img, emotion])
            df = pd.read_csv('annotations.csv')
            df['emotion'] = pd.read_csv('emotions.csv')['emotion']
            df.to_csv('annotations.csv')
            df = pd.read_csv('annotations.csv')
            locations, texts = df['bbox'], df['emotion']
            
            # use boudning boxes to mark the location of the frame and write a text above each box which contains the facial expression
            frame = annotate_emotions(locations, texts, frame)
            end = time.time()
            
            # writing this frame into the output video
            if writer is None:
                fourcc = cv2.VideoWriter_fourcc(*"MP4V")
                output_name = input_name.split('.')[0] + '(ouput).mp4'
                writer = cv2.VideoWriter(output_name, fourcc, 30, (frame.shape[1], frame.shape[0]), True)
                if total > 0:
                    elap = (end - start)
                    print("[INFO] single frame took {:.4f} seconds".format(elap))
                    print("[INFO] estimated total time to finish: {:.4f}".format(elap * total))
            cv2.imwrite('emotion.jpg', frame)
            activity_detector('emotion.jpg')
            frame = cv2.imread('activity.png')
            writer.write(frame)
            
        writer.release()
        vs.release()
    
    # input is an image
    elif '.jpg' in input_name or '.png' in input_name or '.jpeg' in input_name:
        print("---Reading image---")
        frame = cv2.imread(input_name)
        print("---Predicting annotations using Retinaface---")
        annotations = model.predict_jsons(frame)
        if annotations != [{'bbox': [], 'score': -1, 'landmarks': []}]:
            frame = vis_annotations(frame, annotations)
            with open('annotations.json', 'w') as f:
                json.dump(annotations, f)
        name,extension = input_name.split('.')
        print("---Writing output image---")
        output_name = 'emotion.' + extension
        
        json_csv()
        # extracting all faces from the image to a separate directory 'extracted'
        image_extractor(input_name)
        
        # predicting emotions of all the faces in the image
        with open('emotions.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['image_name', 'emotion'])
            for img in sorted(os.listdir('extracted')):
                img_path = os.path.join(root, 'extracted', img)
                emotion = emotion_predictor(img_path)
                writer.writerow([img, emotion])
                print(emotion)
        df = pd.read_csv('annotations.csv')
        df['emotion'] = pd.read_csv('emotions.csv')['emotion']
        df.to_csv('annotations.csv')
        
        df = pd.read_csv('annotations.csv')
        locations, texts = df['bbox'], df['emotion']
        # use boudning boxes to mark the location of the frame and write a text above each box which contains the facial expression
        frame = annotate_emotions(locations, texts, frame)
        
        cv2.imwrite(output_name, frame)
    
    else:
        print("Invalid format ...\nTry again")
