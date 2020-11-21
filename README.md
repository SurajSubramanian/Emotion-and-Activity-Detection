# Emotion and Activity Detection from still images and videos

# RESULT

## Front-end 

![alt text](https://github.com/SurajSubramanian/Emotion-and-Activity-Detection/blob/main/images/frontend1.png)

![alt text](https://github.com/SurajSubramanian/Emotion-and-Activity-Detection/blob/main/images/frontend2.png)

## Video Output

<img src="https://github.com/SurajSubramanian/Emotion-and-Activity-Detection/blob/main/images/running(ouput).mp4/maxresdefault.jpg" width="50%">](https://github.com/SurajSubramanian/Emotion-and-Activity-Detection/blob/main/images/running(ouput).mp4)

## Image Outputs

![alt text](https://github.com/SurajSubramanian/Emotion-and-Activity-Detection/blob/main/images/laughing.png)

![alt text](https://github.com/SurajSubramanian/Emotion-and-Activity-Detection/blob/main/images/emotion-activity.png)

# EXECUTION

Both the facial expression recognition and action-detetion weights have to be downloaded at first. To do this, `cd` into the respective directories and execute the `download_weights.sh` file using : 

```
./download_weights.sh
```

If you do not have the permission, run : `chmod +x download_weights.sh`

Install requirements by running `pip install requirements.txt`

## To upload an image and run the code, use :
```
python runtim.py image_name/video_name
(or)
python runtime.py
```

In the second case, you'll be asked to enter the name of the image/video.

## To execute the real-time FER code, run :

```
python realime.py
```

## To run the web-based application :

Inside the frontend directory, run :
```
npm install
```
to install all the node modules.

To start the front-end React application, run :
```
npm start
```
inside the frontend directory and 
```
python app.py
```
to run the flask application.
