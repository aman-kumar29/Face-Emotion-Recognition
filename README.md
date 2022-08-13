# Face Emotion Detection System
## Packages need to be installed
- Numpy
- CV2
- keras
- tensorflow
- intrtools

## Kaggle Code link
- https://www.kaggle.com/code/amankumar2004/emotion-detection-recognition


## All the folders in the directory:
1. **harcascade_frontalface_classifier**- An xml file which is an Object Detection Algorithm used to identify faces in an image or a real time video. 
2. **models**- contains the final .json file and model weights we used in our final inference.py and live_emotion_detection.py file. 
   emotion_model.json
   emotion_model_weights.h5
4. **samples**- contains the video we found on internet on which we tested our face recognition and emotion detection on using live_emotion_detection.py file.
5. **face_emotion_recognition.ipynb** file if the final jupyter notebook we trained on giving all the details including confusionn matrix and dataset breifing.
6. **inference.py**- An inference file used to check our model on a different dataset( we used CK+ dataset).
7. **live_emotion_detection.py** - This python file is used for live detection using cmaera realtime. We have used a sample video in it to show the outputs given by our model.

## Optimizers  Used
 We trained our model uisng different optimizers including **Adam, Adamax, RMSprop**.
 After evaluation the best one turned out to be **Adam**.
 
 
## Transfer Learning 
 We used many different pretrained models namely **Resnet50, VGG16, InceptionResnetV2**
 We chose **Resnet50** as the best pretrained model after comparing different metrics
## Final Parameters
Final Pretrained model-- **Resnet50**
Final Optimizer used -- **Adam**

|   Train_acc   |    Train_loss   |    Val_acc      |    Val_loss     |    F1_score     |
| :------------ |:---------------:|:---------------:|:---------------:|:---------------:|
|   84.09%      |    0.9372       |    65.60%       |    1.117        |    0.486569     |

https://user-images.githubusercontent.com/99892898/184361402-13b8b507-b4a8-42b7-ba8b-eb34ed96a73a.mp4


#### Group Members
1. Aman Kumar(210002012)
2. Rishabh Patil(210002062)
3. Parth Toshniwal(210002056)
4. Prajwal Bastewad(210002021)

## Group Mentor

1.Atharva Mohite(200003016)
