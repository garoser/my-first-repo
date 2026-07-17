import csv
import math


def add_numbers(a, b):
    return a + b

# calculate the area of a circle given its radius

def calculate_circle_area(radius):
    return math.pi * radius ** 2

# calculate the circumference of a circle given its radius

def calculate_circle_circumference(radius):
    return 2 * math.pi * radius

# Read a .csv file provided on the command line and return a list of dictionaries

def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

