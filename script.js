const studentForm = document.getElementById("studentForm");

studentForm.addEventListener("submit", function (event) {
    event.preventDefault();

    alert("Registration successful!");

    studentForm.reset();
});
