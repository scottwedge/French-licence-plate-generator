# Labrak Yanis
# Bachelor of science in CS - Third years
# Avignon University, Avignon - France
# My first OCR

# Tutorials
  # https://hackernoon.com/latest-deep-learning-ocr-with-keras-and-supervisely-in-15-minutes-34aecd630ed8
  # https://cvisiondemy.com/license-plate-detection-with-opencv-and-python/

import numpy as np
import cv2

import datetime

from PIL import ImageFont, ImageDraw, Image

import random

import glob, os

def Generate():

	file = open("AllLicencePlates_FR.txt", "w")

	for L1 in range(ord('a'), ord('b') + 1):

		for L2 in range(ord('a'), ord('z') + 1):

			for N1 in range(0,9):

				for N2 in range(0,9):
					
					for N3 in range(0,9):

						for L3 in range(ord('a'), ord('z') + 1):

							for L4 in range(ord('a'), ord('z') + 1):

								LicencePlate = str(chr(L1) + chr(L2) + "-" + str(N1) + str(N2) + str(N3) + "-" + chr(L3) + chr(L4) )

								file.write(LicencePlate + "\n")

	file.close()

def NumberPlateToPics(numberPlate, dep_num):
    	
	licencePlate = {
		"metal": {
			"url": "stock_plates/metal.png",
			"x": 720,
			"y": 12
		},
		"plexi": {
			"url": "stock_plates/plexi.png",
			"x": 720,
			"y": 12
		}
	}

	img = cv2.imread(licencePlate["plexi"]["url"], -1)
	Height,Width = img.shape[0], img.shape[1]
	center = (Width/2, Height/2)

	Url = "outputs/" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) + ".png"

	textInfos = {
		"height": int(Width/7.5),
		"width": int(Height/2)
	}

	b,g,r,a = 0,0,0,0
	fontpath = "fonts/Oswald-Regular.ttf"

	img_pil = Image.fromarray(img)
	draw = ImageDraw.Draw(img_pil)
	
	# Numéro d'immatriculation
	fontNumberPlate = ImageFont.truetype(fontpath, 160)
	draw.text((int(Width/8.5), -42),  numberPlate, font = fontNumberPlate, fill = (b, g, r, a))

	# Numéro de département
	fontDepartement = ImageFont.truetype(fontpath, 55)
	dw, dh = draw.textsize(dep_num)
	draw.text((int((Width - 72) + ((15 - dw)/2)), 75),  dep_num, font = fontDepartement, fill = (255, 255, 255, 0))

	# Convert the img back to cv2 format
	img = np.array(img_pil)

	img_region = cv2.resize(cv2.imread("regions/logos/logo-ile-de-france.png"),(61,68))
	img[licencePlate["plexi"]["y"]:licencePlate["plexi"]["y"] + 68, licencePlate["plexi"]["x"]:licencePlate["plexi"]["x"] + 61] = img_region

	# Display the image on the GUI
	cv2.imshow('Mon image', img)

	cv2.imwrite( Url, img )

	# Wait 1s
	cv2.waitKey(10000)

NumberPlateToPics("AV-714-RQ", "84")

# Generate()