from models.ticket import Ticket

class Trip:
    def __init__(self, trip_id, trip_type, travelling_class, total_cost, client_id):
        self.trip_id = trip_id
        self.tickets = []
        self.trip_type = trip_type
        self.travelling_class = travelling_class
        self.total_cost = total_cost
        self.client_id = client_id

    def add_ticket(self, ticket: Ticket):
        self.tickets.append(ticket)

    def set_trip_type(self, type):
        self.trip_type = type

    def set_total_cost(self, counter):
        self.total_cost *= counter