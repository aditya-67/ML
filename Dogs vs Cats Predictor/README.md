# Image Recognition (Dogs vs Cats)

## Website (Deployed in Heroku)

 https://image-recognition-cnn.herokuapp.com/

## Overview

This is an end-to-end implementation of Image Recognition of dogs and cats using CNN built with tflearn, which you can run it locally. We are using Flask to serve our saved model. Just upload the image of either a cat or a dog, it can predict accordingly.

## Dependencies

To install dependencies, 

```pip install -r requirements.txt```

## Training and Saving the model

Please refer to this [notebook](https://github.com/aditya-67/ML/blob/master/Dogs%20vs%20Cats%20Image%20Classification.ipynb)

## Usage

Once dependencies are installed, just run this. 

```python app.py```

Now, the application would be running on 

```http://localhost:8080```

It is serving a saved Keras model via Flask.








