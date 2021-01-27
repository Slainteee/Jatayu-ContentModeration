from flask import Flask, request, redirect, url_for, flash, jsonify
import pickle
import json
from tensorflow import keras
#from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
#import ocrspace
from googletrans import Translator
import requests
from io import BytesIO
from PIL import Image
from sightengine.client import SightengineClient
import pytesseract
import urllib.request
import speech_recognition as sr



app = Flask(__name__)
#with open('tokenizer.pickle', 'rb') as handle:
	#tokenizer = pickle.load(handle)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

client = SightengineClient('510188098','WaehbLBjT3mYTmnxDsp3')

model = pickle.load(open(r"hatespeech\saved_models\lr_model.pkl", 'rb'))  #path to hate speech model
vect = pickle.load(open(r"hatespeech\saved_models\vectorizer.pkl", 'rb')) #path to hate speech vectorizer

spam_model = pickle.load(open(r"Spam Classifier\saved_models\lr_model.pkl", 'rb')) #path to spam model
spam_vect = pickle.load(open(r"Spam Classifier\saved_models\vectorizer.pickle", 'rb')) ##path to spam vectorizer

#model = keras.models.load_model('model.h5')
violence_model=keras.models.load_model(r'Violence-Detection\Tensorflow-Implementation\violence_model4.h5') #path to violence model

@app.route('/', methods=['POST','GET'])
def makecalc():
	data = request.get_json()
	translator = Translator()
	#img_url=data["image"]
	t=data["type"]
	#t=str(request.args["type"])
	if(t=="video"):
		vid_url=data["video"]
		output = client.check('nudity').video_sync(vid_url)
		for i in range(len(output['data']['frames'])):
			if(output['data']['frames'][i]['nudity']['safe']<0.5):
				return jsonify("NUDITY")
		return jsonify("NORMAL")
	elif(t=="image"):
		img_url=data["image"]
		#img_url=str(request.args['image'])
		#api = ocrspace.API('415485422988957', ocrspace.Language.English)
		response=requests.get(img_url)
		img_org=Image.open(BytesIO(response.content))
		img=img_org.resize((160,160))
		img=np.array(img)
		extractedInformation=pytesseract.image_to_string(img_org)
		print(extractedInformation)
		img=np.array([img])
		pred=violence_model.predict(img)
		if(pred[0][0]>=0.5):
			return jsonify("VIOLENT")
		output = client.check('nudity').set_url(img_url)
		if(output['nudity']['safe']<0.5):
			return jsonify("NUDITY")
		#extractedInformation=api.ocr_url(img_url)
		if(extractedInformation==""):
			return jsonify("NORMAL")
	elif(t=="audio"):
		r=sr.Recognizer()
		urllib.request.urlretrieve(data["audio"], "audio.wav")
		with sr.AudioFile("audio.wav") as source:
			audio=r.record(source)
			extractedInformation=r.recognize_google(audio,show_all=False)
			if(extractedInformation==""):
				return jsonify("NORMAL")
	elif(t=="text"):
		extractedInformation=data["text"]
		print(data["text"])
		#extractedInformation=str(request.args["text"])
		extractedInformation=extractedInformation.replace('\r', "").replace('\n'," ")
		extractedInformation=translator.translate(extractedInformation).text
	extractedInformation=[extractedInformation]
	sen_trans = vect.transform(extractedInformation)
	prediction=model.predict(sen_trans)[0]
	spam_trans=spam_vect.transform(extractedInformation)
	spam_prediction=spam_model.predict(spam_trans)[0]
	if(prediction>=0.5):
		return jsonify("OFFENSIVE")
	if(spam_prediction>=0.5):
		return jsonify("SPAM")
	else:
		return jsonify("NORMAL")
app.run(debug = True)
