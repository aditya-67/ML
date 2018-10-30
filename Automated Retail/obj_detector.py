import os
import sys
import glob
import dlib
from skimage import io
from skimage.draw import polygon_perimeter
import traceback

if len(sys.argv) != 2:
    print(
        "Give the path to detect folder")
    exit()
detector_folder = sys.argv[1]

items = ["Food","Healthcare"]

options = dlib.simple_object_detector_training_options()
options.add_left_right_image_flips = True
options.C = 5

options.num_threads = 2;options.be_verbose = True


for f in glob.glob(os.path.join(detector_folder, "test/*.jpg")):
    for i in items:
        training_xml_path = os.path.join(detector_folder, "train", i,"train.xml")
        testing_xml_path = os.path.join(detector_folder, "test","test.xml")
        detector_svm = os.path.join(detector_folder,"train", i ,"detector.svm")

        if not os.path.exists(detector_svm):
            dlib.train_simple_object_detector(training_xml_path, detector_svm, options)

        detector = dlib.simple_object_detector(detector_svm)


        win_det = dlib.image_window()
        win_det.set_image(detector)

        print("Showing detections on the images in the test folder...")
        win = dlib.image_window()
        win = dlib.image_window()
        
        print("Processing file: {}".format(f))
        img = io.imread(f)
        dets = detector(img)
        print("Number of objects detected: {}".format(len(dets)))
        bOverLays = False
        for k, d in enumerate(dets):
            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                k, d.left(), d.top(), d.right(), d.bottom()))
            rr,cc = polygon_perimeter([d.top(), d.top(), d.bottom(), d.bottom()],
                                [d.right(), d.left(), d.left(), d.right()])
            try:
                img[rr, cc] = (0, 255, 0)
                if bOverLays == False:
                    bOverLays = True
            except:
                traceback.print_exc()
                
        # Save the image detections to a file for future review.
        if bOverLays == True:
            io.imsave(f.replace("test/","output/"), img)
        win.clear_overlay()
        win.set_image(img)
        win.add_overlay(dets)
        input("Press Enter to continue...")