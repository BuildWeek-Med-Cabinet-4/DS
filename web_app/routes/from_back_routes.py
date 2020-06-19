
import requests
import json
from flask import Blueprint, request, jsonify
import pandas as pd
import re

from_back_routes = Blueprint("from_back_routes", __name__)

DF_FEATURES = ['Strain', 'Type', 'Effects', "Flavor", 'Description']
def clean_payload(pay_load):
    input_strain = pd.DataFrame.from_records(pay_load, index=[0], columns=['UserID', 'Strain', 'Type', 'Effects', 'Flavor', 'Description'])

    for each in DF_FEATURES:
      input_strain[each] = input_strain[each].apply(lambda x: x.lower())
      input_strain[each] = input_strain[each].apply(lambda x: re.sub('[^a-zA-Z 0-9]', ' ', x))
    
    # Combines text
    input_strain['combined_text'] = input_strain['Type'] + ' ' + input_strain['Effects'] + ' ' + input_strain['Flavor'] + input_strain['Description'] + ' '
    
    return input_strain


def preprocessing(df):
    pass


@from_back_routes.route('/send/', methods = ["POST"])
def parse_json():                         
    pyld = request.get_json()
    df = clean_payload(pyld)
    

    return df.drop(columns=['combined_text']).iloc[0].to_json()


@from_back_routes.route('/send/json')
def parse_json2():
    
    backend_url1 = f"https://raw.githubusercontent.com/jae-finger/med_cabinet_4/master/test_strain.json"
    response1 = requests.get(backend_url1)
    res_text= response1.text
    parsed_response1 = json.loads(res_text)

    return jsonify(parsed_response1)
