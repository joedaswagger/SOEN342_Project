from datetime import date, datetime
from database.database import Database
from models.client import Client
from models.trip import Trip
from models.ticket import Ticket
import json

class History:
    def __init__(self, client: Client):
        self.client = client
        self.db = Database()

    def display_trips(self, past):
        trips = self.db.get_trips_from_client(int(self.client.client_id))
        counter = 0
        for trip_record in trips:
            trip = Trip(trip_record[0], trip_record[1], trip_record[2], trip_record[5], trip_record[3], trip_record[4])

            today = date.today()
            travel_date = datetime.strptime(trip.travel_date, "%B %d, %Y").date()

            if (past == True and travel_date < today) or (past == False and travel_date >= today):
                counter += 1
                trip.print_self()
                connection = None
                
                tickets = self.db.get_tickets_from_trip(trip.trip_id)
                for ticket_record in tickets:
                    ticket = Ticket(ticket_record[0], ticket_record[2], ticket_record[1], ticket_record[3], ticket_record[5])
                    ticket.print_self()
                    connection = json.loads(ticket.route)
                    connection = json.loads(connection)
                self.print_connection(connection)

        if counter == 0:
            print("\nNo trips found.")

    def print_connection(self, connection):
        print("\n     CONNECTION:")

        if "initial" in connection:
            print(
                f"\n     {connection['initial']['train_type']} from {connection['initial']['departure_city']}, {connection['initial']['departure_time']} "
                f"to {connection['initial']['arrival_city']}, {connection['initial']['arrival_time']} | Available {connection['initial']['days_of_operation']} "
                f"| First class: ${connection['initial']['first_class_rate']}, Second class: ${connection['initial']['second_class_rate']} "
                f"| Duration: {connection['initial']['trip_duration_days']} days, {connection['initial']['trip_duration_hours']} hours and "
                f"{connection['initial']['trip_duration_minutes']} minutes"
            )

            if "middle" in connection:
                print("\n     CORRESPONDING WITH")
                print(
                    f"\n     {connection['middle']['train_type']} from {connection['middle']['departure_city']}, {connection['middle']['departure_time']} "
                    f"to {connection['middle']['arrival_city']}, {connection['middle']['arrival_time']} | Available {connection['middle']['days_of_operation']} "
                    f"| First class: ${connection['middle']['first_class_rate']}, Second class: ${connection['middle']['second_class_rate']} "
                    f"| Duration: {connection['middle']['trip_duration_days']} days, {connection['middle']['trip_duration_hours']} hours and "
                    f"{connection['middle']['trip_duration_minutes']} minutes"
                )

            print("\n     CORRESPONDING WITH")
            print(
                f"\n     {connection['final']['train_type']} from {connection['final']['departure_city']}, {connection['final']['departure_time']} "
                f"to {connection['final']['arrival_city']}, {connection['final']['arrival_time']} | Available {connection['final']['days_of_operation']} "
                f"| First class: ${connection['final']['first_class_rate']}, Second class: ${connection['final']['second_class_rate']} "
                f"| Duration: {connection['final']['trip_duration_days']} days, {connection['final']['trip_duration_hours']} hours and "
                f"{connection['final']['trip_duration_minutes']} minutes"
            )

        else:
            print(
                f"\n     {connection['train_type']} from {connection['departure_city']}, {connection['departure_time']} "
                f"to {connection['arrival_city']}, {connection['arrival_time']} | Available {connection['days_of_operation']} "
                f"| First class: ${connection['first_class_rate']}, Second class: ${connection['second_class_rate']} "
                f"| Duration: {connection['trip_duration_days']} days, {connection['trip_duration_hours']} hours and "
                f"{connection['trip_duration_minutes']} minutes"
            )
