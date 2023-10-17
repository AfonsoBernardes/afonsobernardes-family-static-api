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
john_jackson = Person("John", 33, [7, 13, 22], 1)
jackson_family.add_member(john_jackson)

jane_jackson = Person("Jane", 35, [10, 14, 3], 2)
jackson_family.add_member(jane_jackson)

jimmy_jackson = Person("Jimmy", 5, [1], 3)
jackson_family.add_member(jimmy_jackson)



# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200


@app.route('/member/<int:member_id>', methods=['GET', 'DELETE'])
def get_member(member_id):
    # this is how you can use the Family datastructure by calling its methods
    if request.method == 'GET':
        member = jackson_family.get_member(member_id)
        return member

    elif request.method == 'DELETE':
        jackson_family.delete_member(member_id)
        response_body = {
            'done': True,
        }
        return jsonify(response_body), 200

@app.route('/member', methods=['POST'])
def add_family_member():
    # this is how you can use the Family datastructure by calling its methods
    new_member_data = request.get_json()
    if "id" in new_member_data.keys():
        new_member = Person(new_member_data["first_name"],
                            new_member_data["age"],
                            new_member_data["lucky_numbers"],
                            new_member_data["id"]
                    )
    else:
        new_member = Person(new_member_data["first_name"],
                            new_member_data["age"],
                            new_member_data["lucky_numbers"]
                    )

    jackson_family.add_member(new_member)
    response_body = {
        "status": "New member added.",
        "family": jackson_family._members
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
