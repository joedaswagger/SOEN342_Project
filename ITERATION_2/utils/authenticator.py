from database.database import Database
from models.client import Client

class Authenticator:
    def __init__(self):
        self.db = Database()

    def sign_in(self):
        last_name = input("Last name: ")
        id = input("ID: ")
        return self.db.get_client(last_name, id)

    def sign_up(self):
        first_name = input("First name: ")
        last_name = input("Last name: ")
        id = input("ID (e.g.: student ID): ")
        age = input("Age: ")
        try:
            age = int(age)
        except:
            age = 0
        return self.db.insert_client(first_name, last_name, age, id)