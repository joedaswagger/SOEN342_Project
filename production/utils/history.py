from database.database import Database
from models.client import Client
from models.trip import Trip
from models.ticket import Ticket
import json

class History:
    def __init__(self, client: Client):
        self.client = client
        self.db = Database()

    def display_trips(self):
        trips = self.db.get_trips_from_client(int(self.client.client_id))
        for trip_record in trips:
            trip = Trip(trip_record[0], trip_record[1], trip_record[2], trip_record[5], trip_record[3], trip_record[4])
            trip.print_self()
            connection = None
            
            tickets = self.db.get_tickets_from_trip(trip.trip_id)
            for ticket_record in tickets:
                ticket = Ticket(ticket_record[0], ticket_record[2], ticket_record[1], ticket_record[3], ticket_record[5])
                ticket.print_self()
                connection = json.loads(ticket.route)
                connection = json.loads(connection)
            self.print_connection(connection)

    def print_connection(self, connection):
        print("\n     CONNECTION:")\
        
        if "initial" in connection:
            print(f"\n     {connection["initial"]["train_type"]} from {connection["initial"]["departure_city"]}, {connection["initial"]["departure_time"]} to {connection["initial"]["arrival_city"]}, {connection["initial"]["arrival_time"]} | Available {connection["initial"]["days_of_operation"]} | First class: ${connection["initial"]["first_class_rate"]}, Second class: ${connection["initial"]["second_class_rate"]} | Duration: {connection["initial"]["trip_duration_days"]} days, {connection["initial"]["trip_duration_hours"]} hours and {connection["initial"]["trip_duration_minutes"]} minutes")

            
            if "middle" in connection:
                print("\n     CORRESPONDING WITH")
                print(f"\n     {connection["middle"]["train_type"]} from {connection["middle"]["departure_city"]}, {connection["middle"]["departure_time"]} to {connection["middle"]["arrival_city"]}, {connection["middle"]["arrival_time"]} | Available {connection["middle"]["days_of_operation"]} | First class: ${connection["middle"]["first_class_rate"]}, Second class: ${connection["middle"]["second_class_rate"]} | Duration: {connection["middle"]["trip_duration_days"]} days, {connection["middle"]["trip_duration_hours"]} hours and {connection["middle"]["trip_duration_minutes"]} minutes")
            
            print("\n     CORRESPONDING WITH")
            print(f"\n     {connection["final"]["train_type"]} from {connection["final"]["departure_city"]}, {connection["final"]["departure_time"]} to {connection["final"]["arrival_city"]}, {connection["final"]["arrival_time"]} | Available {connection["final"]["days_of_operation"]} | First class: ${connection["final"]["first_class_rate"]}, Second class: ${connection["final"]["second_class_rate"]} | Duration: {connection["final"]["trip_duration_days"]} days, {connection["final"]["trip_duration_hours"]} hours and {connection["final"]["trip_duration_minutes"]} minutes")
        else:
            pass
            print(f"\n     {connection["train_type"]} from {connection["departure_city"]}, {connection["departure_time"]} to {connection["arrival_city"]}, {connection["arrival_time"]} | Available {connection["days_of_operation"]} | First class: ${connection["first_class_rate"]}, Second class: ${connection["second_class_rate"]} | Duration: {connection["trip_duration_days"]} days, {connection["trip_duration_hours"]} hours and {connection["trip_duration_minutes"]} minutes")