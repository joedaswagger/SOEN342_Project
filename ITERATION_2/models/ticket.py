from datetime import datetime 
import uuid

class Ticket: 
    def __init__(self, route):
        self.ticket_id = self.generate_ticket_id()
        self.date_issued = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.route = route # serialize with JSON
        self.cost = None

    def generate_ticket_id(self):
        return str(uuid.uuid4())[:8].upper()
