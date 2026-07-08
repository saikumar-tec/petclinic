/* ==========================================
   Pet Clinic Management System
   app.js
========================================== */

document.addEventListener("DOMContentLoaded", function () {
    console.log("Pet Clinic Loaded");

    initializeSearch();
    initializeForms();
});

/* ==========================================
   Toast Notification
========================================== */

function showToast(message, type = "success") {

    const toast = document.createElement("div");

    toast.className =
        `alert alert-${type} position-fixed top-0 end-0 m-3`;

    toast.style.zIndex = "9999";

    toast.innerHTML = message;

    document.body.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, 3000);
}

/* ==========================================
   Loading Spinner
========================================== */

function showLoader() {

    let loader = document.getElementById("loader");

    if (!loader) {

        loader = document.createElement("div");

        loader.id = "loader";

        loader.className = "loader position-fixed top-50 start-50";

        document.body.appendChild(loader);
    }

    loader.style.display = "block";
}

function hideLoader() {

    const loader = document.getElementById("loader");

    if (loader) {

        loader.style.display = "none";
    }
}

/* ==========================================
   Generic GET API
========================================== */

async function getData(url) {

    showLoader();

    try {

        const response = await fetch(url);

        const data = await response.json();

        hideLoader();

        return data;

    } catch (error) {

        hideLoader();

        showToast("Unable to load data", "danger");

        console.error(error);
    }
}

/* ==========================================
   Generic POST API
========================================== */

async function postData(url, data) {

    showLoader();

    try {

        const response = await fetch(url, {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(data)

        });

        hideLoader();

        return await response.json();

    } catch (error) {

        hideLoader();

        showToast("Request Failed", "danger");

        console.error(error);
    }
}

/* ==========================================
   Generic PUT API
========================================== */

async function updateData(url, data) {

    showLoader();

    try {

        const response = await fetch(url, {

            method: "PUT",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(data)

        });

        hideLoader();

        return await response.json();

    }

    catch (error) {

        hideLoader();

        showToast("Update Failed", "danger");

    }

}

/* ==========================================
   Generic DELETE API
========================================== */

async function deleteData(url) {

    if (!confirm("Are you sure?")) {

        return;

    }

    showLoader();

    try {

        const response = await fetch(url, {

            method: "DELETE"

        });

        hideLoader();

        return await response.json();

    }

    catch (error) {

        hideLoader();

        showToast("Delete Failed", "danger");

    }

}

/* ==========================================
   Table Search
========================================== */

function initializeSearch() {

    const search = document.getElementById("search");

    if (!search) return;

    search.addEventListener("keyup", function () {

        let filter = search.value.toLowerCase();

        let table = document.querySelector("table tbody");

        let rows = table.getElementsByTagName("tr");

        for (let i = 0; i < rows.length; i++) {

            let text = rows[i].innerText.toLowerCase();

            rows[i].style.display =

                text.indexOf(filter) > -1

                    ? ""

                    : "none";

        }

    });

}

/* ==========================================
   Form Validation
========================================== */

function initializeForms() {

    const forms = document.querySelectorAll("form");

    forms.forEach(form => {

        form.addEventListener("submit", function (e) {

            const required = form.querySelectorAll("[required]");

            let valid = true;

            required.forEach(input => {

                if (input.value.trim() === "") {

                    input.classList.add("is-invalid");

                    valid = false;

                }

                else {

                    input.classList.remove("is-invalid");

                }

            });

            if (!valid) {

                e.preventDefault();

                showToast("Please complete required fields", "warning");

            }

        });

    });

}

/* ==========================================
   Number Animation
========================================== */

function animateValue(id, endValue) {

    let obj = document.getElementById(id);

    if (!obj) return;

    let start = 0;

    let duration = 800;

    let step = Math.ceil(endValue / (duration / 20));

    let interval = setInterval(() => {

        start += step;

        if (start >= endValue) {

            start = endValue;

            clearInterval(interval);

        }

        obj.innerHTML = start;

    }, 20);

}

/* ==========================================
   Dashboard Counters
========================================== */

async function loadDashboard() {

    const data = await getData("/dashboard");

    if (!data) return;

    animateValue("pets", data.pets);

    animateValue("owners", data.owners);

    animateValue("doctors", data.doctors);

    animateValue("appointments", data.appointments);

}

/* ==========================================
   Logout
========================================== */

function logout() {

    if (confirm("Logout?")) {

        window.location.href = "/login";

    }

}

/* ==========================================
   Refresh Page
========================================== */

function refreshPage() {

    location.reload();

}

/* ==========================================
   Format Date
========================================== */

function formatDate(date) {

    return new Date(date).toLocaleString();

}

/* ==========================================
   Current Year Footer
========================================== */

const year = document.getElementById("year");

if (year) {

    year.innerHTML = new Date().getFullYear();

}