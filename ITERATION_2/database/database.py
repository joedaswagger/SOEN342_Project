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
        print("\nDatabase connection instantiated succesfully.\n")
        return sqlite3.connect(self.database)

    def close_connection(self):
        self.connection.close()

    def create_tables(self):
        trip_table_query = """
            CREATE TABLE IF NOT EXISTS trips (
                trip_id TEXT PRIMARY KEY,
                trip_type TEXT,
                travelling_class TEXT,
                total_cost REAL
            )
        """

        ticket_table_query = """
            CREATE TABLE IF NOT EXISTS tickets (
                ticket_id INT PRIMARY KEY,
                cost REAL,
                route TEXT,
                date_issued TEXT,
                trip_id TEXT,
                FOREIGN KEY (trip_id) REFERENCES trips (trip_id)
            )
        """

        client_table_query = """
            CREATE TABLE IF NOT EXISTS clients (
                client_id TEXT PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                id TEXT,
                trip_id TEXT,
                FOREIGN KEY (trip_id) REFERENCES trips (trip_id)
                UNIQUE(trip_id)
            )
        """

        cursor = self.connection.cursor()
        cursor.execute(trip_table_query)
        cursor.execute(ticket_table_query)
        cursor.execute(client_table_query)
        self.connection.commit()

    def insert_ticket(self, ticket: Ticket, trip: Trip):
        query = """
            INSERT INTO tickets (ticket_id, cost, route, date_issued, trip_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        cursor = self.connection.cursor()
        cursor.execute(query, (ticket.ticket_id, ticket.cost, ticket.route, ticket.date_issued, trip.trip_id))
        self.connection.commit()

    def insert_trip(self, trip: Trip):
        query = """
            INSERT INTO trips (trip_id, trip_type, travelling_class, total_cost)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        cursor = self.connection.cursor()
        cursor.execute(query, (trip.trip_id, trip.trip_type, trip.travelling_class, trip.total_cost))
        self.connection.commit()

    def insert_client(self, client: Client):
        query = """
            INSERT INTO clients (client_id, first_name, last_name, age, id, trip_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        cursor = self.connection.cursor()
        cursor.execute(query, (client.client_id, client.first_name, client.last_name, client.age, client.id, client.trip.trip_id))
        self.connection.commit()

    def get_tickets_from_trip(self, trip_id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM tickets WHERE trip_id = {trip_id};")
        tickets = cursor.fetchall()
        return tickets

    def get_trip(self, trip_id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM trips WHERE trip_id = {trip_id};")
        trip = cursor.fetchone()
        return trip

    def get_client(self, last_name, id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM clients WHERE last_name = {last_name} AND id = {id};")
        client = cursor.fetchone()
        return client

    

    # def show_all(self):
    #     #Display all tickets.
    #     cursor = self.conn.execute("SELECT * FROM tickets")
    #     return cursor.fetchall()