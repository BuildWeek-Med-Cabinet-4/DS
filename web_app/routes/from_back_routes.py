
import requests
import json
from flask import Blueprint, request, jsonify
import pandas as pd
import re

from_back_routes = Blueprint("from_back_routes", __name__)

DF_FEATURES = ['Strain', 'Type', 'Effects', "Flavor", 'Description']
def clean_payload(pay_load):
    input_strain = pd.DataFrame.from_records(pay_load, index=[0], columns=['Strain', 'Type', 'Effects', 'Flavor', 'Description'])

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

    return df.to_json()



    #Strain =pyld ["Strain"]
    #Type = pyld ["Type"]
    #Rating = pyld ["Rating"]
    #Effects = pyld ["Effects"]
    #Flavor = pyld ["Flavor"]
    #Description = pyld ["Description"]


    #return '''{} {} {} {} {} {}''' .format(Strain, Type, Rating, Effects, Flavor, Description)

@from_back_routes.route('/send/json')
def parse_json2():
    
    backend_url1 = f"https://raw.githubusercontent.com/jae-finger/med_cabinet_4/master/test_strain.json"
    response1 = requests.get(backend_url1)
    res_text= response1.text
    parsed_response1 = json.loads(res_text)

    return jsonify(parsed_response1)



    #Strain =parsed_response1 ["Strain"]
    #Type = parsed_response1 ["Type"]
    ##Rating = parsed_response1 ["Rating"]
    #Effects = parsed_response1 ["Effects"]
    #Flavor = parsed_response1 ["Flavor"]
    #Description = parsed_response1 ["Description"]
#
    #return jsonify(parsed_response1)

    
























''''
# Using requests
backend_url1 = f"https://api.openaq.org/v1/cities"
backend_url2 = f"https://api.openaq.org/v1/cities"
backend_url3 = f"https://api.openaq.org/v1/countries"
backend_url4 = f"https://api.openaq.org/v1/fetches"


backend_list=[backend_url1, backend_url2, backend_url3, backend_url4]


@from_back_routes.route('/parse')
def parse_json():
    for link in backend_list:
        response=requests.get(link)
        #parse_json=json.loads(response)

        breakpoint()
    return response





response1 = requests.get(backend_url1)
response2 = requests.get(backend_url2)
response3 = requests.get(backend_url3)
response4 = requests.get(backend_url4)

parsed_response1 = json.loads(response1.text)
parsed_response1 = json.loads(response2.text)
parsed_response1 = json.loads(response3.text)
parsed_response1 = json.loads(response4.text)
'''
