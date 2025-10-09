from utils.route import Route

class Trip_planner:
    def __init__(self, routes):
        self.routes = routes
        self.search()

    # TO-DO: search for routes using any parameter except ID
    def search(self):
        display = ["Departure City", "Arrival City", "Departure Time", "Arrival Time", "Train Type", "Days of Operation", "First-Class Rate", "Second-Class Rate", "Trip Duration"]
        while True:
            options = {1: "departure_city", 2: "arrival_city", 3: "departure_time", 4: "arrival_time", 5: "train_type", 6: "days_of_operation", 7: "first_class_rate", 8: "second_class_rate"}
            first_input = input("Select which criteria you wish to use to find your route: \n" \
            "1. Departure City\n" \
            "2. Arrival City\n" \
            "3. Departure Time\n" \
            "4. Arrival Time\n" \
            "5. Train Type\n" \
            "6. Days of Operation\n" \
            "7. First Class ticket rate (in euro)\n" \
            "8. Second class ticket rate (in euro)\n"
            "9. Exit\n")

            if (0 < int(first_input) < 9):
                second_input = input("Search here: ")
                print("Results: \n")
                counter = 0
                for line in self.routes:
                    variables = vars(line)
                    option = options[int(first_input)]
                    if (variables[option] == second_input):
                        for i in range(1, len(list(variables.values()))):
                            if (list(variables.values())[i] == None): 
                                print(display[i-1] + ": " + "None\n")
                            elif i == 1:
                                counter += 1
                                print(str(counter) + ". " + display[i-1] + ": " + list(variables.values())[i], end = ", ")
                            else: 
                                print(display[i-1] + ": " + list(variables.values())[i], end = ", ")
                if (counter == 0):
                    print("No results found\n")

            elif (int(first_input) == 9):
                break        
            else: 
                print("\nPlease select between 1 and 9.\n")
            
            
            
        

    # TO-DO: sort routes using an input parameter
    def sort_routes(self):
        pass

    # TO-DO: build custom route for two cities with no direct connection
    def construct_connections(self):
        pass