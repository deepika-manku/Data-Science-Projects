import pandas as pd
student_data={
    "Roll_No":[101,102,103,104],
    "Name":["Anusha","Babitha","Charitha","Deepika"],
    "Department":["IT","IT","CSE","ECE"],
    "Percentage":[89,92,88,85]
}
df=pd.DataFrame(student_data)
df.to_csv("student_output.txt",sep="\t",index=False)
print("Data successfully written to student_output.txt")