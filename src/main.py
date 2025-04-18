# main.py
# Authors:
#   Carmen Bland Jr
#   Sydney Seder
#   Sam Gil

import os
import pandas as pd

# Load in data from excel file
def data_load(filename):
    """data_load Loads data from an excel file for usage in other methods

    Keyword Arguments:
    filename - a PathLike object containing path to excel sheet.
    """
    data = pd.read_excel(filename, header=0, engine='openxyl')
    return data

def main():
    pass

if "__name__" == "__main__":
    main():
