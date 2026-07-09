// =====================================
// Pet Clinic Management System
// doctors.js
// =====================================

checkLogin();

const DOCTOR_API = API_URL + "/doctors";


// ================================
// Load Doctors
// ================================

function loadDoctors() {

    fetch(DOCTOR_API)

    .then(response => response.json())

    .then(data => {

        const table = document.getElementById("doctorsTable");

        table.innerHTML = "";

        data.forEach(doctor => {

            table.innerHTML += `
                <tr>
                    <td>${doctor.id}</td>
                    <td>${doctor.name}</td>
                    <td>${doctor.specialization}</td>
                    <td>${doctor.phone}</td>
                </tr>
            `;

        });

    })

    .catch(error => {

        console.error("Error Loading Doctors:", error);

    });

}


// ================================
// Add Doctor
// ================================

document.getElementById("doctorForm").addEventListener("submit", function(e){

    e.preventDefault();

    const doctor = {

        name: document.getElementById("name").value,
        specialization: document.getElementById("specialization").value,
        phone: document.getElementById("phone").value

    };

    fetch(DOCTOR_API, {

        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(doctor)

    })
    .then(response => response.json())
    .then(data => {

        alert(data.message);

        document.getElementById("doctorForm").reset();

        loadDoctors();

    })
    .catch(error => {

        console.error("Error Adding Doctor:", error);

    });

});