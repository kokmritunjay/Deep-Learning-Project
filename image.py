import urllib2
import urllib
from urllib2 import urlopen
import glob
import cv2
from PIL import Image
from PIL import ImageStat
import math

def numface(img):
    CASCADE="Face_cascade.xml"
    FACE_CASCADE=cv2.CascadeClassifier(CASCADE)
    image=cv2.imread(img)
    #load test iamge
    #convert the test image to gray image as opencv face detector expects gray images
    image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = FACE_CASCADE.detectMultiScale(image_grey,scaleFactor=1.16,minNeighbors=5,minSize=(25,25),flags=0)
    return (len(faces))

def brightness( im_file ):
   im = Image.open(im_file)
   stat = ImageStat.Stat(im)
   r,g,b = stat.mean
   return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))

def is_grey_scale(img):
    im = Image.open(img).convert('RGB')
    w,h = im.size
    for i in range(w):
        for j in range(h):
            r,g,b = im.getpixel((i,j))
            if r != g != b: return False
    return True

filepath="/home/shalini.pcs16/btp/images.txt"
i=0
with open(filepath) as fp:  
    line=fp.readline()
    while line:
	print line
        urllib.urlretrieve(line,"/home/shalini.pcs16/btp/images//" +str(i+1)+".jpg")
        i=i+1
        line = fp.readline()
for img in glob.glob('/home/shalini.pcs16/btp/images//*.jpg'): # All jpeg images
    if(is_grey_scale(img)):
        print("gray")
    else:
        print("color")
    print("brightness="+(str)(brightness(img)))
    print("number of faces="+str(numface(img)))
    print("\n")
    
    
