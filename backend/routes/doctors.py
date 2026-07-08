from flask import Blueprint, request, jsonify
from database import db
from models import Doctor

# Create Blueprint
doctors_bp = Blueprint("doctors", __name__)


#########################################################
# Get All Doctors
#########################################################

@doctors_bp.route("/doctors", methods=["GET"])
def get_doctors():

    doctors = Doctor.query.all()

    result = []

    for doctor in doctors:

        result.append({

            "id": doctor.id,
            "name": doctor.name,
            "specialization": doctor.specialization,
            "phone": doctor.phone

        })

    return jsonify(result)


#########################################################
# Get Doctor By ID
#########################################################

@doctors_bp.route("/doctors/<int:id>", methods=["GET"])
def get_doctor(id):

    doctor = Doctor.query.get_or_404(id)

    return jsonify({

        "id": doctor.id,
        "name": doctor.name,
        "specialization": doctor.specialization,
        "phone": doctor.phone

    })


#########################################################
# Create Doctor
#########################################################

@doctors_bp.route("/doctors", methods=["POST"])
def create_doctor():

    data = request.get_json()

    doctor = Doctor(

        name=data["name"],
        specialization=data["specialization"],
        phone=data["phone"]

    )

    db.session.add(doctor)

    db.session.commit()

    return jsonify({

        "message": "Doctor Created Successfully"

    }), 201


#########################################################
# Update Doctor
#########################################################

@doctors_bp.route("/doctors/<int:id>", methods=["PUT"])
def update_doctor(id):

    doctor = Doctor.query.get_or_404(id)

    data = request.get_json()

    doctor.name = data["name"]
    doctor.specialization = data["specialization"]
    doctor.phone = data["phone"]

    db.session.commit()

    return jsonify({

        "message": "Doctor Updated Successfully"

    })


#########################################################
# Delete Doctor
#########################################################

@doctors_bp.route("/doctors/<int:id>", methods=["DELETE"])
def delete_doctor(id):

    doctor = Doctor.query.get_or_404(id)

    db.session.delete(doctor)

    db.session.commit()

    return jsonify({

        "message": "Doctor Deleted Successfully"

    })


#########################################################
# Search Doctor By Name
#########################################################

@doctors_bp.route("/doctors/search/<string:name>", methods=["GET"])
def search_doctor(name):

    doctors = Doctor.query.filter(
        Doctor.name.like(f"%{name}%")
    ).all()

    result = []

    for doctor in doctors:

        result.append({

            "id": doctor.id,
            "name": doctor.name,
            "specialization": doctor.specialization,
            "phone": doctor.phone

        })

    return jsonify(result)