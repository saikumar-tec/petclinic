from database import db
from datetime import datetime

############################################################
# Owner Model
############################################################

class Owner(db.Model):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True)
    address = db.Column(db.String(255))

    # Relationship
    pets = db.relationship(
        "Pet",
        backref="owner",
        lazy=True,
        cascade="all, delete"
    )

    def __repr__(self):
        return f"<Owner {self.name}>"

############################################################
# Pet Model
############################################################

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    breed = db.Column(db.String(100))

    age = db.Column(db.Integer)

    gender = db.Column(db.String(20))

    vaccination_status = db.Column(
        db.String(100),
        default="Pending"
    )

    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("owners.id"),
        nullable=False
    )

    appointments = db.relationship(
        "Appointment",
        backref="pet",
        lazy=True,
        cascade="all, delete"
    )

    def __repr__(self):
        return f"<Pet {self.name}>"

############################################################
# Doctor Model
############################################################

class Doctor(db.Model):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False
    )

    specialization = db.Column(
        db.String(100),
        nullable=False
    )

    phone = db.Column(db.String(20))

    email = db.Column(
        db.String(100),
        unique=True
    )

    appointments = db.relationship(
        "Appointment",
        backref="doctor",
        lazy=True,
        cascade="all, delete"
    )

    def __repr__(self):
        return f"<Doctor {self.name}>"

############################################################
# Appointment Model
############################################################

class Appointment(db.Model):
    __tablename__ = "appointments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    pet_id = db.Column(
        db.Integer,
        db.ForeignKey("pets.id"),
        nullable=False
    )

    doctor_id = db.Column(
        db.Integer,
        db.ForeignKey("doctors.id"),
        nullable=False
    )

    appointment_date = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    reason = db.Column(
        db.String(255)
    )

    status = db.Column(
        db.String(50),
        default="Scheduled"
    )

    notes = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Appointment {self.id}>"