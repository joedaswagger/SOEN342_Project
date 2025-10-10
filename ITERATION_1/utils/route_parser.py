import csv
import os
from utils.route import Route
import tkinter as tk
from tkinter import filedialog

class Route_parser:
    def __init__(self, default):
        self.default = default
        self.filepath = None
        self.file = None
        self.routes = []

        self.build_path()
        self.read_csv()

    def build_path(self):
        if self.default == False:
            root = tk.Tk()
            root.withdraw()

            try:
                root.attributes('-topmost', True)
            except Exception:
                pass

            self.filepath = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])
            root.destroy()

            if not self.filepath:  
                print("\nNo file selected. Using default CSV file.\n")
                self.default = True
        
        if self.default == True:
            absolute_path = os.path.dirname(__file__)
            self.filepath = os.path.join(absolute_path, "../data/eu_rail_network.csv")

    def read_csv(self):
        with open(self.filepath, mode ="r", encoding="utf8")as csv_file:
            self.file = csv.reader(csv_file)
            next(self.file)
            for line in self.file:
                route = Route(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
                route.calculate_duration()
                route.print_self()
                self.routes.append(route)