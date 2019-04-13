from flask import Flask, render_template,request,jsonify
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
import re
import base64
import sys 
import os

sys.path.append(os.path.abspath("./model"))
from load import * 

app = Flask(__name__)

global model, graph
model, graph = init()

#decoding an image from base64 into raw representation
def convertImage(imgData1):
	imgstr = re.search('data:image/png;base64,(.*)', imgData1).group(1)
	with open('output.png', 'wb') as output:
		output.write(base64.b64decode(imgstr))
	

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/predict/',methods=['GET','POST'])
def predict():
	imgData = request.get_data().decode('utf-8')
	#encode it into a suitable format
	convertImage(imgData)
	#read the image into memory
	x = imread('output.png',mode='L')
	#compute a bit-wise inversion so black becomes white and vice versa
	x = np.invert(x)
	#make it the right size
	x = imresize(x,(28,28))
	#imshow(x)
	#convert to a 4D tensor to feed into our model
	x = x.reshape(1,28,28,1)
	#in our computation graph
	with graph.as_default():
		#perform the prediction
		out = model.predict(x)
		#convert the response to a string
		probabilities = np.array_str(out)
		result = str(np.argmax(out,axis=1))
		return jsonify({"probabilities" : probabilities, "result":result})
	

if __name__ == "__main__":
	#decide what port to run the app in
	port = int(os.environ.get('PORT', 5000))
	#run the app locally on the givn port
	app.run(host='0.0.0.0', port=port)
	#optional if we want to run in debugging mode
	#app.run(debug=True)
