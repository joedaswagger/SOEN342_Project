from datetime import datetime 
import uuid
import json
from json import JSONEncoder

class Ticket: 
    def __init__(self, route, cost, assigned_name):
        self.ticket_id = self.generate_ticket_id()
        self.date_issued = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.route = jsonEncoder().encode(route) # serialize with JSON
        self.cost = cost
        self.assigned_name = assigned_name

    def generate_ticket_id(self):
        return str(uuid.uuid4())[:8].upper()

class jsonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__