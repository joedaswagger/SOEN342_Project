from utils.route import Route

class Trip_planner:
    display = ["Departure City", "Arrival City", "Departure Time", "Arrival Time", "Train Type", "Days of Operation", "First-Class Rate", "Second-Class Rate", "Trip Duration"]
    counter = 0

    def __init__(self, routes):
        self.routes = routes
        self.search()

    # TO-DO: search for routes using any parameter except ID
    def search(self):
        
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
                print("\nNOTE: If searching days of operation, please do not input 'Mon' or 'Tue', simply type out the full days you wish to find. For daily trains, simply type 'Daily'.")
                second_input = input("Search here: ")
                print("Results: \n")
                Trip_planner.counter = 0
                for line in self.routes:
                    variables = vars(line)
                    option = options[int(first_input)]
                    if (int(first_input) == 6):
                        self.dayParser(variables, second_input)
                        daySearch = True
                    elif (variables[option].lower() == second_input.lower()):
                        self.printResults(variables)
                if (Trip_planner.counter == 0 and daySearch != True):
                    print("No results found\n")

            elif (int(first_input) == 9):
                break        
            else: 
                print("\nPlease select between 1 and 9.\n")

    
    def printResults(self, variables):
        isLastParam = False
        for i in range(1, len(list(variables.values()))):
            if (list(variables.values())[i] == None): 
                print(Trip_planner.display[i-1] + ": " + Route.calculate_duration(list(variables.values())[3], list(variables.values())[4]) + "\n")
                isLastParam = True
            elif i == 1:
                not isLastParam
                Trip_planner.counter += 1
                print(str(Trip_planner.counter) + ". " + Trip_planner.display[i-1] + ": " + list(variables.values())[i], end = ", ")
                
            else: 
                print(Trip_planner.display[i-1] + ": " + list(variables.values())[i], end = ", ")
            if((Trip_planner.counter) % 51 == 50 and isLastParam):
                input("\nPress enter to display more...")
                continue
    

            
    def dayParser(self, variables, second_input):
        days = {0: ["Monday", "Mon"], 1: ["Tuesday", "Tue"], 2: ["Wednesday", "Wed"], 3: ["Thursday", "Thu"], 4: ["Friday", "Fri"], 5: ["Saturday", "Sat"], 6: ["Sunday", "Sun"]}
        daysLookup = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
        operationDay = list(variables.values())[6]
        lst = [item[0] for item in list(days.values())]

        if(second_input.lower() == "Daily".lower()):
            dailyUsed = True
        else:
            dailyUsed = False

        for j in lst:
            if(j.lower() == second_input.lower() or dailyUsed == True): # Making sure you're putting in an actual day
                
                if("-" in operationDay): #if it's a range
                    first_day = operationDay.split('-')[0]
                    last_day = operationDay.split('-')[1]
                    for k in range(daysLookup.get(first_day), daysLookup.get(last_day) + 1):
                        if (days.get(k)[0].lower() == second_input.lower()):
                            self.printResults(variables)
                
                elif("," in operationDay): #if it's a list
                    listOfDays = operationDay.split(',')
                    loweredInput = ""
                    for k in range(len(list((days.keys())))):
                        if(second_input.lower() == days.get(k)[0].lower()):
                            loweredInput = days.get(k)[1]
                            
                    for l in range(len(listOfDays)):
                        if(listOfDays[l] == loweredInput):
                            self.printResults(variables)
                
                elif(operationDay == "Daily"):
                    self.printResults(variables)
                    if(second_input.lower() == "Daily".lower()):
                        dailyUsed = False

                else:
                    for k in range(len(list(days.keys()))):
                        if(second_input.lower() == days.get(k)[0].lower()):
                            self.printResults(variables)
                        
            

                            

    # TO-DO: sort routes using an input parameter
    def sort_routes(self):
        pass

    # TO-DO: build custom route for two cities with no direct connection
    def construct_connections(self):
        pass