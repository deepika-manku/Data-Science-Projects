import pandas as pd
# Create student data
student_data = {
    "Roll_No": [101, 102, 103, 104],
    "Name": ["Anusha", "Babitha", "Charitha", "Deepika"],
    "Department": ["IT", "IT", "CSE", "ECE"],
    "Percentage": [89, 92, 88, 85]
}

df = pd.DataFrame(student_data)
# Write data into an Excel file
df.to_excel(
    "students.xlsx",
    sheet_name="Students",
    index=False
)
print("Excel file created successfully!")
# Read data from Excel file
excel_data = pd.read_excel("students.xlsx", sheet_name="Students")
print("\nData read from Excel file:")
print(excel_data)
# Create another DataFrame
course_data = {
    "Course_ID": ["C101", "C102", "C103"],
    "Course_Name": ["Python", "Data Science", "Machine Learning"]
}
df2 = pd.DataFrame(course_data)
# Write multiple sheets into one Excel workbook
with pd.ExcelWriter("college_data.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Students", index=False)
    df2.to_excel(writer, sheet_name="Courses", index=False)
print("\nMultiple Excel sheets created successfully!")
# Read all sheets from Excel file
all_sheets = pd.read_excel("college_data.xlsx", sheet_name=None)
for sheet, data in all_sheets.items():
    print("\nSheet:", sheet)
    print(data)
print("\nExcel operations completed successfully!")