// Dunbar Veterinary Clinic
// Client Appointment Functionality
// Story: MSD426IBSU2-12


// Temporary appointment data used for Sprint 1 development.
// This can later be connected to the team's shared data structure.

const appointments = [
    {
        id: 1,
        clientId: "1",
        date: "28/09/2026",
        type: "Consultation",
        animal: "Moss",
        species: "Dog",
        status: "Booked"
    },

    {
        id: 2,
        clientId: "1",
        date: "29/09/2026",
        type: "Farm Visit",
        property: "Stony Creek",
        status: "Booked"
    },

    {
        id: 3,
        clientId: "1",
        date: "02/10/2026",
        type: "Consultation",
        animal: "Sooty",
        species: "Cat",
        status: "Cancelled"
    },

    {
        id: 4,
        clientId: "2",
        date: "30/09/2026",
        type: "Consultation",
        animal: "Bella",
        species: "Dog",
        status: "Booked"
    }
];


// Get the HTML elements that the JavaScript needs.

const clientSelect =
    document.getElementById("clientSelect");

const viewAppointmentsBtn =
    document.getElementById("viewAppointmentsBtn");

const appointmentTableBody =
    document.getElementById("appointmentTableBody");

const noAppointmentsMessage =
    document.getElementById("noAppointmentsMessage");


// Run the function when the user clicks
// the View Appointments button.

viewAppointmentsBtn.addEventListener(
    "click",
    displayClientAppointments
);


// Main function for displaying appointments.

function displayClientAppointments() {

    // Get the selected client ID.

    const selectedClientId = clientSelect.value;


    // Clear previous results.

    appointmentTableBody.innerHTML = "";
    noAppointmentsMessage.textContent = "";


    // Make sure a client has been selected.

    if (selectedClientId === "") {

        noAppointmentsMessage.textContent =
            "Please select a client.";

        return;
    }


    // Find appointments belonging to the selected client.

    const clientAppointments = appointments.filter(
        appointment =>
            appointment.clientId === selectedClientId
    );


    // Handle clients with no appointments.

    if (clientAppointments.length === 0) {

        noAppointmentsMessage.textContent =
            "No appointments found for this client.";

        return;
    }


    // Display every appointment belonging
    // to the selected client.

    clientAppointments.forEach(appointment => {

        const row = document.createElement("tr");


        // Work out what information should appear
        // in the Details column.

        let appointmentDetails = "";


        if (appointment.type === "Consultation") {

            appointmentDetails =
                `${appointment.animal} (${appointment.species})`;

        }

        else if (appointment.type === "Farm Visit") {

            appointmentDetails =
                appointment.property;

        }


        // Add appointment information to the row.

        row.innerHTML = `
            <td>${appointment.date}</td>
            <td>${appointment.type}</td>
            <td>${appointmentDetails}</td>
            <td>${appointment.status}</td>
        `;


        // Add the completed row to the table.

        appointmentTableBody.appendChild(row);

    });

}
