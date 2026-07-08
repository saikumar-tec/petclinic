from flask import Blueprint, request, jsonify
from database import db
from models import Appointment, Pet, Doctor
from datetime import datetime

appointments_bp = Blueprint("appointments", __name__)


@appointments_bp.route("/appointments", methods=["GET"])
def get_appointments():

    appointments = Appointment.query.all()

    result = []

    for appointment in appointments:

        result.append({

            "id": appointment.id,
            "pet_id": appointment.pet_id,
            "doctor_id": appointment.doctor_id,
            "appointment_date": appointment.appointment_date.strftime("%Y-%m-%d %H:%M"),
            "status": appointment.status

        })

    return jsonify(result)

@appointments_bp.route("/appointments/<int:id>", methods=["GET"])
def get_appointment(id):

    appointment = Appointment.query.get_or_404(id)

    return jsonify({

        "id": appointment.id,
        "pet_id": appointment.pet_id,
        "doctor_id": appointment.doctor_id,
        "appointment_date": appointment.appointment_date.strftime("%Y-%m-%d %H:%M"),
        "status": appointment.status

    })

@appointments_bp.route("/appointments", methods=["POST"])
def create_appointment():

    data = request.json

    pet = Pet.query.get(data["pet_id"])

    if pet is None:

        return jsonify({"message": "Pet Not Found"}),404

    doctor = Doctor.query.get(data["doctor_id"])

    if doctor is None:

        return jsonify({"message":"Doctor Not Found"}),404

    appointment = Appointment(

        pet_id=data["pet_id"],

        doctor_id=data["doctor_id"],

        appointment_date=datetime.strptime(
            data["appointment_date"],
            "%Y-%m-%dT%H:%M"
        ),

        status=data.get("status","Scheduled")

    )

    db.session.add(appointment)

    db.session.commit()

    return jsonify({

        "message":"Appointment Created Successfully"

    }),201


@appointments_bp.route("/appointments/<int:id>", methods=["PUT"])
def update_appointment(id):

    appointment = Appointment.query.get_or_404(id)

    data = request.json

    appointment.pet_id = data["pet_id"]

    appointment.doctor_id = data["doctor_id"]

    appointment.appointment_date = datetime.strptime(
        data["appointment_date"],
        "%Y-%m-%dT%H:%M"
    )

    appointment.status = data["status"]

    db.session.commit()

    return jsonify({

        "message":"Appointment Updated Successfully"

    })            

@appointments_bp.route("/appointments/<int:id>", methods=["DELETE"])
def delete_appointment(id):

    appointment = Appointment.query.get_or_404(id)

    db.session.delete(appointment)

    db.session.commit()

    return jsonify({

        "message":"Appointment Deleted Successfully"

    })


@appointments_bp.route("/appointments/status/<status>", methods=["GET"])
def search_by_status(status):

    appointments = Appointment.query.filter_by(
        status=status
    ).all()

    result=[]

    for appointment in appointments:

        result.append({

            "id":appointment.id,

            "pet_id":appointment.pet_id,

            "doctor_id":appointment.doctor_id,

            "appointment_date":appointment.appointment_date.strftime("%Y-%m-%d %H:%M"),

            "status":appointment.status

        })

    return jsonify(result)
