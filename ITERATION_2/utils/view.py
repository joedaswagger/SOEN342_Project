from database.database import Database
from models.route import Route

class View:
    db = Database()

    def _init_(self, name, id):
        self.name = name
        self.id = id

    def fetch(self, name, id):
        client = self.db.get_client(name, id)

        print(client.trip_id)

        ticket = self.db.get_tickets_from_trip(client.trip_id)

        route = ticket[2]

        Route.print_self(route, 1)


        pass