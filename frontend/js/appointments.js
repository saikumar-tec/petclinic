// =====================================
// Pet Clinic Management System
// appointments.js
// =====================================

checkLogin();

const APPOINTMENT_API = API_URL + "/appointments";


// =====================================
// Load Appointments
// =====================================

function loadAppointments() {

    fetch(APPOINTMENT_API)

    .then(response => response.json())

    .then(data => {

        const table = document.getElementById("appointmentsTable");

        table.innerHTML = "";

        data.forEach(appointment => {

            table.innerHTML += `
                <tr>
                    <td>${appointment.id}</td>
                    <td>${appointment.pet_id}</td>
                    <td>${appointment.doctor_id}</td>
                    <td>${appointment.appointment_date}</td>
                    <td>${appointment.status}</td>
                </tr>
            `;

        });

    })

    .catch(error => {

        console.error("Error Loading Appointments:", error);

    });

}


// =====================================
// Add Appointment
// =====================================

document.getElementById("appointmentForm").addEventListener("submit", function(e){

    e.preventDefault();

    const appointment = {

        pet_id: parseInt(document.getElementById("pet_id").value),

        doctor_id: parseInt(document.getElementById("doctor_id").value),

        appointment_date: document.getElementById("appointment_date").value,

        status: document.getElementById("status").value

    };

    fetch(APPOINTMENT_API, {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(appointment)

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        document.getElementById("appointmentForm").reset();

        loadAppointments();

    })

    .catch(error => {

        console.error("Error Adding Appointment:", error);

    });

});


// =====================================
// Load Appointments on Page Load
// =====================================

window.onload = function () {

    loadAppointments();

};