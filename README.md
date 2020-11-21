# Emotion and Activity Detection from still images and videos

# RESULT

## Front-end 

<figure>
    <img src='https://github.com/SurajSubramanian/Emotion-and-Activity-Detection/blob/main/images/frontend1.png' alt='missing' width = '425'/>
    <figcaption>Front-end design</figcaption>
</figure>
<figure>
    <img src='https://github.com/SurajSubramanian/Emotion-and-Activity-Detection/blob/main/images/frontend2.png' alt='missing' width = '425'/>
    <figcaption>Outputs after uploading image</figcaption>
</figure>


## Video Output

<video width="320" height="240" controls>
  <source src="https://drive.google.com/file/d/10fwQ4HK_emfmPkviYwL8QLXVSO2cQUiH/preview" type="video/mp4">
</video>

## Image Outputs

<img src="https://github.com/SurajSubramanian/Emotion-and-Activity-Detection/blob/main/images/laughing.png" width="425"/>

<img src="https://github.com/SurajSubramanian/Emotion-and-Activity-Detection/blob/main/images/emotion-activity.png" width="425"/>

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
