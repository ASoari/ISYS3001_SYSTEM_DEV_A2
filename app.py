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


if __name__ == "__main__":
    app.run(debug=True)

       