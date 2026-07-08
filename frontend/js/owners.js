// =====================================
// Pet Clinic - Owners
// owners.js
// =====================================

checkLogin();

const OWNER_API = API_URL + "/owners";


// Load Owners
function loadOwners() {

    fetch(OWNER_API)

    .then(response => response.json())

    .then(data => {

        const table = document.getElementById("ownersTable");

        table.innerHTML = "";

        data.forEach(owner => {

            table.innerHTML += `
                <tr>
                    <td>${owner.id}</td>
                    <td>${owner.name}</td>
                    <td>${owner.phone}</td>
                    <td>${owner.email}</td>
                    <td>${owner.address}</td>
                </tr>
            `;

        });

    })

    .catch(error => {

        console.error("Error Loading Owners:", error);

    });

}


// Add Owner

document.getElementById("ownerForm").addEventListener("submit", function(e){

    e.preventDefault();

    const owner = {

        name: document.getElementById("name").value,

        phone: document.getElementById("phone").value,

        email: document.getElementById("email").value,

        address: document.getElementById("address").value

    };


    fetch(OWNER_API, {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(owner)

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        document.getElementById("ownerForm").reset();

        loadOwners();

    })

    .catch(error => {

        console.error(error);

    });

});


// Load Owners Automatically

window.onload = function () {

    loadOwners();

};