# This Script Shows how to work with an excel file using pandas.
#
# Script Output
#	1) Opening Excel file
#   2) Read field
#
import pandas as pd
from openpyxl import Workbook 

"""
1) Opening the Excel File

"""


# We Will buidl a data frame from an excel file
# xlsx files require the openpyxl module, older files do not require this engine
df = pd.read_excel("workbook.xlsx",engine='openpyxl')

# The len() function will inform us on how many rows are in the excel file
# this helps with writing loops if you need to iterate through the data
len(df)

#For clarity we will now call the excel file a data frame or df for short
#The following show our current df
df
print(df)


