from utils.route_parser import Route_parser
from utils.trip_planner import Trip_planner

default_path = None

while True:
    default_input = input("Do you want to\n   1) Use our default CSV file\n   2) Select a CSV file\n")
    try:
        default_input = int(default_input)
        if default_input == 1:
            default_path = True
            break
        elif default_input == 2:
            default_path = False
            break
        else:
            print("\nPlease select between 1 and 2.\n")
    except:
        print("\nPlease input a numeric value.\n")

parser = Route_parser(default_path)
planner = Trip_planner(parser.routes)

while True:
    menu = input("\n[MENU] Please select an operation:\n" \
        "1. Search connections\n" \
        "2. Sort previous results\n" \
        "3. Exit\n")
    
    try:
        match int(menu):
            case 1:
                planner.search()
            case 2:
                planner.sort()
            case 3:
                print("\nThank you for using our trip search algorithm!\n")
                break
            case _:
                print("\nPlease select an option from the menu\n")
    except ValueError:
        print("\nPlease enter a numerical selection\n")