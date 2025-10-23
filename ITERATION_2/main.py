from utils.route_parser import Route_parser
from utils.trip_planner import Trip_planner
from database.database import Database
from utils.authenticator import Authenticator

def main():
    parser = Route_parser(True)
    planner = Trip_planner(parser.routes)
    db = Database()
    auth = Authenticator()

    current_user = None

    while True:
        menu = input("[MENU] Please select an operation:\n" \
            "1. Search for connections\n" \
            "2. Sort previous results\n" \
            "3. Authenticate yourself\n" \
            "4. Book a trip from previous results\n" \
            "5. Exit\n")
        
        try:
            match int(menu):
                case 1:
                    planner.search()
                case 2:
                    planner.sort()
                case 3:
                    while True:
                        auth_option = input("\nDo you already own an account? (y/n)")
                        if auth_option.strip().lower() == "y":
                            current_user = auth.sign_in
                            break
                        elif auth_option.strip().lower() == "n":
                            current_user = auth.sign_up
                            break
                        else:
                            print("\nInvalid selection.")
                case 4:
                    if (current_user == None):
                        print("\nYou must authenticate (menu-3) in order to book a trip.\n")
                        break
                case 5:
                    print("\nThank you for using our trip search algorithm!\n")
                    break
                case _:
                    print("\nPlease select an option from the menu\n")
        except ValueError:
            print("\nPlease enter a numerical selection\n")

if __name__=="__main__":
    main()