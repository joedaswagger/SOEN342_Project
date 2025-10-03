import csv
import os
from utils.route import Route
# import tkinter as tk
# from tkinter import filedialog

class Route_parser:
    def __init__(self, default, relative_path):
        self.default = default
        self.relative_path = relative_path
        self.filepath = None
        self.file = None
        self.routes = []

        self.build_path()
        self.read_csv()

    def build_path(self):
        # root = tk.Tk()
        # root.withdraw()
        # x = filedialog.askopenfilename()
        absolute_path = os.path.dirname(__file__)
        self.filepath = os.path.join(absolute_path, self.relative_path)

    def read_csv(self):
        with open(self.filepath, mode ="r", encoding="utf8")as csv_file:
            self.file = csv.reader(csv_file)
            next(self.file)
            for line in self.file:
                route = Route(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
                self.routes.append(route)