# Offline Operation Testing

## Jira Story
MSD426IBSU2-13 — Offline/Local Operation

## Purpose
This test verifies that the Dunbar Veterinary Clinic Appointment System can operate locally without requiring an active internet connection.

## Test Environment
The application was opened directly from the local project files using index.html.

## Tests Performed

1. Disconnected the computer from the internet.
2. Opened index.html locally in the web browser.
3. Confirmed that the application interface loaded correctly.
4. Confirmed that CSS styling remained available.
5. Selected clients using the client dropdown.
6. Used the View Appointments function.
7. Confirmed that appointment information displayed correctly.
8. Confirmed that clients with no appointments were handled correctly.

## Result

PASS — The current prototype operated successfully without an active internet connection.

The HTML, CSS and JavaScript files required for the current prototype are stored locally, allowing the appointment interface and client appointment functionality to operate offline.