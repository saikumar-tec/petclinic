from flask import Blueprint, request, jsonify
from database import db
from models import Pet, Owner

# Blueprint
pets_bp = Blueprint("pets", __name__)


#########################################################
# GET ALL PETS
#########################################################

@pets_bp.route("/pets", methods=["POST"])
def create_pet():

    data = request.get_json()

    if not data:
        return jsonify({"message":"No JSON received"}),400

    owner_id = data.get("owner_id")

    if owner_id is None:
        return jsonify({"message":"Owner ID is required"}),400

    owner = Owner.query.get(owner_id)

    if owner is None:
        return jsonify({"message":"Owner Not Found"}),404

    pet = Pet(
        name=data.get("name"),
        breed=data.get("breed"),
        age=data.get("age"),
        gender=data.get("gender"),
        vaccination_status=data.get("vaccination_status","Pending"),
        owner_id=owner_id
    )

    db.session.add(pet)
    db.session.commit()

    return jsonify({
        "message":"Pet Created Successfully",
        "id":pet.id
    }),201


#########################################################
# UPDATE PET
#########################################################

@pets_bp.route("/pets/<int:id>", methods=["PUT"])
def update_pet(id):

    pet = Pet.query.get_or_404(id)

    data = request.get_json()

    owner = Owner.query.get(data["owner_id"])

    if owner is None:

        return jsonify({

            "message": "Owner Not Found"

        }), 404

    pet.name = data["name"]
    pet.breed = data["breed"]
    pet.age = data["age"]
    pet.gender = data["gender"]
    pet.owner_id = data["owner_id"]

    db.session.commit()

    return jsonify({

        "message": "Pet Updated Successfully"

    })


#########################################################
# DELETE PET
#########################################################

@pets_bp.route("/pets/<int:id>", methods=["DELETE"])
def delete_pet(id):

    pet = Pet.query.get_or_404(id)

    db.session.delete(pet)

    db.session.commit()

    return jsonify({

        "message": "Pet Deleted Successfully"

    })


#########################################################
# SEARCH PET
#########################################################

@pets_bp.route("/pets/search/<string:name>", methods=["GET"])
def search_pet(name):

    pets = Pet.query.filter(
        Pet.name.like(f"%{name}%")
    ).all()

    result = []

    for pet in pets:

        result.append({

            "id": pet.id,
            "name": pet.name,
            "breed": pet.breed,
            "age": pet.age,
            "gender": pet.gender,
            "owner_id": pet.owner_id

        })

    return jsonify(result)