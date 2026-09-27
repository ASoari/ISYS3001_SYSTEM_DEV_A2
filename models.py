import sqlite3

def get_db_connection():
    conn = sqlite3.connect('dunbar_vet.db')
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Clients Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            client_type TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    
    # 2. Properties Table (US1)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            property_name TEXT NOT NULL,
            locality_pic TEXT NOT NULL,
            gate_access_notes TEXT,
            FOREIGN KEY (client_id) REFERENCES clients (id)
        )
    ''')

    # 3. Farm Visits Table (US2)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS farm_visits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            property_id INTEGER NOT NULL,
            visit_date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            duration_hours REAL NOT NULL,
            notes TEXT,
            FOREIGN KEY (property_id) REFERENCES properties (id)
        )
    ''')
    
    cursor.execute("SELECT * FROM clients")
    if len(cursor.fetchall()) == 0:
        cursor.execute(
            "INSERT INTO clients (name, client_type, phone) VALUES (?, ?, ?)",
            ('John Dunbar', 'Rural Business', '0412345678')
        )
        conn.commit()
        
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialization complete for US2.")