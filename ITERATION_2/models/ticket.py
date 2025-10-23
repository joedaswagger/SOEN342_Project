from datetime import datetime 
import uuid


class Ticket: 
    def __init__(self, traveller_name, traveller_age, traveller_id, connection_id, ticket_type="single"): 
        if ticket_type not in ("single", "multiple"): #For validating ticket type one person or a group
            raise ValueError("ticket_type must be either 'single' or 'multiple'") 
        #Unique ID for each ticket generated automatically
        self.ticket_id = self.generate_ticket_id() 

        # Date/time the ticket is issued
        self.date_issued = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Traveller details
        self.traveller_name = traveller_name 
        self.traveller_age = traveller_age 
        self.traveller_id = traveller_id 
        self.connection_id = connection_id 
        self.ticket_type = ticket_type 
    #Function to generate ticket ID
    def generate_ticket_id(self):

        return str(uuid.uuid4())[:8].upper()
    #Convert to tuple for database
    def to_tuple(self):
        """Return data as a tuple for database insertion."""
        return (
        self.ticket_id,
        self.traveller_name,
        self.traveller_age,
        self.traveller_id,
        self.connection_id,
        self.ticket_type,
        self.date_issued
        )

