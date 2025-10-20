from utils.route import Route

class Trip_planner:
    display = ["Departure City", "Arrival City", "Departure Time", "Arrival Time", "Train Type", "Days of Operation", "First-Class Rate", "Second-Class Rate", "Trip Duration"]
    def __init__(self, routes):
        self.routes = routes
        self.search_results = []
        self.search_results_one_stop = []
        self.search_results_two_stops = []
        self.counter = 5

    def search(self):
        while True:
            self.search_results = []
            self.search_results_one_stop = []
            self.search_results_two_stops = []

            search_parameter = input("\nWhich parameter would you like to use for trip search: \n" \
            "1. City\n" \
            "2. Departure Time\n" \
            "3. Arrival Time\n" \
            "4. Train Type\n" \
            "5. Days of Operation\n" \
            "6. First Class ticket rate (in euro)\n" \
            "7. Second class ticket rate (in euro)\n"
            "8. Cancel\n")

            try:
                match int(search_parameter):
                    case 1:
                        input_departure_city = input("\nDeparture city name: ")
                        input_arrival_city = input("\nArrival city name: ")
                        for route in self.routes:
                            if route.departure_city.lower().strip() == input_departure_city.lower().strip() and route.arrival_city.lower().strip() == input_arrival_city.lower().strip():
                                self.search_results.append(route)
                        
                        if len(self.search_results) == 0:
                            depart_connections = [route for route in self.routes if route.departure_city.lower().strip() == input_departure_city.lower().strip()]
                            arrival_connections = [route for route in self.routes if route.arrival_city.lower().strip() == input_arrival_city.lower().strip()]

                            for connection in depart_connections:
                                for correspondance in arrival_connections:
                                    if connection.arrival_city.lower().strip() == correspondance.departure_city.lower().strip():
                                        self.search_results_one_stop.append({"initial": connection, "final": correspondance, "transfer_time": ""})

                        if len(self.search_results) == 0 and len(self.search_results_one_stop) == 0:
                            depart_connections = [route for route in self.routes if route.departure_city.lower().strip() == input_departure_city.lower().strip()]
                            first_stop_cities = [route.arrival_city.lower().strip() for route in depart_connections]
                            arrival_connections = [route for route in self.routes if route.arrival_city.lower().strip() == input_arrival_city.lower().strip()]
                            second_stop_cities = [route.departure_city.lower().strip() for route in arrival_connections]
                            middle_connections = [route for route in self.routes if route.departure_city.lower().strip() in first_stop_cities and route.arrival_city.lower().strip() in second_stop_cities]

                            for connection in depart_connections:
                                for middle in middle_connections:
                                    if connection.arrival_city.lower().strip() == middle.departure_city.lower().strip():
                                        for correspondance in arrival_connections:
                                            if middle.arrival_city.lower().strip() == correspondance.departure_city.lower().strip():
                                                self.search_results_two_stops.append({"initial": connection, "middle": middle, "final": correspondance, "transfer_time1": "", "transfer_time2": ""})

                        break
                    case 2:
                        while True:
                            time_input = input("\nEnter your preffered departure hour: ")
                            try:
                                if int(time_input) >= 24 or int(time_input) < 0:
                                    print("\nPlease enter a time from 0h to 23h\n")
                                else:
                                    for route in self.routes:
                                        if int(route.departure_time.split(":")[0]) == int(time_input):
                                            self.search_results.append(route)
                                    break
                            except:
                                print("\nPlease enter a numerical value\n")
                        break
                    case 3:
                        while True:
                            time_input = input("\nEnter your preffered arrival hour: ")
                            try:
                                if int(time_input) >= 24 or int(time_input) < 0:
                                    print("\nPlease enter a time from 0h to 23h\n")
                                else:
                                    for route in self.routes:
                                        if int(route.arrival_time.split(":")[0]) == int(time_input):
                                            self.search_results.append(route)
                                    break
                            except:
                                print("\nPlease enter a numerical value\n")
                        break
                    case 4:
                        train_types = [
                            "RJX", "ICE", "InterCity", "Frecciarossa", "RegioExpress", "EuroCity", "TGV", "Italo", "RE", "Nightjet", "Intercités", "Thalys", "Eurostar", "TER", "IC", "AVE", "Railjet"
                        ]

                        while True:
                            try:
                                for i, t in enumerate(train_types, start=1):
                                    print(f"{i}. {t}")
                                print("\n ")

                                train_selection = int(input("\nSelect a train type by index: "))

                                if train_selection < 1 or train_selection > 17:
                                    print("\nPlease enter a value from 1 to 17\n")
                                else:
                                    for route in self.routes:
                                        if route.train_type == train_types[train_selection - 1]:
                                            self.search_results.append(route)
                                    break

                            except ValueError:
                                print("\nPlease enter a numerical value\n")
                        break
                    case 5:
                        days_of_operation = [
                            "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
                        ]

                        while True:
                            try:
                                for i, t in enumerate(days_of_operation, start=1):
                                    print(f"{i}. {t}")
                                print("\n ")

                                day_seletion = int(input("\nSelect a travel day by index: "))

                                if day_seletion < 1 or day_seletion > 7:
                                    print("\nPlease enter a value from 1 to 7\n")
                                else:
                                    for route in self.routes:
                                        if route.days_of_operation == days_of_operation[day_seletion - 1]:
                                            self.search_results.append(route)
                                    break

                            except ValueError:
                                print("\nPlease enter a numerical value\n")
                        break
                    case 6:
                            minimum = input("\nEnter the smallest amount you're willing to spend: ")
                            maximum = input("\nEnter the largest amount you're willing to spend: ")
                            try:
                                if float(maximum) < float(minimum):
                                    print("\nThe largest amount must be equal or greater than the smallest amount.\n")
                                else:
                                    for route in self.routes:
                                        if float(route.first_class_rate) >= float(minimum) and float(route.first_class_rate) <= float(maximum):
                                            self.search_results.append(route)
                                    break
                            except:
                                print("\nPlease enter a numerical value\n")
                    case 7:
                            minimum = input("\nEnter the smallest amount you're willing to spend: ")
                            maximum = input("\nEnter the largest amount you're willing to spend: ")
                            try:
                                if float(maximum) < float(minimum):
                                    print("\nThe largest amount must be equal or greater than the smallest amount.\n")
                                else:
                                    for route in self.routes:
                                        if float(route.second_class_rate) >= float(minimum) and float(route.first_class_rate) <= float(maximum):
                                            self.search_results.append(route)
                                    break
                            except:
                                print("\nPlease enter a numerical value\n")
                    case 8:
                        print("\nReturning to main menu\n")
                    case _:
                        print("\nPlease select a number from 1 to 9\n")
            except ValueError:
                print("\nPlease enter a numerical selection\n")
        
        self.print_results()

    def print_results(self):
        self.calculate_transfer_times()

        print("\n" + str(len(self.search_results)) + " connections found for the search criteria.\n")

        for route in self.search_results:
            route.print_self()
            print("____________________________________")

        if len(self.search_results) == 0:
            print("\nNo connection found; generating one-stop correspondances...\n")

            for route in self.search_results_one_stop:
                route["initial"].print_self()
                print("\nCORRESPONDING WITH " + route["transfer_time"])
                route["final"].print_self()
                print("____________________________________")

        if len(self.search_results_one_stop) == 0 and len(self.search_results) == 0:
            print("\nNo one-stop correspondance found; generating two-stops correspondances...\n")

            for route in self.search_results_two_stops:
                route["initial"].print_self()
                print("\nCORRESPONDING WITH " + route["transfer_time1"])
                route["middle"].print_self()
                print("\nCORRESPONDING WITH " + route["transfer_time2"])
                route["final"].print_self()
                print("____________________________________")

        if len(self.search_results_two_stops) == 0 and len(self.search_results_one_stop) == 0 and len(self.search_results) == 0:
            print("\nNo two-stop correspondance found.\n")

    def sort(self):
        while True:
            sort_parameter = input("\nWhich parameter would you like to use for trip sorting: \n" \
                "1. Trip duration\n" \
                "2. First Class ticket rate (in euro)\n" \
                "3. Second class ticket rate (in euro)\n"
                "4. Cancel\n")
            
            direction_input = input("\nDo you want to sort ascending (press ENTER) or descending (any input): ")
            direction_reverse = False if direction_input == "" else True
            
            try:
                match int(sort_parameter):
                    case 1:
                        self.search_results = sorted(self.search_results, key=lambda c: c.trip_duration, reverse = direction_reverse)
                        break
                    case 2:
                        self.search_results = sorted(self.search_results, key=lambda c: c.first_class_rate, reverse = direction_reverse)
                        break
                    case 3:
                        self.search_results = sorted(self.search_results, key=lambda c: c.second_class_rate, reverse = direction_reverse)
                        break
                    case 4:
                        print("\nReturning to main menu\n")
                        break
                    case _:
                        print("\nPlease select a number from 1 to 4\n")
            except ValueError:
                print("\nPlease enter a numerical selection\n")

        self.print_results()      

    def calculate_transfer_times(self):
        if len(self.search_results_one_stop) != 0:
            for connection in self.search_results_one_stop:
                start_time_values = connection["initial"].arrival_time.split(":")
                end_time_values = connection["final"].departure_time.split(":")

                connection["transfer_time"] = self.time_calculator(start_time_values, end_time_values)

        if len(self.search_results_two_stops) != 0:
            for connection in self.search_results_two_stops:
                start_time_values = connection["initial"].arrival_time.split(":")
                end_time_values = connection["middle"].departure_time.split(":")

                connection["transfer_time1"] = self.time_calculator(start_time_values, end_time_values)

                start_time_values = connection["middle"].arrival_time.split(":")
                end_time_values = connection["final"].departure_time.split(":")

                connection["transfer_time2"] = self.time_calculator(start_time_values, end_time_values)

    def time_calculator(self, start_time_values, end_time_values):
        hours = 0

        if "(+1d)" in start_time_values[1]:
            start_time_values[1] = start_time_values[1].split(" ")[0]

        if int(end_time_values[0]) < int(start_time_values[0]):
            hours = (24 - int(start_time_values[0])) + int(end_time_values[0])
        else:
            hours = int(end_time_values[0]) - int(start_time_values[0])

        minutes = int(end_time_values[1]) - int(start_time_values[1])

        if minutes < 1:
            hours = hours - 1
            minutes = 60 + minutes

        return f"(transfer time: {hours} hours and {minutes} minutes)"