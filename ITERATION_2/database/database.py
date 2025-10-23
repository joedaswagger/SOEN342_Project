import sqlite3
import pickle
from models.ticket import Ticket

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
        ticket_tale_query = """
            CREATE TABLE IF NOT EXISTS tickets (
                ticket_id INT PRIMARY KEY,
                cost REAL,
                route TEXT,
                date_issued TEXT,
                FOREIGN KEY (trip_id) REFERENCES trips (trip_id)
            )
        """

        trip_tale_query = """
            CREATE TABLE IF NOT EXISTS trips (
                trip_id TEXT PRIMARY KEY,
                trip_type TEXT,
                travelling_class TEXT,
                total_cost REAL
            )
        """

        client_tale_query = """
            CREATE TABLE IF NOT EXISTS clients (
                client_id TEXT PRIMARY KEY,
                age INTEGER,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                id TEXT,
                FOREIGN KEY (trip_id) REFERENCES trips (trip_id)
                UNIQUE(trip_id)
            )
        """

        self.conn.execute(trip_tale_query)
        self.conn.execute(ticket_tale_query)
        self.conn.execute(client_tale_query)
        self.conn.commit()

    def insert_ticket(self, ticket: Ticket):
        #Insert a ticket into database.
        query = """
        INSERT INTO tickets (ticket_id, traveller_name, traveller_age, traveller_id,connection_id, ticket_type, date_issued)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.conn.execute(query, ticket.to_tuple())
        self.conn.commit()

    def show_all(self):
        #Display all tickets.
        cursor = self.conn.execute("SELECT * FROM tickets")
        return cursor.fetchall()
    
    def database(self, t1):
        db = Ticket_Database()

        # Add to db
        db.insert_ticket(t1)

        print("Tickets inserted!\nCurrent database data\n")
        print(db.show_all())