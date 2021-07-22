import pandas as pd
import csv
import numpy as np

def get_data_source(path):
    percentage = []
    days = []
    with open(path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            percentage.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))

    return {"x" : percentage, "y": days}


def find_correlation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Percentage of marks and days present is :-  \n--->",correlation[0,1])

def setup():
    path = 'Student Marks vs Days Present.csv'
    data_source = get_data_source(path)
    find_correlation(data_source)

setup()