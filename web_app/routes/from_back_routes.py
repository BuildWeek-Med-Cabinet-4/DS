
import requests
import json
from flask import Blueprint, request, jsonify
import pandas as pd
import re
import os


# ML Engineers imports. Must be formated like this or else pickled model won't
# work
from sklearn.feature_extraction import text 
# TFIDF / Word Embeddings
from sklearn.feature_extraction.text import TfidfVectorizer
# Similarity
from sklearn.metrics.pairwise import cosine_similarity
# Deployment
import pickle

from_back_routes = Blueprint("from_back_routes", __name__)

DF_FEATURES = ['Strain', 'Type', 'Effects', "Flavor", 'Description']
def clean_payload(pay_load):
    '''
    Quick helper function for cleaning the payload
    '''
    input_strain = pd.DataFrame.from_records(pay_load, index=[0], columns=['UserID', 'Strain', 'Type', 'Effects', 'Flavor', 'Description'])

    for each in DF_FEATURES:
      input_strain[each] = input_strain[each].apply(lambda x: x.lower())
      input_strain[each] = input_strain[each].apply(lambda x: re.sub('[^a-zA-Z 0-9]', ' ', x))
    
    # Combines text
    input_strain['combined_text'] = input_strain['Type'] + ' ' + input_strain['Effects'] + ' ' + input_strain['Flavor'] + input_strain['Description'] + ' '
    
    return input_strain

def safe_paths():
    '''
    Quick helper to make platfor independant file paths
    Returns - (vectorizer, df, dtm)
    '''
    vectorizer_path = os.path.join('models', 
                                    'pickled_vectorizer.pkl')

    df_path = os.path.join('models', 
                            'pickled_df.pkl')

    dtm_path = os.path.join('models', 
                            'pickled_dtm.pkl')

    return (vectorizer_path, df_path, dtm_path)

def find_rec_strains(p_strain):
    """
    This function takes in a preprocessed JSON from preprocess_strain(strain).
    It creates a JSON containing info on the 5 most similar strains
    """

    vectorizer_path, df_path, dtm_path = safe_paths()

    # load the model from disk
    filename = 'pickled_vectorizer.pkl'
    pickled_vectorizer = pickle.load(open(vectorizer_path, 'rb'))
    strain_list = pd.read_pickle(df_path)
    pickled_dtm = pickle.load(open(dtm_path, 'rb'))

    # Transforms preprocessed strain and appends
    input_dtm = pd.DataFrame((pickled_vectorizer.transform(p_strain['combined_text'])).todense(), columns=pickled_vectorizer.get_feature_names())
    dtm_1 = (pickled_dtm.append(input_dtm)).reset_index(drop=True)

    # Calculate similarity of all strains
    cosine_df = pd.DataFrame(cosine_similarity(dtm_1))

    #Grab top 5 results that are most similar to user inputted strain
    cosine_results = (pd.DataFrame(cosine_df[cosine_df[0] < 1][len(cosine_df)-1].sort_values(ascending=False)[1:6])).reset_index()
    cos_results = cosine_results['index'].values.tolist()
    recs = []
    for each in cos_results:
        temp = strain_list.iloc[each]
        recs.append(temp)
        
    recs = pd.DataFrame(recs).iloc[0].to_json()
    print('Created predicted_recs.json')

    return recs

def clean_response(recs, userID):
    features = DF_FEATURES
    features.insert(0, 'UserID')

    temp = json.loads(recs)
    temp['UserID'] = userID

    cleaned = {}

    for f in features:
        cleaned[f] = temp[f]

    return json.dumps(cleaned)


@from_back_routes.route('/send/', methods = ["POST"])
def parse_json():
    print('Fetching payload')
    pyld = request.get_json()

    print('Preprocessing payload')
    preprocessed = clean_payload(pyld)

    print('Processing payload')
    recs = find_rec_strains(preprocessed)

    print('Preparing repsonse')
    clean_recs = clean_response(recs, pyld['UserID'])

    print('Sending response')

    return clean_recs



@from_back_routes.route('/')
def parse_json2():
    
    backend_url1 = f"https://raw.githubusercontent.com/jae-finger/med_cabinet_4/master/test_strain.json"
    response1 = requests.get(backend_url1)
    res_text= response1.text
    parsed_response1 = json.loads(res_text)

    return jsonify(parsed_response1)
