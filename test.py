# USAGE
# python3 test.py --model terror.model --imageFolder testimages --outPutFile resultDemo.csv

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

##my import
import os
import pandas as pd


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,	help="path to trained model model")
ap.add_argument("-i", "--imageFolder", required=True, help="path to input image")
ap.add_argument("-j", "--outPutFile", required=True, help="path to outPutFile CSV")
args = vars(ap.parse_args())

#loading model
print("[INFO] loading network...")
model = load_model(args["model"])

##output file variables
df=pd.DataFrame()
nameL,noL,yesL=[],[],[]

##code
imageLis=os.listdir(args["imageFolder"])
for img in imageLis:
	##modify image true filename
	img=args["imageFolder"]+"/"+img
	#load the image
	image = cv2.imread(img)
	print img
	orig = image.copy()
	#print(image,type(image))
	# pre-process the image for classification
	image = cv2.resize(image, (28, 28))
	image = image.astype("float") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	#model evaluation
	(notSanta, santa) = model.predict(image)[0]
	nameL.append(img);noL.append(notSanta);yesL.append(santa)
	#print (img)
df["img"],df["no"],df["yes"]=nameL,noL,yesL
df.to_csv(args["outPutFile"], index=False)
print ("done")

