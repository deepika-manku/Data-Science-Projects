import pandas as pd
#Reading all sheets
excel_data=pd.read_excel("college_data.xlsx",sheet_name=None)
print("Available sheets:")
print(excel_data.keys())
print("Student sheet:")
print(excel_data["Students"])
print("Course sheet:")
print(excel_data["Courses"])