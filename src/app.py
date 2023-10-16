"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure, Person
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Add members to family.
john_jackson = Person("John", 33, [7, 13, 22])
jackson_family.add_member(john_jackson)

jane_jackson = Person("Jane", 35, [10, 14, 3])
jackson_family.add_member(jane_jackson)

jimmy_jackson = Person("Jimmy", 5, [1])
jackson_family.add_member(jimmy_jackson)

afonso_jackson = Person("Afonso", 25, [7, 12])

print("OLD", jackson_family._members)
jackson_family.update_member(jackson_family._members[0]["id"], afonso_jackson)
print("NEW", jackson_family._members)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }


    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
