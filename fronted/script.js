// =========================================
// STUDENT MANAGEMENT SYSTEM
// =========================================


// Get the form
const studentForm = document.getElementById("studentForm");


// =========================================
// ADD STUDENT
// =========================================

studentForm.addEventListener("submit", function(event) {

    // Stop page from refreshing
    event.preventDefault();


    // =========================================
    // GET GENDER
    // =========================================

    const selectedGender =
        document.querySelector('input[name="gender"]:checked');

    let gender = "";

    if (selectedGender) {
        gender = selectedGender.value;
    }


    // =========================================
    // CREATE STUDENT OBJECT
    // =========================================

    const student = {

        id: document.getElementById("studentId").value,

        name: document.getElementById("fullName").value,

        age: document.getElementById("age").value,

        gender: gender,

        email: document.getElementById("email").value,

        phone: document.getElementById("phone").value,

        course: document.getElementById("course").value,

        semester: document.getElementById("semester").value,

        state: document.getElementById("state").value

    };


    // =========================================
    // SEND DATA TO FLASK BACKEND
    // =========================================

    fetch("http://127.0.0.1:5000/students", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(student)

    })


    // =========================================
    // BACKEND RESPONSE
    // =========================================

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        // Clear form
        studentForm.reset();

    })


    // =========================================
    // ERROR
    // =========================================

    .catch(error => {

        console.error("Error:", error);

        alert("Student could not be added.");

    });

});