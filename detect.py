#!/usr/bin/env python
import io
import pandas as pd
import cv2
import glob
import re
import os
from google.cloud import vision
from google.cloud.vision import types
dirany=os.path.dirname(__file__)
data=[]
for i in range(0,1710,100):
	client = vision.ImageAnnotatorClient()
	a='frame'+str(i)+'.jpg'
	file_name=os.path.join(dirany,a)
	with io.open(file_name,'rb') as image_file:
		content=image_file.read()
	image = vision.types.Image(content=content)
	response = client.text_detection(image=image)
	texts = response.text_annotations
	print('Texts:')
	flag=0;
	ans=''
	ansnum=0
	for text in texts:
		if(flag!=0):
			ans+=text.description
		flag=1
		#vertices = (['({},{})'.format(vertex.x, vertex.y)
		#	for vertex in text.bounding_poly.vertices])
		#print('bounds: {}'.format(','.join(vertices)))
	ansnum=float(ans)/10
	data.append(ansnum)
	print(ansnum)
	print (i)	
df = pd.DataFrame(data, columns=["data"])
df.to_csv('list.csv', index=False)
print (data)
    