import sqlite3

def get_db_connection():
    conn = sqlite3.connect("dunbar_vet.db")
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # In-clinic Consultations Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            animal_id INTEGER,
            consultation_date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            duration_minutes INTEGER NOT NULL DEFAULT 15,
            notes TEXT,
            status TEXT NOT NULL DEFAULT 'Scheduled'
        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("Consultation database initialization complete.")