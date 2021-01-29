import numpy as np
from PhishingWebsite import feature_extraction
import PhishingWebsite.trainedmodel.model as tm
from sklearn.ensemble import RandomForestClassifier as rfc
#from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as lr
from flask import jsonify
import pickle
from googlesearch import search

#Importing dataset
"""data = np.loadtxt(r"dataset/dataset.csv", delimiter = ",")

#Seperating features and labels
X = data[: , :-1]
y = data[: , -1]

#Seperating training features, testing features, training labels & testing labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
clf = rfc()
clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)
#print(score*100)
"""
#pickle.dump(clf,open('trained-model/model_random_forest.pkl','wb'))

def getResult(url):




    model= tm.fmodel()

    X_new = []

    X_input = url
    X_new=feature_extraction.generate_data_set(X_input)
    X_new = np.array(X_new).reshape(1,-1)

    try:
        prediction = model.predict(X_new)
        if prediction == -1:
            return "Phishing Website"
        else:
            return "Legitimate Website"
    except:
        return "Phishing Website"
