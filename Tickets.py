from datetime import datetime 


class Ticket: 
    def __init__(self, traveller_name, traveller_age, traveller_id, connection_id, ticket_type="single"): 
        if ticket_type not in ("single", "multiple"): #For validating ticket type one person or a group
            raise ValueError("ticket_type must be either 'single' or 'multiple'") 
        #Unique ID for each ticket generated automatically(TBD how)
        self.ticket_id = self._generate_ticket_id() 

        # Date/time the ticket is issued
        self.date_issued = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Traveller details
        self.traveller_name = traveller_name 
        self.traveller_age = traveller_age 
        self.traveller_id = traveller_id 
        self.connection_id = connection_id 
        self.ticket_type = ticket_type 
     