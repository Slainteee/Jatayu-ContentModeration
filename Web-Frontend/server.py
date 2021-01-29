import os
import urllib.request
from flask import *
from werkzeug.utils import secure_filename
import filetype
import requests
import json
import cv2
import cloudinary
import cloudinary.uploader as up
import os
cloudinary.config.update = ({
    'cloud_name':'drlf6gntz',
    'api_key': '894749617857176',
    'api_secret': 'Qp-ckIp4k_xIresVZF7Gms0WrPY'
})

url = 'http://localhost:5000/'

upload_folder = r".\static\uploads"

app = Flask(__name__)

app.secret_key = 'dsdsqqwqw'
contents=[]
@app.route('/')
def upload_form():

    return render_template('index.html')


@app.route('/', methods=['POST'])

def upload_image():


    try:
        text = request.form["text"]

        if text:
            t=[text,"text"]
            data = text
            j_data=json.dumps({"data":data,"type":"text"})
            headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
            r = requests.post(url, data=j_data, headers=headers)
            #print(r.text.split())
            if r.text.split()[0]=="true":

                if len(contents)==0 or contents[0]!=t:
                    contents.insert(0,t)
            else:
                flash("Invalid Text")
                return render_template("index.html",content=contents)

        else:
            file = request.files['files']
            filename = secure_filename(file.filename)
            path = os.path.join(upload_folder, filename)
            file.save(path)
            kind = filetype.guess(path)
            type,extension = str(kind.mime).split("/")
            #print(path)
            p=[path,type]
            #print(p)
            if type=="image":
                img=up.upload(path,cloud_name='drlf6gntz',api_key='894749617857176',api_secret='Qp-ckIp4k_xIresVZF7Gms0WrPY')
                img_url=img["url"]
                j_data = json.dumps({"data":img_url,"type":"image"})
                headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
                r = requests.post(url, data=j_data, headers=headers)
                #print(r.text.split())
                if r.text.split()[0]=="true":
                    if len(contents)==0 or contents[0]!=p:
                        contents.insert(0,p)
                else:
                    flash("Invalid Image")
                    return render_template("index.html",content=contents)


            elif type=="audio":
                audio=up.upload(path,cloud_name='drlf6gntz',api_key='894749617857176',api_secret='Qp-ckIp4k_xIresVZF7Gms0WrPY',resource_type="raw")
                audio_url=audio["url"]
                #print(audio_url)
                j_data = json.dumps({"data":audio_url,"type":"audio"})
                headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
                r = requests.post(url, data=j_data, headers=headers)
                #print(r.text.split())
                if r.text.split()[0]=="true":
                    if len(contents)==0 or contents[0]!=p:
                        contents.insert(0,p)
                else:
                    flash("Invalid Audio")
                    return render_template("index.html",content=contents)
            elif type=="video":
                vid=up.upload_large(path,cloud_name='drlf6gntz',api_key='894749617857176',api_secret='Qp-ckIp4k_xIresVZF7Gms0WrPY')
                vid_url=vid["url"]
                #print(vid_url)
                j_data = json.dumps({"data":vid_url,"type":"video"})
                headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
                r = requests.post(url, data=j_data, headers=headers)
                if r.text.split()[0]=="true":
                    if len(contents)==0 or contents[0]!=p:
                        contents.insert(0,p)
                else:
                    flash("Invalid Video")
                    return render_template("index.html",content=contents)

        return render_template("index.html",content=contents)
    except Exception as e:
        print(e)
        return render_template('index.html',content=contents)








if __name__ == "__main__":
    app.run(host='127.0.0.1',port=1025,debug=True)
