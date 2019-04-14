from flask import Flask, render_template,request,jsonify
import numpy as np
import re
import base64
import sys 
import os
import cv2

sys.path.append(os.path.abspath("./model"))
from load import * 

app = Flask(__name__)

global model, graph
model, graph = init()

#decoding an image from base64 into raw representation
def convertImage(imgData1):
	imgstr = re.search('data:image/jpeg;base64,(.*)', imgData1).group(1)
	with open('output.png', 'wb') as output:
		output.write(base64.b64decode(imgstr))
	

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/predict/',methods=['GET','POST'])
def predict():
	str_label = ''
	imgData = request.get_data().decode('utf-8')
	#encode it into a suitable format
	convertImage(imgData)
	#read the image into memory
	x = cv2.resize(cv2.imread('output.png', cv2.IMREAD_GRAYSCALE),(100,100))
	x = x.reshape(100,100,1)
	#in our computation graph
	with graph.as_default():
		#perform the prediction
		model_out = model.predict([x])[0]
		#convert the response to a string
		if np.argmax(model_out) == 1: 
			str_label='Dog'
			probability = model_out[1]
		else: 
			str_label='Cat'
			probability = model_out[0]
		result = str_label
		probability = str(round(probability*100, 2))
		return jsonify({"probability" : probability, "result":result})
	

if __name__ == "__main__":
	#decide what port to run the app in
	port = int(os.environ.get('PORT', 5000))
	#run the app locally on the givn port
	app.run(host='0.0.0.0', port=port)
	#optional if we want to run in debugging mode
	#app.run(debug=True)
