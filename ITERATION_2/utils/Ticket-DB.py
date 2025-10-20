import sqlite3
import Ticket

class Ticket_Database:

    def __init__(self, db="ticket.db"):
        self.conn = sqlite3.connect(db)
        self.create_table()
    
    #Creates table at init
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tickets (ticket_id TEXT PRIMARY KEY, traveller_name TEXT, traveller_age INTEGER, traveller_id TEXT, connection_id TEXT, ticket_type TEXT, issue_date TEXT)
        """

        self.conn.execute(query)
        self.conn.commit()


if __name__ == "__main__":
    db = Ticket_Database()

    # Create test tickets
    t1 = Ticket("Rohit", 22, "A000", "C456", "single")
    t2 = Ticket("Matthew", 35, "B001", "C123", "multiple")

    # Add to db
    db.insert_ticket(t1)
    db.insert_ticket(t2)

    print("Tickets inserted!\nCurrent database data\n")
    db.show_all()