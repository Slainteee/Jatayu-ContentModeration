import os

import urllib.request
from flask import *
from werkzeug.utils import secure_filename
import filetype

upload_folder = r".\static\uploads"

app = Flask(__name__)


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
            if len(contents)==0 or contents[0]!=t:
                contents.insert(0,t)
        else:
            file = request.files['files']
            filename = secure_filename(file.filename)
            path = os.path.join(upload_folder, filename)
            file.save(path)
            kind = filetype.guess(path)
            type,extension = str(kind.mime).split("/")

            p=[path,type]
            #print(p)
            if len(contents)==0 or contents[0]!=p:
                contents.insert(0,p)

        return render_template("index.html",content=contents)
    except:
        print("Error")
        return render_template('index.html',content=content)








if __name__ == "__main__":
    app.run(debug=True)
