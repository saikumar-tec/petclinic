// =====================================================
// Pet Clinic Management System
// Common JavaScript
// =====================================================

// Backend API URL
// Local Docker
const API_URL = "/api";

// For Kubernetes/AKS with Ingress later
// const API_URL = "/api";


// ======================================
// Login Check
// ======================================

function checkLogin() {

    const loggedIn = localStorage.getItem("loggedIn");

    if (loggedIn !== "true") {

        window.location.href = "login.html";

    }

}


// ======================================
// Logout
// ======================================

function logout() {

    localStorage.removeItem("loggedIn");

    window.location.href = "login.html";

}


// ======================================
// Dashboard Statistics
// ======================================

function loadDashboard() {

    fetch(API_URL + "/dashboard")

        .then(response => response.json())

        .then(data => {

            if (document.getElementById("petsCount"))
                document.getElementById("petsCount").innerHTML = data.pets;

            if (document.getElementById("ownersCount"))
                document.getElementById("ownersCount").innerHTML = data.owners;

            if (document.getElementById("doctorsCount"))
                document.getElementById("doctorsCount").innerHTML = data.doctors;

            if (document.getElementById("appointmentsCount"))
                document.getElementById("appointmentsCount").innerHTML = data.appointments;

        })

        .catch(error => {

            console.log("Dashboard API Error:", error);

        });

}


// ======================================
// Generic GET Request
// ======================================

async function getData(endpoint) {

    try {

        const response = await fetch(API_URL + endpoint);

        return await response.json();

    }

    catch (err) {

        console.log(err);

    }

}


// ======================================
// Generic POST Request
// ======================================

async function postData(endpoint, data) {

    try {

        const response = await fetch(API_URL + endpoint, {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(data)

        });

        return await response.json();

    }

    catch (err) {

        console.log(err);

    }

}


// ======================================
// Generic PUT Request
// ======================================

async function putData(endpoint, data) {

    try {

        const response = await fetch(API_URL + endpoint, {

            method: "PUT",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(data)

        });

        return await response.json();

    }

    catch (err) {

        console.log(err);

    }

}


// ======================================
// Generic DELETE Request
// ======================================

async function deleteData(endpoint) {

    try {

        const response = await fetch(API_URL + endpoint, {

            method: "DELETE"

        });

        return await response.json();

    }

    catch (err) {

        console.log(err);

    }

}


// ======================================
// Alert Helper
// ======================================

function showMessage(message) {

    alert(message);

}


// ======================================
// Delete Confirmation
// ======================================

function confirmDelete() {

    return confirm("Are you sure you want to delete this record?");

}


// ======================================
// Format Date
// ======================================

function formatDate(date) {

    return new Date(date).toLocaleString();

}


// ======================================
// Automatically Load Dashboard
// ======================================

if (window.location.pathname.includes("dashboard.html")) {

    checkLogin();

    loadDashboard();

}