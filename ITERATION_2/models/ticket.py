from datetime import datetime 
import uuid
import json
from json import JSONEncoder

class Ticket: 
    def __init__(self, ticket_id, route, cost, date_issued, assigned_name):
        self.ticket_id = self.generate_ticket_id() if ticket_id == None else ticket_id
        self.date_issued = datetime.now().strftime("%Y-%m-%d %H:%M:%S") if date_issued == None else date_issued
        self.route = jsonEncoder().encode(route) # serialize with JSON
        self.cost = cost
        self.assigned_name = assigned_name

    def generate_ticket_id(self):
        return str(uuid.uuid4())[:8].upper()
    
    def print_self(self):
        print(f"\n     TICKET {self.ticket_id} FOR {self.assigned_name} | TRAVEL ON {self.date_issued} | COST OF {self.cost}")

class jsonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__