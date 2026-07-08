from flask import Flask, request, jsonify, session
from flask_cors import CORS
from database import db
from routes.auth import auth_bp
from models import Owner, Pet, Doctor, Appointment
from config import Config
from routes.appointments import appointments_bp



app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(appointments_bp)
app.secret_key = "petclinic-secret-key"
app.register_blueprint(auth_bp)

db.init_app(app)
CORS(app)

with app.app_context():
    db.create_all()


#########################################################
# HEALTH CHECK
#########################################################

@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "Healthy",
        "application": "Pet Clinic API",
        "version": "1.0"
    })


#########################################################
# LOGIN
#########################################################

@app.route("/login", methods=["POST"])
def login():

    data = request.json

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "admin123":

        session["loggedIn"] = True

        return jsonify({
            "message": "Login Successful"
        })

    return jsonify({
        "message": "Invalid Username or Password"
    }), 401


#########################################################
# LOGOUT
#########################################################

@app.route("/logout")
def logout():

    session.clear()

    return jsonify({
        "message": "Logged Out"
    })


#########################################################
# DASHBOARD
#########################################################

@app.route("/dashboard", methods=["GET"])
def dashboard():

    return jsonify({

        "owners": Owner.query.count(),

        "pets": Pet.query.count(),

        "doctors": Doctor.query.count(),

        "appointments": Appointment.query.count()

    })


#########################################################
# GET ALL OWNERS
#########################################################

@app.route("/owners", methods=["GET"])
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

@app.route("/owners/<int:id>", methods=["GET"])
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

@app.route("/owners", methods=["POST"])
def create_owner():

    data = request.json

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

@app.route("/owners/<int:id>", methods=["PUT"])
def update_owner(id):

    owner = Owner.query.get_or_404(id)

    data = request.json

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

@app.route("/owners/<int:id>", methods=["DELETE"])
def delete_owner(id):

    owner = Owner.query.get_or_404(id)

    db.session.delete(owner)

    db.session.commit()

    return jsonify({

        "message": "Owner Deleted Successfully"

    })

#########################################################
# PET APIs
#########################################################

# Get All Pets
@app.route("/pets", methods=["GET"])
def get_pets():

    pets = Pet.query.all()

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


#########################################################
# Get Pet By ID
#########################################################

@app.route("/pets/<int:id>", methods=["GET"])
def get_pet(id):

    pet = Pet.query.get_or_404(id)

    return jsonify({

        "id": pet.id,
        "name": pet.name,
        "breed": pet.breed,
        "age": pet.age,
        "gender": pet.gender,
        "owner_id": pet.owner_id

    })


#########################################################
# Create Pet
#########################################################

@app.route("/pets", methods=["POST"])
def create_pet():

    data = request.get_json()

    try:

        owner = Owner.query.get(data["owner_id"])

        if owner is None:

            return jsonify({

                "message": "Owner Not Found"

            }), 404

        pet = Pet(

            name=data["name"],
            breed=data["breed"],
            age=data["age"],
            gender=data["gender"],
            owner_id=data["owner_id"]

        )

        db.session.add(pet)

        db.session.commit()

        return jsonify({

            "message": "Pet Created Successfully"

        }), 201

    except Exception as e:

        db.session.rollback()

        return jsonify({

            "message": str(e)

        }), 500


#########################################################
# Update Pet
#########################################################

@app.route("/pets/<int:id>", methods=["PUT"])
def update_pet(id):

    pet = Pet.query.get_or_404(id)

    data = request.get_json()

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
# Delete Pet
#########################################################

@app.route("/pets/<int:id>", methods=["DELETE"])
def delete_pet(id):

    pet = Pet.query.get_or_404(id)

    db.session.delete(pet)

    db.session.commit()

    return jsonify({

        "message": "Pet Deleted Successfully"

    })


#########################################################
# Search Pets
#########################################################

@app.route("/pets/search/<string:name>", methods=["GET"])
def search_pet(name):

    pets = Pet.query.filter(Pet.name.like(f"%{name}%")).all()

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


#########################################################
# DOCTOR APIs
#########################################################

# Get All Doctors
@app.route("/doctors", methods=["GET"])
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

@app.route("/doctors/<int:id>", methods=["GET"])
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

@app.route("/doctors", methods=["POST"])
def create_doctor():

    data = request.get_json()

    try:

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

    except Exception as e:

        db.session.rollback()

        return jsonify({

            "message": str(e)

        }), 500


#########################################################
# Update Doctor
#########################################################

@app.route("/doctors/<int:id>", methods=["PUT"])
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

@app.route("/doctors/<int:id>", methods=["DELETE"])
def delete_doctor(id):

    doctor = Doctor.query.get_or_404(id)

    db.session.delete(doctor)

    db.session.commit()

    return jsonify({

        "message": "Doctor Deleted Successfully"

    })


#########################################################
# Search Doctor
#########################################################

@app.route("/doctors/search/<string:name>", methods=["GET"])
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


#########################################################
# APPOINTMENT APIs
#########################################################

# Get All Appointments
@app.route("/appointments", methods=["GET"])
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


#########################################################
# Get Appointment By ID
#########################################################

@app.route("/appointments/<int:id>", methods=["GET"])
def get_appointment(id):

    appointment = Appointment.query.get_or_404(id)

    return jsonify({

        "id": appointment.id,
        "pet_id": appointment.pet_id,
        "doctor_id": appointment.doctor_id,
        "appointment_date": appointment.appointment_date.strftime("%Y-%m-%d %H:%M"),
        "status": appointment.status

    })


#########################################################
# Create Appointment
#########################################################

@app.route("/appointments", methods=["POST"])
def create_appointment():

    data = request.get_json()

    try:

        pet = Pet.query.get(data["pet_id"])

        if pet is None:

            return jsonify({

                "message": "Pet Not Found"

            }), 404

        doctor = Doctor.query.get(data["doctor_id"])

        if doctor is None:

            return jsonify({

                "message": "Doctor Not Found"

            }), 404

        appointment = Appointment(

            pet_id=data["pet_id"],
            doctor_id=data["doctor_id"],
            appointment_date=data["appointment_date"],
            status=data.get("status", "Scheduled")

        )

        db.session.add(appointment)

        db.session.commit()

        return jsonify({

            "message": "Appointment Booked Successfully"

        }), 201

    except Exception as e:

        db.session.rollback()

        return jsonify({

            "message": str(e)

        }), 500


#########################################################
# Update Appointment
#########################################################

@app.route("/appointments/<int:id>", methods=["PUT"])
def update_appointment(id):

    appointment = Appointment.query.get_or_404(id)

    data = request.get_json()

    appointment.pet_id = data["pet_id"]
    appointment.doctor_id = data["doctor_id"]
    appointment.appointment_date = data["appointment_date"]
    appointment.status = data["status"]

    db.session.commit()

    return jsonify({

        "message": "Appointment Updated Successfully"

    })


#########################################################
# Delete Appointment
#########################################################

@app.route("/appointments/<int:id>", methods=["DELETE"])
def delete_appointment(id):

    appointment = Appointment.query.get_or_404(id)

    db.session.delete(appointment)

    db.session.commit()

    return jsonify({

        "message": "Appointment Deleted Successfully"

    })


#########################################################
# Search Appointment by Status
#########################################################

@app.route("/appointments/status/<string:status>", methods=["GET"])
def search_appointment(status):

    appointments = Appointment.query.filter_by(status=status).all()

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


#########################################################
# ROOT API
#########################################################

@app.route("/", methods=["GET"])
def home():

    return jsonify({

        "application": "Pet Clinic Management System",

        "version": "1.0",

        "status": "Running"

    })


#########################################################
# RUN APPLICATION
#########################################################

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )          