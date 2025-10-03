import csv
import os
from route import Route

class Route_parser:
    def __init__(self, relative_path):
        self.relative_path = relative_path
        self.filepath = None
        self.file = None
        self.routes = []

        self.build_path()
        self.read_csv()

    def build_path(self):
        absolute_path = os.path.dirname(__file__)
        self.filepath = os.path.join(absolute_path, self.relative_path)

    def read_csv(self):
        with open(self.filepath, mode ="r", encoding="utf8")as csv_file:
            self.file = csv.reader(csv_file)
            for line in self.file:
                print(line)