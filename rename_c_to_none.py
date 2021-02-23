"""
Auther : moriitkys
LICENSE : MIT
"""

import numpy as np
import glob
import cv2

input_folder = "./0001_raw"

extentions = {"_c.png":".png", "_c_mask":"_mask.png"}
extention_out = ""

for file in glob.glob(input_folder + "/*"):
    for key in extentions:
        if extentions[key] in file:
            input_img = cv2.imread(file)

            cv2.imwrite(file.replace(key, extentions[key]), input_img)


