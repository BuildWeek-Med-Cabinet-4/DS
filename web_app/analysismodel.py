'''
import os
import pickle as pickle
import pandas as pd
import json

def train_and_save_model():
    """Train dataset and save model as pickled file, (done in colab by jon)
    """

    #TODO: load dataset

    #TODO: instantiate a model = classifier

    #TODO: fit training set into model

    #TODO: jsonify classifier (strain_json)

    '''pickling json results'''
    pickle_to = open("pickled_file", 'wb')
    pkl.dump(strain_json, pickle_to)   

    return strain_json


model_file = <"pickled_file">      # pre-trained model
def load_model():
    """Load pickled pretrained data
    """
    strain_file = open(model_file, 'rb')
    #TODO: convert json file to model-readable format
    saved_strain=pkl.load(strain_file)
    return saved_strain

if __name__ == "__main__":

    train_and_save_model()   

    clf = load_model()
    print("CLASSIFIER:", clf)

    #TODO: X, y = load training dataset 
    
    #TODO: inputs = user-given features

    #TODO: result = clf.predict(inputs)


'''
