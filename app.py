# API response: Return True if the query is OK else False
# -----------------------------------------------#

from flask import Flask, request, jsonify
import requests
import pickle
import pytesseract
import re
import urllib.request
import speech_recognition as sr
import torch
from PIL import Image
from io import BytesIO
import torchvision.transforms as transforms
import numpy as np
from sightengine.client import SightengineClient
from PhishingWebsite import phishing_detection
from urlextract import URLExtract


app = Flask(__name__)

# ---------------------------- Loading Models ---------------------------- #


# ------------------ Hate Speech ------------------- #

hate_model = pickle.load(
    open(r"hatespeech\saved_models\lr_model.pkl", "rb")
)  # path to hate speech model
hate_vect = pickle.load(
    open(r"hatespeech\saved_models\vectorizer.pkl", "rb")
)  # path to hate speech vectorizer


# ------------------ Spam Detection ------------------- #

spam_model = pickle.load(
    open(r"Spam Classifier\saved_models\lr_model.pkl", "rb")
)  # path to spam model
spam_vect = pickle.load(
    open(r"Spam Classifier\saved_models\vectorizer.pickle", "rb")
)  # path to spam vectorizer


# ------------------ Voilence Detection ------------------- #

violence_model = pickle.load(
    open(r"Violence-Detection\Pytorch-Implementation\saved_model\resnetmain.pkl", "rb")
)
checkpoint = torch.load(
    r"Violence-Detection\Pytorch-Implementation\saved_model\main_model.pt",
    map_location=torch.device("cpu"),
)
violence_model.load_state_dict(checkpoint["state_dict"])


#  ---------------------------------------------------------------------- #


custom_config = r"--oem 3 --psm 6"

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Set the tesseract path here
)

client = SightengineClient(
    "510188098", "WaehbLBjT3mYTmnxDsp3"
)  # Change Credentials Accordingly
extractor = URLExtract()


# -----------------------------------------------#

# To detect spam
def isspam(string: str) -> bool:
    """Checks for spam in the given string

    Args:
      string: A string to be checked

    Returns:
      Boolean

    """
    string = [string]
    sen_trans = spam_vect.transform(string)
    prediction = spam_model.predict(sen_trans)[0]  # 0->ham 1->spam
    return True if prediction else False


# To detect hate speech
def ishate(string: str) -> bool:
    """Checks for hate speech in the given string

    Args:
      string: A string to be checked

    Returns:
      Boolean

    """
    string = [string]
    sen_trans = hate_vect.transform(string)
    prediction = hate_model.predict(sen_trans)[0]  # 0->normal 1->toxic
    return True if prediction else False


# To detect violence
def isviolence(img) -> bool:
    """Checks for violence in the given image

    Args:
      img: A image object to be checked

    Returns:
      Boolean

    Raises:
      IOError – If the file cannot be found, or the image
                cannot be opened and identified

    """
    class_names = ["safe", "unsafe"]
    standard_normalization = transforms.Normalize(
        mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
    )
    try:

        def load_input_image(img):
            image = img.convert("RGB")
            prediction_transform = transforms.Compose(
                [
                    transforms.Resize(size=(224, 224)),
                    transforms.ToTensor(),
                    standard_normalization,
                ]
            )

            image = prediction_transform(image)[:3, :, :].unsqueeze(0)
            return image

        def predict_image(model, class_names, img):
            # load the image and return the predicted breed
            img = load_input_image(img)
            model = model.cpu()
            model.eval()
            idx = torch.argmax(model(img))
            return class_names[idx]

        def run_app(img):

            prediction = predict_image(violence_model, class_names, img)
            return prediction

        p = run_app(img)
        return 0 if p == "safe" else 1
    except IOError:
        return 1


# -----------------------------------------------#


@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        data = request.get_json()
        t = data["type"]

        if t == "audio":
            r = sr.Recognizer()
            path = r"Web-Frontend\static\uploads\audio.wav"  # Media storage path.
            urllib.request.urlretrieve(data["data"], path)
            with sr.AudioFile(path) as source:
                audio = r.record(source)
                extractedInformation = r.recognize_google(audio, show_all=False)
                if extractedInformation == "":
                    return jsonify(True)
                if re.search("\*", extractedInformation):
                    return jsonify(False)
                else:
                    if isspam(extractedInformation) or ishate(extractedInformation):
                        return jsonify(False)
                    else:
                        return jsonify(True)

        elif t == "video":
            vid_url = data["data"]
            output = client.check("nudity").video_sync(vid_url)
            for i in range(len(output["data"]["frames"])):
                if output["data"]["frames"][i]["nudity"]["safe"] > 0.5:
                    return jsonify(True)
            return jsonify(False)

        elif t == "image":

            img_url = data["data"]
            response = requests.get(img_url)
            img_org = Image.open(BytesIO(response.content))
            if isviolence(img_org):
                return jsonify(False)

            output = client.check("nudity").set_url(img_url)
            if output["nudity"]["safe"] < 0.5:
                return jsonify(False)

            img = img_org.resize((160, 160))
            img = np.array(img)
            extractedInformation = pytesseract.image_to_string(img_org)
            extractedInformation = re.sub(r"\n", " ", extractedInformation)
            extractedInformation = re.sub(r"\f", "", extractedInformation)
            if ishate(extractedInformation):
                return jsonify(False)
            if isspam(extractedInformation):
                return jsonify(False)

            return jsonify(True)

        elif t == "text":
            receivedtext = data["data"]
            urls = extractor.find_urls(receivedtext)
            if urls:
                result_list = []
                for i in urls:
                    result_list.append(phishing_detection.getResult(i))
                if "Phishing Website" in result_list:
                    return jsonify(False)

            if ishate(receivedtext):
                return jsonify(False)
            if isspam(receivedtext):
                return jsonify(False)
            return jsonify(True)
    else:
        return jsonify(True)


if __name__ == "__main__":
    app.run(debug=True)
