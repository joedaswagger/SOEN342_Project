from utils.route import Route

class Trip_planner:
    display = ["Departure City", "Arrival City", "Departure Time", "Arrival Time", "Train Type", "Days of Operation", "First-Class Rate", "Second-Class Rate", "Trip Duration"]
    def __init__(self, routes):
        self.routes = routes
        self.search_results = []
        self.counter = 5

    def search(self):
        while True:
            self.search_results = []

            search_parameter = input("\nWhich parameter would you like to use for trip search: \n" \
            "1. Departure City\n" \
            "2. Arrival City\n" \
            "3. Departure Time\n" \
            "4. Arrival Time\n" \
            "5. Train Type\n" \
            "6. Days of Operation\n" \
            "7. First Class ticket rate (in euro)\n" \
            "8. Second class ticket rate (in euro)\n"
            "9. Cancel\n")

            try:
                match int(search_parameter):
                    case 1:
                        input_city = input("\nCity name: ")
                        for route in self.routes:
                            if route.departure_city.lower().strip() == input_city.lower().strip():
                                self.search_results.append(route)
                    case 2:
                        input_city = input("\nCity name: ")
                        for route in self.routes:
                            if route.arrival_city.lower().strip() == input_city.lower().strip():
                                self.search_results.append(route)
                    case 3:
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
                    case 4:
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
                    case 5:
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
                                        if route.train_type == train_types[train_selection]:
                                            self.search_results.append(route)
                                    break

                            except ValueError:
                                print("\nPlease enter a numerical value\n")
                    case 6:
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
                                        if route.days_of_operation == days_of_operation[day_seletion]:
                                            self.search_results.append(route)
                                    break

                            except ValueError:
                                print("\nPlease enter a numerical value\n")
                    case 7:
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
                    case 8:
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
                    case 9:
                        print("\nReturning to main menu\n")
                    case _:
                        print("\nPlease select a number from 1 to 9\n")
            except ValueError:
                print("\nPlease enter a numerical selection\n")

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