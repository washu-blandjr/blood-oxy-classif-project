# main.py
#   Authors:
#       Carmen Bland Jr
#       Sydney Seder
#       Sam Gil

import os
import logging
import pandas as pd
# TODO: Import any other libraries you need for our ML model, (maybe scikit-learn, etc.)

# Constants
EXCEL_FILE_NAME = 'Combined.xlsx' # Name of the excel file to load
EXCEL_FILE_PATH = os.path.join(os.path.dirname(__file__), 'data', EXCEL_FILE_NAME) # Name of the excel path
EXCEL = {'name': EXCEL_FILE_NAME, 'path': EXCEL_FILE_PATH} # Dictionary containing the name and path of the excel file

# Logging configuration
logger = logging.getLogger(__name__) # Create a logger object
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') # Set up basic configuration

# Load in data from excel file
def data_load(filename):
    """data_load Loads data from an excel file for usage in other methods

    Keyword Arguments:
    filename - a PathLike object containing path to excel sheet.
    """
    data = pd.read_excel(filename, header=0, engine='openxyl')
    return data

# TODO: Add a function to train the ML Model
def train_model(insert_parameters_here):
    pass

# TODO: Add a function to test the ML Model
def test_model(insert_parameters_here):
    pass


def main():
    filename = EXCEL['path'] # Path to the Combined excel file
    logger.debug("Loading data from %s", filename)
    
    exceldata = data_load(filename) # Load the data from the excel file
    
    if exceldata is None:
        logger.error("Failed to load data from %s", filename)
        return

if "__name__" == "__main__":
    main()
