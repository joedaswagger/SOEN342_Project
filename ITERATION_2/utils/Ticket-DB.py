import sqlite3
import pickle
from Ticket import Ticket

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
        INSERT INTO tickets (ticket_id, traveller_name, traveller_age, traveller_id,connection_id, ticket_type, issue_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.conn.execute(query, ticket.to_tuple())
        self.conn.commit()

    def show_all(self):
        #Display all tickets.
        cursor = self.conn.execute("SELECT * FROM tickets")
        return cursor.fetchall()
    
if __name__ == "__main__":
    db = Ticket_Database()

    # Create test tickets
    t1 = Ticket("Rohit", 22, "A000", "C456", "single")
    t2 = Ticket("Matthew", 35, "B001", "C123", "multiple")

    # Add to db
    db.insert_ticket(t1)
    db.insert_ticket(t2)

    print("Tickets inserted!\nCurrent database data\n")
    print(db.show_all())