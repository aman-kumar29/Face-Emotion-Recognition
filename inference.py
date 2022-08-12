""" importing the necessary libraries"""
import cv2
from tensorflow.keras.models import load_model
from keras import regularizers
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
from keras import models

""" Mounting drive on my google colab """

from google.colab import drive
drive.mount('/content/drive')

emotions = {0:'angry',
            1:'contempt',
            2:'disgust',
            3:'fear',
            4:'happy',
            5:'sad',
            6:'surprise'}
classes= ['angry','contempt', 'disgust', 'fear', 'happy', 'sad', 'surprise']

model = keras.models.load_model('/content/drive/MyDrive/ModelEmotionDetection/emotion_model.h5')

test_datagen  = ImageDataGenerator(rescale = 1./255)

test_dataset = test_datagen.flow_from_directory(directory = '/content/drive/MyDrive/ModelEmotionDetection/CK48',
                                                  target_size = (48,48),
                                                  class_mode = 'categorical',
                                                  batch_size = 64)
""" defining the prediction function"""

def predictionfn(img_path,cll):
  img=image.load_img(img_path)
  img=img.resize((48,48))
  arr=np.asarray(img)
  arr=np.expand_dims(arr,axis=0)
  score = model.predict(arr)
  print(score)
  score[0]
  y_pred=np.argmax(score[0])
  print("true emotion: ",cl,"Predicted Emotion: ",emotions[y_pred])
  return score[0]


""" predicting the outcome for every emotion using ck+ dataset"""

for cl in classes:
  listt=[]
  class_path= os.path.join('/content/drive/MyDrive/ModelEmotionDetection/CK48',cl)
  for img in os.listdir(class_path):
    prediction = predictionfn((class_path + "/" + img),cl)
    listt.append(prediction)



"""Pre-Processing the testing image"""
img=image.load_img('/content/drive/MyDrive/ModelEmotionDetection/model.h5')
img=img.resize((48,48))
arr=np.asarray(img)
arr=np.expand_dims(arr,axis=0)
score = np.array([[1,3,5,6,8]])
print(score)
print(type(score))
print(np.argmax(score[0]))



