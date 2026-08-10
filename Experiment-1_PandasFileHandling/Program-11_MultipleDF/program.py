import pandas as pd
student_data = {
    "Roll_No": [101, 102, 103, 104],
    "Name": ["Anusha", "Babitha", "Charitha", "Deepika"],
    "Department": ["IT", "IT", "CSE", "ECE"],
    "Percentage": [89, 92, 88, 85]
}
course_data={"Course_ID":["C101","C102","C103"],
             "Course_Name":["Python","Data Science","Machine Learning"],
             "Credits":[4,3,4]
}
students_df = pd.DataFrame(student_data)
courses_df=pd.DataFrame(course_data)
#Writing multiple data frames into different sheets
with pd.ExcelWriter("college_data.xlsx",engine="openpyxl") as writer:
    students_df.to_excel(writer,sheet_name="Students",index=False)
    courses_df.to_excel(writer,sheet_name="Courses",index=False)
print("Multiple sheets successfully written to college_data.xlsx")
