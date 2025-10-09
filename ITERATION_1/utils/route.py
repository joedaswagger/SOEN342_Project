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
        self.trip_duration = None

        

    # TO-DO: calculate duration from start to end of the trip
    def calculate_duration(depTime, arrTime):
        dep = depTime.split(':')
        arr = arrTime.split(':')

        

        hour = int(arr[0]) - int(dep[0])
        arr = arr[1].split(' (')
        minute = abs(int(arr[0]) - int(dep[1]))

        

        return str(hour) + " hours and " + str(minute) + " minutes"