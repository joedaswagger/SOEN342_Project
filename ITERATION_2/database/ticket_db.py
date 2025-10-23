import sqlite3
import pickle
from models.ticket import Ticket

class Ticket_Database:

    def __init__(self, db="ticket.db"):
        self.conn = sqlite3.connect(db)
        self.create_table()
    
    #Creates table at init
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tickets (ticket_id TEXT PRIMARY KEY, traveller_name TEXT, traveller_age INTEGER, traveller_id TEXT, connection_id TEXT, ticket_type TEXT, date_issued TEXT)
        """

        self.conn.execute(query)
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