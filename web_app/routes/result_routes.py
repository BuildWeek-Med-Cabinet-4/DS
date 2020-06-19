from flask import Blueprint, jsonify, request

result_routes = Blueprint("result_routes", __name__)

@result_routes.route('/strains')
def strain():
    some_results=[{"strain":"blah" , "type": "duh" }]
    return jsonify (some_results)


@result_routes.route('/effects')
def effects():
    some_results2=[{"strain":"blah" , "type": "duh" }]
    return jsonify (some_results2)


@result_routes.route('/recommendations')
def recommendation():
    some_results3={"strain":"blah" , "type": "duh" }
    
    breakpoint()
    
    return jsonify (some_results3)