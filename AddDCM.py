#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/4/24 10:35
import os
import numpy as np
import pydicom
from decompressed import dc
from PIL import Image

dir = r'D:\DataExport\Pneumonia\DataPreprocess'
os.chdir(dir)

def dcm2png(dcm_file, png_file):
	img = pydicom.read_file(dcm_file)
# 	convert to float type
	img = img.pixel_array.astype(float)
# 	scaled into 0-255
	img_scaled = (np.maximum(img, 0)/img.max())*255.0
	img_scaled = np.uint8(img_scaled)
	new_img = Image.fromarray(img_scaled)
	new_img.save(png_file)


for path, subpath, files in os.walk(dir + r'\data'):
	for sub in subpath:
		if len(sub) > 10:
			# extract exam_no
			exam_no = sub[-10:]
			# 去掉路径中的中文，不然decompressed文件无法读取
			os.rename(os.path.join(path,sub), os.path.join(path,exam_no))
			sub = exam_no
			for filename in os.listdir(os.path.join(path,sub)):
				temp = exam_no + '.dcm'
				if '.dcm' not in filename.lower():
					os.rename(os.path.join(path,sub, filename), os.path.join(path, sub, temp))
				comp = os.path.join(path, sub, temp)
				dc(comp, comp)
				dcm2png(comp, os.path.join(dir, 'preprocessed_data', exam_no+'.png'))
