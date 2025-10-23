from datetime import datetime 
import uuid

class Ticket: 
    def __init__(self, route):
        #Unique ID for each ticket generated automatically
        self.__ticket_id = self.generate_ticket_id()
        # Date/time the ticket is issued
        self.date_issued = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.route = route
        self.cost = None

    def generate_ticket_id(self):
        return str(uuid.uuid4())[:8].upper()
    
    #Convert to tuple for database
    # def to_tuple(self):
    #     """Return data as a tuple for database insertion."""
    #     return (
    #     self.ticket_id,
    #     self.traveller_name,
    #     self.traveller_age,
    #     self.traveller_id,
    #     self.connection_id,
    #     self.ticket_type,
    #     self.date_issued
    #     )

