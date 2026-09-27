# client.py

# A simple in-memory list to store clients
clients = []

def add_client(name, phone):
    """
    Add a new client with name and phone number.
    Each client starts with an empty list of animals.
    """
    client = {
        "name": name,
        "phone": phone,
        "animals": []
    }
    clients.append(client)
    return client

def update_client(name, new_phone):
    """
    Update a client's phone number by searching their name.
    """
    for client in clients:
        if client["name"].lower() == name.lower():
            client["phone"] = new_phone
            return client
    return None

def search_client(name):
    """
    Search for clients by name (case-insensitive).
    Returns a list of matching clients.
    """
    return [c for c in clients if name.lower() in c["name"].lower()]

def list_clients():
    """
    Return all clients in the system.
    """
    return clients


# main.py
from client import add_client, update_client, search_client, list_clients

# Add some clients
add_client("John Doe", "123456789")
add_client("Jane Smith", "987654321")

# Update a client
update_client("John Doe", "111222333")

# Search for a client
print(search_client("Jane"))

# List all clients
print(list_clients())
