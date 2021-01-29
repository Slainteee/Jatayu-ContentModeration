import pickle

def fmodel():
    model=pickle.load(open(r'PhishingWebsite\trainedmodel\model_random_forest.pkl','rb'))
    return model
