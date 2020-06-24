
import requests
import json
from flask import Blueprint, request, jsonify, render_template, Flask
from flask_cors import CORS, cross_origin
import pandas as pd
import re
import os

# *************************************************************************** #
# ML Engineers imports. Must be formated like this or else pickled model won't
# work
from sklearn.feature_extraction import text 
# TFIDF / Word Embeddings
from sklearn.feature_extraction.text import TfidfVectorizer
# Similarity
from sklearn.metrics.pairwise import cosine_similarity
# Deployment
import pickle
# *************************************************************************** #
# Activating CORS
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
# *************************************************************************** #

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
    vect_path = os.path.join('models', 
                                    'pickled_vectorizer.pkl')

    df_path = os.path.join('models', 
                            'pickled_df.pkl')

    dtm_path = os.path.join('models', 
                            'pickled_dtm.pkl')

    return (vect_path, df_path, dtm_path)

def load_models():
    '''
    Helper function for loading pickled models
    '''
    vect_path, df_path, dtm_path = safe_paths()

    # load the model from disk
    pickled_vectorizer = pickle.load(open(vect_path, 'rb'))
    strain_list = pd.read_pickle(df_path)
    pickled_dtm = pickle.load(open(dtm_path, 'rb'))

    return (pickled_vectorizer, strain_list, pickled_dtm)

# *************************************************************************** #
# Loading the pickled models in global memory, to increase response time of api
PICKLED_VECTORIZER, STRAIN_LIST, PICKLED_DTM = load_models()
# *************************************************************************** #

def find_rec_strains(p_strain):
    """
    This function takes in a preprocessed JSON from preprocess_strain(strain).
    It creates a JSON containing info on the 5 most similar strains
    """

    # vect_path, df_path, dtm_path = safe_paths()

    # # load the model from disk
    # pickled_vectorizer = pickle.load(open(vect_path, 'rb'))
    # strain_list = pd.read_pickle(df_path)
    # pickled_dtm = pickle.load(open(dtm_path, 'rb'))

    # Transforms preprocessed strain and appends
    input_dtm = pd.DataFrame((PICKLED_VECTORIZER.transform(p_strain['combined_text'])).todense(), columns=PICKLED_VECTORIZER.get_feature_names())
    dtm_1 = (PICKLED_DTM.append(input_dtm)).reset_index(drop=True)

    # Calculate similarity of all strains
    cosine_df = pd.DataFrame(cosine_similarity(dtm_1))

    #Grab top 5 results that are most similar to user inputted strain
    cosine_results = (pd.DataFrame(cosine_df[cosine_df[0] < 1][len(cosine_df)-1].sort_values(ascending=False)[1:6])).reset_index()
    cos_results = cosine_results['index'].values.tolist()
    recs = []
    for each in cos_results:
        temp = STRAIN_LIST.iloc[each]
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

    #print(cleaned)

    return cleaned

@from_back_routes.route('/send/', methods = ["POST"])
@cross_origin()
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

    #print(clean_recs)

    #print(jsonify(clean_recs))

    # json_recs = jsonify(
    #     UserID = clean_recs['UserID'],
    #     Strain = clean_recs['Strain'],
    #     Type = clean_recs['Type'],
    #     Effects = clean_recs['Effects'],
    #     Flavor = clean_recs['Flavor'],
    #     Description = clean_recs['Description']
    # )

    response = app.response_class(
        json.dumps(clean_recs, sort_keys = False, indent = 4),
        mimetype = app.config['JSONIFY_MIMETYPE']
    )

    return response

@from_back_routes.route('/json')
def parse_json2():
    
    backend_url1 = f"https://raw.githubusercontent.com/jae-finger/med_cabinet_4/master/test_strain.json"
    response1 = requests.get(backend_url1)
    res_text= response1.text
    parsed_response1 = json.loads(res_text)    

    return jsonify(parsed_response1)

@from_back_routes.route('/')
def land_page():
    return render_template("index.html", message = "A datascience API for serving up cannabis strains to a webdev team")

@from_back_routes.route('/references')
def refer_page():
    return render_template("references.html", message = "A datascience API for serving up cannabis strains to a webdev team")