import pandas as pd
# Read an online CSV dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
print("CSV Dataset:")
print(df.head())
# Write data into a CSV file
df.to_csv("iris_output.csv", index=False)
print("\nCSV file written successfully!")
# Read the CSV file
csv_data = pd.read_csv("iris_output.csv")
print("\nData read from CSV file:")
print(csv_data.head())
# Create a sample DataFrame
data = {
    "Roll_No": [101, 102, 103],
    "Name": ["Anusha", "Babitha", "Deepika"],
    "Department": ["IT", "CSE", "ECE"]
}
df2 = pd.DataFrame(data)
# Write data into a tab-delimited text file
df2.to_csv("students.txt", sep="\t", index=False)
print("\nTab-delimited file written successfully!")
# Read the tab-delimited text file
text_data = pd.read_csv("students.txt", sep="\t")
print("\nData read from text file:")
print(text_data)