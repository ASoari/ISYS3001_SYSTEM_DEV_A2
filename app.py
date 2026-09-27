from flask import Flask, render_template, request, redirect, url_for
from models import get_db_connection, init_db

app = Flask(__name__)
app.secret_key = 'dunbar-secret-key-123'

# Ensure database tables are created on startup
init_db()

@app.route("/")
def home():
    return redirect(url_for("manage_properties"))

@app.route("/properties", methods=["GET", "POST"])
def manage_properties():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == "POST":
        # Get data from web form
        client_id = request.form.get("client_id")
        property_name = request.form.get("property_name")
        locality_pic = request.form.get("locality_pic")
        gate_access_notes = request.form.get("gate_access_notes")
        
        # Simple input check
        if property_name != "" and locality_pic != "":
            cursor.execute(
                "INSERT INTO properties (client_id, property_name, locality_pic, gate_access_notes) VALUES (?, ?, ?, ?)",
                (client_id, property_name, locality_pic, gate_access_notes)
            )
            conn.commit()
            conn.close()
            return redirect(url_for("manage_properties"))
    
    # Fetch properties joined with client names
    cursor.execute('''
        SELECT properties.id, properties.property_name, properties.locality_pic, properties.gate_access_notes, clients.name
        FROM properties
        JOIN clients ON properties.client_id = clients.id
    ''')
    properties = cursor.fetchall()
    
    # Fetch all clients for the dropdown list
    cursor.execute("SELECT id, name, client_type FROM clients")
    clients = cursor.fetchall()
    
    conn.close()
    return render_template("properties.html", properties=properties, clients=clients)

if __name__ == "__main__":
    app.run(debug=True)