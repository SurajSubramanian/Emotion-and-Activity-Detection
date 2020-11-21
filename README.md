# Emotion and Activity Detection from still images and videos

Both the facial expression recognition and action-detetion weights have to be downloaded at first. To do this, `cd` into the respective directories and execute the `download_weights.sh` file using : 

```
./download_weights.sh
```

If you do not have the permission, run : `chmod +x download_weights.sh`

Install requirements by running `pip install requirements.txt`

## To upload an image and run the code, use :
```
python main.py image_name/video_name
(or)
python main.py
```

In the second case, you'll be asked to enter the name of the image/video.

## To execute the real-time FER code, run :

```
python realime.py
```
