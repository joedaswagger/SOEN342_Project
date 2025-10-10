class Route:
    def __init__(self, __route_id, departure_city, arrival_city, departure_time, arrival_time, train_type, days_of_operation, first_class_rate, second_class_rate):
        self.route_id = __route_id
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.train_type = train_type
        self.days_of_operation = days_of_operation
        self.first_class_rate = first_class_rate
        self.second_class_rate = second_class_rate
        self.trip_duration_days = 0
        self.trip_duration_hours = 0
        self.trip_duration_minutes = 0

        

    def calculate_duration(self):
        departure_time_values = self.departure_time.split(':')
        arrival_time_values = self.arrival_time.split(':')
        if "(+1d)" in arrival_time_values[1]:
            arrival_time_values[1] = arrival_time_values[1].split(" ")[0]
            self.trip_duration_days = 1

        if int(arrival_time_values[0]) < int(departure_time_values[0]):
            self.trip_duration_hours = (24 - int(departure_time_values[0])) + int(arrival_time_values[0])
        else:
            self.trip_duration_hours = int(arrival_time_values[0]) - int(departure_time_values[0])

        self.trip_duration_minutes = int(arrival_time_values[1]) - int(departure_time_values[1])

        if self.trip_duration_minutes < 0:
            self.trip_duration_hours = self.trip_duration_hours - 1
            self.trip_duration_minutes = 60 + self.trip_duration_minutes