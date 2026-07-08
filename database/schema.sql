CREATE DATABASE IF NOT EXISTS petclinic;

USE petclinic;

--------------------------------------------------------
-- Owners
--------------------------------------------------------

CREATE TABLE owners (

    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    phone VARCHAR(20) NOT NULL,

    email VARCHAR(100) UNIQUE,

    address VARCHAR(255)

);

--------------------------------------------------------
-- Pets
--------------------------------------------------------

CREATE TABLE pets (

    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    breed VARCHAR(100),

    age INT,

    gender VARCHAR(20),

    vaccination_status VARCHAR(50) DEFAULT 'Pending',

    owner_id INT NOT NULL,

    FOREIGN KEY(owner_id)
    REFERENCES owners(id)
    ON DELETE CASCADE

);

--------------------------------------------------------
-- Doctors
--------------------------------------------------------

CREATE TABLE doctors (

    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    specialization VARCHAR(100),

    phone VARCHAR(20),

    email VARCHAR(100)

);

--------------------------------------------------------
-- Appointments
--------------------------------------------------------

CREATE TABLE appointments (

    id INT AUTO_INCREMENT PRIMARY KEY,

    pet_id INT NOT NULL,

    doctor_id INT NOT NULL,

    appointment_date DATETIME,

    reason VARCHAR(255),

    status VARCHAR(50),

    notes TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
    REFERENCES pets(id)
    ON DELETE CASCADE,

    FOREIGN KEY(doctor_id)
    REFERENCES doctors(id)
    ON DELETE CASCADE

);

--------------------------------------------------------
-- Sample Owners
--------------------------------------------------------

INSERT INTO owners(name,phone,email,address)

VALUES

('John Smith','9876543210','john@gmail.com','Hyderabad'),

('David Kumar','9876543222','david@gmail.com','Bangalore'),

('Sara Ali','9999999999','sara@gmail.com','Chennai');

--------------------------------------------------------
-- Sample Pets
--------------------------------------------------------

INSERT INTO pets

(name,breed,age,gender,vaccination_status,owner_id)

VALUES

('Bruno','Labrador',3,'Male','Completed',1),

('Tom','Persian Cat',2,'Male','Pending',2),

('Bella','Golden Retriever',1,'Female','Completed',3);

--------------------------------------------------------
-- Sample Doctors
--------------------------------------------------------

INSERT INTO doctors

(name,specialization,phone,email)

VALUES

('Dr. Raj','General Vet','8888888888','raj@clinic.com'),

('Dr. Priya','Surgery','7777777777','priya@clinic.com');

--------------------------------------------------------
-- Sample Appointments
--------------------------------------------------------

INSERT INTO appointments

(pet_id,doctor_id,appointment_date,reason,status)

VALUES

(1,1,'2026-06-30 10:00:00','Vaccination','Scheduled'),

(2,2,'2026-07-01 11:30:00','Health Check','Scheduled');