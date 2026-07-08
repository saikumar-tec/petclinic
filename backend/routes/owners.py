from flask import Blueprint, request, jsonify
from database import db
from models import Owner

# Blueprint
owners_bp = Blueprint("owners", __name__)


#########################################################
# GET ALL OWNERS
#########################################################

@owners_bp.route("/owners", methods=["GET"])
def get_owners():

    owners = Owner.query.all()

    result = []

    for owner in owners:

        result.append({

            "id": owner.id,
            "name": owner.name,
            "phone": owner.phone,
            "email": owner.email,
            "address": owner.address

        })

    return jsonify(result)


#########################################################
# GET OWNER BY ID
#########################################################

@owners_bp.route("/owners/<int:id>", methods=["GET"])
def get_owner(id):

    owner = Owner.query.get_or_404(id)

    return jsonify({

        "id": owner.id,
        "name": owner.name,
        "phone": owner.phone,
        "email": owner.email,
        "address": owner.address

    })


#########################################################
# CREATE OWNER
#########################################################

@owners_bp.route("/owners", methods=["POST"])
def create_owner():

    data = request.get_json()

    owner = Owner(

        name=data["name"],
        phone=data["phone"],
        email=data["email"],
        address=data["address"]

    )

    db.session.add(owner)

    db.session.commit()

    return jsonify({

        "message": "Owner Created Successfully"

    }), 201


#########################################################
# UPDATE OWNER
#########################################################

@owners_bp.route("/owners/<int:id>", methods=["PUT"])
def update_owner(id):

    owner = Owner.query.get_or_404(id)

    data = request.get_json()

    owner.name = data["name"]
    owner.phone = data["phone"]
    owner.email = data["email"]
    owner.address = data["address"]

    db.session.commit()

    return jsonify({

        "message": "Owner Updated Successfully"

    })


#########################################################
# DELETE OWNER
#########################################################

@owners_bp.route("/owners/<int:id>", methods=["DELETE"])
def delete_owner(id):

    owner = Owner.query.get_or_404(id)

    db.session.delete(owner)

    db.session.commit()

    return jsonify({

        "message": "Owner Deleted Successfully"

    })


#########################################################
# SEARCH OWNER
#########################################################

@owners_bp.route("/owners/search/<string:name>", methods=["GET"])
def search_owner(name):

    owners = Owner.query.filter(
        Owner.name.like(f"%{name}%")
    ).all()

    result = []

    for owner in owners:

        result.append({

            "id": owner.id,
            "name": owner.name,
            "phone": owner.phone,
            "email": owner.email,
            "address": owner.address

        })

    return jsonify(result)