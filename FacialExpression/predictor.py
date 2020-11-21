import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import torch
import torch.nn as nn
import torch.nn.functional as F
import os
from torch.autograd import Variable

from FacialExpression.transforms import transforms
from skimage import io
from skimage.transform import resize
from FacialExpression.models.vgg import *

os.environ['KMP_DUPLICATE_LIB_OK']='True'

cut_size = 44

transform_test = transforms.Compose([
    transforms.TenCrop(cut_size),
    transforms.Lambda(lambda crops: torch.stack([transforms.ToTensor()(crop) for crop in crops])),
])
root = os.getcwd()

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.58, 0.114])

def emotion_predictor(img_name):
    raw_img = io.imread(img_name)
    gray = rgb2gray(raw_img)
    gray = resize(gray, (48,48), mode='symmetric').astype(np.uint8)

    img = gray[:, :, np.newaxis]

    img = np.concatenate((img, img, img), axis=2)
    img = Image.fromarray(img)
    inputs = transform_test(img)

    class_names = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

    net = VGG('VGG19')
    checkpoint = torch.load(os.path.join(root, 'FacialExpression', 'PrivateTest_model.t7'), map_location=torch.device('cpu'))
    net.load_state_dict(checkpoint['net'])
    # net.cuda()
    net.eval()

    ncrops, c, h, w = np.shape(inputs)

    inputs = inputs.view(-1, c, h, w)
    # inputs = inputs.cuda()
    with torch.no_grad():
        inputs = Variable(inputs)
    outputs = net(inputs)

    outputs_avg = outputs.view(ncrops, -1).mean(0)  # avg over crops

    score = F.softmax(outputs_avg, dim=0)
    _, predicted = torch.max(outputs_avg.data, 0)
    return str(class_names[int(predicted.cpu().numpy())])
