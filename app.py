from flask import Flask, render_template, request, redirect, url_for
from models import get_db_connection, init_db

app = Flask(__name__)

#Initialise the database when the application starts
init_db()


@app.route("/")
def home():
    return redirect(url_for("book_consultation"))

# Feature 1: Book an In-Clinic Consultation
@app.route("/consultation/book", methods=["GET", "POST"])
def book_consultation():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        animal_id = request.form.get("animal_id")
        consultation_date = request.form.get("consultation_date")
        start_time = request.form.get("start_time")
        notes = request.form.get("notes")

        # In-clinic consultations are fixed at 15 minutes
        duration_minutes = 15
        status = "Scheduled"

        if animal_id and consultation_date and start_time:
            cursor.execute("""
                INSERT INTO consultations (
                    animal_id,
                    consultation_date,
                    start_time,
                    duration_minutes,
                    notes,
                    status
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                animal_id,
                consultation_date,
                start_time,
                duration_minutes,
                notes,
                status
            ))

            conn.commit()
            conn.close()

            return redirect(url_for("book_consultation"))

    # TEMPORARY test animals.
    # This will be replaced by the team's Animal table later.
    animals = [
        (1, "Max"),
        (2, "Bella"),
        (3, "Charlie")
    ]

    cursor.execute("""
        SELECT
            id,
            animal_id,
            consultation_date,
            start_time,
            duration_minutes,
            notes,
            status
        FROM consultations
        ORDER BY consultation_date, start_time
    """)

    consultations = cursor.fetchall()

    conn.close()

    return render_template(
        "consultation.html",
        animals=animals,
        consultations=consultations
    )


# Feature 2: View Daily Schedule
@app.route("/schedule")
def daily_schedule():
    selected_date = request.args.get("date")

    conn = get_db_connection()
    cursor = conn.cursor()

    consultations = []
    farm_visits = []

    if selected_date:
        # Get in-clinic consultations for the selected date
        cursor.execute("""
            SELECT
                id,
                animal_id,
                consultation_date,
                start_time,
                duration_minutes,
                notes,
                status
            FROM consultations
            WHERE consultation_date = ?
        """, (selected_date,))

        for row in cursor.fetchall():
            consultations.append({
                "id": row[0],
                "type": "In-clinic Consultation",
                "details": f"Animal ID: {row[1]}",
                "date": row[2],
                "start_time": row[3],
                "duration": f"{row[4]} minutes",
                "notes": row[5],
                "status": row[6]
            })

        # Get farm visits if the teammate's table exists
        cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table' AND name='farm_visits'
        """)

        farm_visit_table = cursor.fetchone()

        if farm_visit_table:
            cursor.execute("""
                SELECT
                    farm_visits.id,
                    farm_visits.visit_date,
                    farm_visits.start_time,
                    farm_visits.duration_hours,
                    farm_visits.notes,
                    properties.property_name
                FROM farm_visits
                JOIN properties
                    ON farm_visits.property_id = properties.id
                WHERE farm_visits.visit_date = ?
            """, (selected_date,))

            for row in cursor.fetchall():
                farm_visits.append({
                    "id": row[0],
                    "type": "Farm Visit",
                    "details": row[5],
                    "date": row[1],
                    "start_time": row[2],
                    "duration": f"{row[3]} hours",
                    "notes": row[4],
                    "status": "Scheduled"
                })

    conn.close()

    # Combine both appointment types
    schedule = consultations + farm_visits

    # Sort all appointments by start time
    schedule.sort(key=lambda appointment: appointment["start_time"])

    return render_template(
        "daily_schedule.html",
        schedule=schedule,
        selected_date=selected_date
    )


# Feature 3: Change an Appointment
@app.route("/consultation/<int:consultation_id>/edit", methods=["GET", "POST"])
def edit_consultation(consultation_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Find the consultation being edited
    cursor.execute("""
        SELECT
            id,
            animal_id,
            consultation_date,
            start_time,
            duration_minutes,
            notes,
            status
        FROM consultations
        WHERE id = ?
    """, (consultation_id,))

    consultation = cursor.fetchone()

    if consultation is None:
        conn.close()
        return "Consultation not found", 404

    if request.method == "POST":
        consultation_date = request.form.get("consultation_date")
        start_time = request.form.get("start_time")
        notes = request.form.get("notes")

        if consultation_date and start_time:
            cursor.execute("""
                UPDATE consultations
                SET consultation_date = ?,
                    start_time = ?,
                    notes = ?
                WHERE id = ?
            """, (
                consultation_date,
                start_time,
                notes,
                consultation_id
            ))

            conn.commit()
            conn.close()

            return redirect(
                url_for(
                    "daily_schedule",
                    date=consultation_date
                )
            )

    conn.close()

    return render_template(
        "edit_consultation.html",
        consultation=consultation
    )


# Feature 3: Cancel an Appointment
@app.route("/consultation/<int:consultation_id>/cancel", methods=["POST"])
def cancel_consultation(consultation_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get the consultation date before cancelling
    cursor.execute("""
        SELECT consultation_date
        FROM consultations
        WHERE id = ?
    """, (consultation_id,))

    consultation = cursor.fetchone()

    if consultation is None:
        conn.close()
        return "Consultation not found", 404

    consultation_date = consultation[0]

    # Keep the appointment but change its status
    cursor.execute("""
        UPDATE consultations
        SET status = 'Cancelled'
        WHERE id = ?
    """, (consultation_id,))

    conn.commit()
    conn.close()

    return redirect(
        url_for(
            "daily_schedule",
            date=consultation_date
        )
    )

if __name__ == "__main__":
    app.run(debug=True)
