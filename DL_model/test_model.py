import random

from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
from imutils import paths
#import train_network as tn
import data.constants as cst
import os



# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True, help="path to trained model model")
ap.add_argument("-d", "--dataset", required=True, help="path to input dataset")
args = vars(ap.parse_args())

# initialize the data and labels
print("[INFO] loading images...")
data = []
labels = []

# grab the image paths and randomly shuffle them
imagePaths = sorted(list(paths.list_images(args["dataset"])))
random.seed(42)
random.shuffle(imagePaths)

# loop over the input images
for imagePath in imagePaths:
    # load the image, pre-process it, and store it in the data list
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (28, 28))
    image = img_to_array(image)
    data.append(image)

    # extract the class label from the image path and update the
    # labels list
    label = imagePath.split(os.path.sep)[-2]
    if label == "cardboard" :
        label = cst.CARDBOARD
    elif label == "glass":
        label = cst.GLASS
    elif label == "metal":
        label = cst.METAL
    elif label == "paper":
        label = cst.PAPER
    elif label == "plastic":
        label = cst.PLASTIC
    else :
        label = cst.TRASH
    labels.append(label)
print(len(labels))

# load the trained convolutional neural network
print("[INFO] loading network...")
model = load_model(args["model"])


data = np.array(data, dtype="float") / 255.0
#labels = np.array(labels)


res = model.predict(data)

compteur = 0
for i in range(0, len(res)):

    # classify the input image
    [glass, paper, cardboard, plastic, metal, trash] = res[i]
    l = [glass, paper, cardboard, plastic, metal, trash]

    # build the label
    m = max(l)
    for k, j in enumerate(l) :
        if j == m :
            res_index = k

    name = ['glass', 'paper', 'cardboard', 'plastic', 'metal', 'trash']
    label = name[res_index]
    proba = l[res_index]

    if name[labels[i]] == label :
        compteur = compteur + 1
    #label = "{}: {:.2f}%".format(label, proba * 100)

print("Accuracy : ", compteur/len(res))

# # draw the label on the image
# output = imutils.resize(orig, width=400)
# cv2.putText(output, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
#             0.7, (0, 255, 0), 2)
#
# # show the output image
# cv2.imshow("Output", output)
# cv2.waitKey(0)