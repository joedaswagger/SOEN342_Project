from models.ticket import Ticket

class Trip:
    def __init__(self, trip_id, trip_type, travelling_class, client_id, travel_date, total_cost=0):
        self.trip_id = trip_id
        self.tickets = []
        self.trip_type = trip_type
        self.travelling_class = travelling_class
        self.total_cost = total_cost
        self.client_id = client_id
        self.travel_date = travel_date

    def add_ticket(self, ticket: Ticket):
        self.tickets.append(ticket)

    def set_trip_type(self, type):
        self.trip_type = type

    def set_total_cost(self, counter):
        self.total_cost = (float(self.total_cost) / (counter - 1)) * counter

    def print_self(self):
        print(f"\nTRIP {self.trip_id} | TRAVELLING '{self.travelling_class}' | TRAVELLING ON {self.travel_date} | TOTAL COST OF ${self.total_cost}")
