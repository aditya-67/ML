import numpy as np
import cv2
import argparse
from imutils.paths import list_images
from box_selector import BoxSelector

#parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d","--dataset",required=True,help="path to images dataset...")
ap.add_argument("-a","--annotations",required=True,help="path to save annotations...")
ap.add_argument("-i","--images",required=True,help="path to save images")
args = vars(ap.parse_args())

#annotations and image paths
annotations = []
imPaths = []
string = ""

#loop through each image and collect annotations
for imagePath in list_images(args["dataset"]):
    #load image and create a BoxSelector instance
    image = cv2.imread(imagePath)
    bs = BoxSelector(image,"Image")
    cv2.imshow("Image",image)
    cv2.waitKey(0)

    #order the points suitable for the Object detector
    pt1,pt2 = bs.roiPts
    (x,y,xb,yb) = [pt1[0],pt1[1],pt2[0],pt2[1]]
    annotations.append([int(x),int(y),int(xb),int(yb)])
    imPaths.append(imagePath)
    imagePath = imagePath.split("/")[1]
    string += "<image file='"+ imagePath +"'>\n"
    string += "<box top='" + str(int(y))+ "' left='"+str(int(x))+"' width='"+str(int(xb))+"' height='"+str(int(yb))+"'/>\n</image>\n"
    
    

#save annotations and image paths to disk
annotations = np.array(annotations)
imPaths = np.array(imPaths,dtype="unicode")


#print(str)
f = open(args["dataset"] + "/train.xml","w+")
f.write("<?xml version='1.0' encoding='ISO-8859-1'?>\n<?xml-stylesheet type='text/xsl' href='image_metadata_stylesheet.xsl'?>\n<dataset>\n<name>imglab dataset</name>")
f.write("<images>")
f.write(string)
f.write("</images>\n</dataset>")

np.save("annotations/" + args["annotations"],annotations)
np.save("imgpaths/" + args["images"],imPaths)
