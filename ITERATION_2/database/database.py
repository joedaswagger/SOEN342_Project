import sqlite3
import pickle
from models.ticket import Ticket
from models.trip import Trip
from models.client import Client

class Database:
    def __init__(self):
        self.database = "trip_planner.db"
        self.connection = self.connect()

        self.create_tables()
    
    def connect(self):
        return sqlite3.connect(self.database)

    def close_connection(self):
        self.connection.close()

    def create_tables(self):
        trip_table_query = """
            CREATE TABLE IF NOT EXISTS trips (
                trip_id TEXT PRIMARY KEY,
                trip_type TEXT,
                travelling_class TEXT,
                total_cost REAL,
                client_id INT,
                FOREIGN KEY (client_id) REFERENCES clients (client_id)
            )
        """

        ticket_table_query = """
            CREATE TABLE IF NOT EXISTS tickets (
                ticket_id INT PRIMARY KEY,
                cost REAL,
                route TEXT,
                date_issued TEXT,
                trip_id TEXT,
                assigned_name TEXT,
                FOREIGN KEY (trip_id) REFERENCES trips (trip_id)
            )
        """

        client_table_query = """
            CREATE TABLE IF NOT EXISTS clients (
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                id TEXT
            )
        """

        cursor = self.connection.cursor()
        cursor.execute(client_table_query)
        cursor.execute(trip_table_query)
        cursor.execute(ticket_table_query)
        self.connection.commit()

    def insert_ticket(self, ticket: Ticket, trip: Trip):
        query = """
            INSERT INTO tickets (ticket_id, cost, route, date_issued, trip_id, assigned_name)
            VALUES (?, ?, ?, ?, ?, ?)
        """

        cursor = self.connection.cursor()
        cursor.execute(query, (ticket.ticket_id, ticket.cost, ticket.route, ticket.date_issued, trip.trip_id, ticket.assigned_name))
        self.connection.commit()

    def insert_trip(self, trip: Trip):
        query = """
            INSERT INTO trips (trip_id, trip_type, travelling_class, total_cost, client_id)
            VALUES (?, ?, ?, ?, ?)
        """

        cursor = self.connection.cursor()
        cursor.execute(query, (trip.trip_id, trip.trip_type, trip.travelling_class, trip.total_cost, trip.client_id))
        self.connection.commit()

    def insert_client(self, first_name, last_name, age, id):
        query = """
            INSERT INTO clients (first_name, last_name, age, id)
            VALUES (?, ?, ?, ?)
            RETURNING *
        """

        cursor = self.connection.cursor()
        cursor.execute(query, (first_name, last_name, age, id))
        inserted_client = cursor.fetchone()
        self.connection.commit()

        return Client(inserted_client[0], inserted_client[1], inserted_client[2], inserted_client[3], inserted_client[4])

    def get_tickets_from_trip(self, trip_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM tickets WHERE trip_id = ?;", (trip_id,))
        tickets = cursor.fetchall()
        return tickets

    def get_trips_from_client(self, client_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM trips WHERE client_id = ?;", (client_id,))
        trips = cursor.fetchall()
        return trips

    def get_client(self, last_name, id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM clients WHERE last_name = ? AND id = ?;", (last_name, id))
        client = cursor.fetchone()
        
        if client:
            return Client(client[0], client[1], client[2], client[3], client[4])
        else:
            return None