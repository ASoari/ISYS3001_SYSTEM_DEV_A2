# Dunbar Veterinary Clinic Appointment System

## 1. Project Overview

The Dunbar Veterinary Clinic Appointment System is a software development project designed to support the management of veterinary appointments. The system aims to provide a simple digital alternative for managing clinic appointment information.

The current prototype allows clinic staff to select a client and view appointments associated with that client. The project is being developed using an Agile/Scrum approach, with tasks managed through Jira and source code managed through Git and GitHub.

## 2. Current Features

The current prototype includes:

- Selection of a client from a client list.
- Display of appointments associated with the selected client.
- Support for consultation appointment records.
- Support for farm visit appointment records.
- Display of relevant appointment details and status.
- Handling of clients with no appointments.
- Validation when no client is selected.
- Local operation without requiring an active internet connection.

Additional functionality will be developed as the project progresses through future sprints.

## 3. Technologies Used

The current prototype uses:

- **HTML** — provides the structure of the web interface.
- **CSS** — provides the visual styling and layout.
- **JavaScript** — provides client appointment filtering and interactive functionality.
- **Git** — provides local version control.
- **GitHub** — provides source code management and team collaboration.
- **Jira** — supports sprint planning, task assignment and progress monitoring.

## 4. Project Structure

```text
Dunbar-Veterinary-Clinic---Appointment-System-
│
├── index.html
├── style.css
├── script.js
└── README.md
```

### File Descriptions

**index.html**  
Contains the structure of the Dunbar Veterinary Clinic appointment interface, including the client selector and appointment table.

**style.css**  
Contains the visual styling for the application, including the page layout, appointment table, buttons and responsive design.

**script.js**  
Contains the JavaScript functionality used to filter and display appointments according to the selected client.

**README.md**  
Contains the project overview, structure, setup instructions and information required to run the current prototype.

## 5. Setup Instructions

### Option 1 — Clone Using Git

Ensure Git is installed on the computer.

Open Git Bash, PowerShell or another Git-compatible terminal and navigate to the folder where the project should be stored.

Clone the GitHub repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd Dunbar-Veterinary-Clinic---Appointment-System-
```

The project can then be opened in Visual Studio Code:

```bash
code .
```

### Option 2 — Download from GitHub

The project can also be downloaded directly from GitHub.

1. Open the project repository on GitHub.
2. Select **Code**.
3. Select **Download ZIP**.
4. Extract the downloaded ZIP file.
5. Open the extracted project folder.

## 6. Running the Application

The current prototype does not require a web server.

To run the application:

1. Open the project folder.
2. Locate `index.html`.
3. Double-click `index.html`.
4. The application will open in the default web browser.
5. Select a client from the dropdown menu.
6. Select **View Appointments**.
7. The appointments associated with the selected client will be displayed.

## 7. Offline Operation

The current front-end prototype uses locally stored HTML, CSS and JavaScript files and does not rely on external online resources for its current functionality.

Offline testing was performed by disconnecting the computer from the internet and opening the application locally.

During testing:

- The application interface loaded successfully.
- CSS styling remained available.
- Client selection continued to function.
- JavaScript appointment filtering continued to function.
- Appointment information continued to display.

This confirms that the **current front-end prototype** can operate locally without an active internet connection.

## 8. Development Workflow

The project uses Git branches to separate development work.

A typical development workflow is:

```text
Jira Task
   ↓
Create Git Branch
   ↓
Develop Feature
   ↓
Test Feature
   ↓
Commit Changes
   ↓
Push to GitHub
   ↓
Pull Request / Team Review
   ↓
Integration
```

Developers should avoid making feature changes directly to the `main` branch.

Example branch names used during development include:

```text
MSD426IBSU2-12-client-appointments
MSD426IBSU2-13-offline-local
MSD426IBSU2-22-readme
```

## 9. Git Commands

Check the current branch and project status:

```bash
git status
```

View available branches:

```bash
git branch
```

Stage changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Describe the change"
```

Push the current branch to GitHub:

```bash
git push
```

## 10. Agile and Team Collaboration

The project is being developed using an Agile/Scrum approach.

The team uses:

- **Jira** for backlog management, user stories, task allocation and sprint monitoring.
- **GitHub** as the source code repository and for version control.
- **Git branches** to separate individual development tasks.
- **Mini Sprints** to develop and test project functionality incrementally.
- **Scrum communication** to discuss progress, completed work, upcoming work and blockers.

Development follows an iterative process of:

**Analysis → Design → Development → Testing**

## 11. Current Development Status

The current prototype demonstrates initial appointment management functionality developed during Mini Sprint 1.

Completed or tested functionality includes client appointment listing and local/offline operation. Further features will be integrated as development progresses through the team's remaining sprint activities.

---

**Project:** Dunbar Veterinary Clinic Appointment System  
**Unit:** ISYS3001 Managing Software Development
