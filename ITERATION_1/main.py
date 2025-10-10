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
# manager = Trip_planner(parser.routes)

