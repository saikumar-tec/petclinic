// ======================================
// Pet Clinic - Pets
// ======================================

checkLogin();

const PET_API = API_URL + "/pets";

// Load Pets
function loadPets() {

    fetch(PET_API)

    .then(response => response.json())

    .then(data => {

        const table = document.getElementById("petsTable");

        table.innerHTML = "";

        data.forEach(pet => {

            table.innerHTML += `
                <tr>
                    <td>${pet.id}</td>
                    <td>${pet.name}</td>
                    <td>${pet.breed}</td>
                    <td>${pet.age}</td>
                    <td>${pet.gender}</td>
                    <td>${pet.owner_id}</td>
                </tr>
            `;

        });

    })

    .catch(error => {

        console.error("Error loading pets:", error);

    });

}


// Add Pet

document.getElementById("petForm").addEventListener("submit", function(e){

    e.preventDefault();

    const pet = {

        name: document.getElementById("name").value,

        breed: document.getElementById("breed").value,

        age: parseInt(document.getElementById("age").value),

        gender: document.getElementById("gender").value,

        owner_id: parseInt(document.getElementById("owner_id").value)

    };

    fetch(PET_API,{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify(pet)

    })

    .then(response=>response.json())

    .then(data=>{

        alert(data.message);

        document.getElementById("petForm").reset();

        loadPets();

    })

    .catch(error=>{

        console.error(error);

    });

});


// Load pets when page opens

window.onload = function(){

    loadPets();

};