from flask import Flask, render_template, request, redirect, url_for
from models import get_db_connection, init_db

app = Flask(__name__)
app.secret_key = 'dunbar-secret-key-123'

init_db()

@app.route("/")
def home():
    return redirect(url_for("manage_properties"))

# US1 Route: Manage Properties
@app.route("/properties", methods=["GET", "POST"])
def manage_properties():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == "POST":
        client_id = request.form.get("client_id")
        property_name = request.form.get("property_name")
        locality_pic = request.form.get("locality_pic")
        gate_access_notes = request.form.get("gate_access_notes")
        
        if property_name != "" and locality_pic != "":
            cursor.execute(
                "INSERT INTO properties (client_id, property_name, locality_pic, gate_access_notes) VALUES (?, ?, ?, ?)",
                (client_id, property_name, locality_pic, gate_access_notes)
            )
            conn.commit()
            conn.close()
            return redirect(url_for("manage_properties"))
    
    cursor.execute('''
        SELECT properties.id, properties.property_name, properties.locality_pic, properties.gate_access_notes, clients.name
        FROM properties
        JOIN clients ON properties.client_id = clients.id
    ''')
    properties = cursor.fetchall()
    
    cursor.execute("SELECT id, name, client_type FROM clients")
    clients = cursor.fetchall()
    
    conn.close()
    return render_template("properties.html", properties=properties, clients=clients)

# US2 Route: Book Farm Visit
@app.route("/farm-visit/book", methods=["GET", "POST"])
def book_farm_visit():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == "POST":
        property_id = request.form.get("property_id")
        visit_date = request.form.get("visit_date")
        start_time = request.form.get("start_time")
        duration_hours = request.form.get("duration_hours")
        notes = request.form.get("notes")
        
        if property_id and visit_date and start_time and duration_hours:
            cursor.execute(
                "INSERT INTO farm_visits (property_id, visit_date, start_time, duration_hours, notes) VALUES (?, ?, ?, ?, ?)",
                (property_id, visit_date, start_time, duration_hours, notes)
            )
            conn.commit()
            conn.close()
            return redirect(url_for("book_farm_visit"))
            
    cursor.execute('''
        SELECT farm_visits.id, properties.property_name, farm_visits.visit_date, farm_visits.start_time, farm_visits.duration_hours, farm_visits.notes
        FROM farm_visits
        JOIN properties ON farm_visits.property_id = properties.id
    ''')
    visits = cursor.fetchall()

    cursor.execute("SELECT id, property_name, locality_pic FROM properties")
    properties = cursor.fetchall()
    
    conn.close()
    return render_template("farm_visit.html", properties=properties, visits=visits)

if __name__ == "__main__":
    app.run(debug=True)