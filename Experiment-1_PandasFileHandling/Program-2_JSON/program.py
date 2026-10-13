import pandas as pd
from io import StringIO
# Create sample student data
data = {
    "Roll_No": [101, 102, 103],
    "Name": ["Anusha", "Babitha", "Deepika"],
    "Department": ["IT", "CSE", "ECE"],
    "Marks": [89, 92, 85]
}
df = pd.DataFrame(data)
# Write data into a JSON file
df.to_json("students.json", orient="records", indent=4)
print("JSON file written successfully!")
# Read data from JSON file
json_data = pd.read_json("students.json")
print("\nData read from JSON file:")
print(json_data)
# Parse JSON formatted string
json_string = """
[
    {"Roll_No": 104, "Name": "Charitha", "Marks": 88},
    {"Roll_No": 105, "Name": "Harika", "Marks": 90}
]
"""
parsed_data = pd.read_json(StringIO(json_string))
print("\nParsed JSON Data:")
print(parsed_data)
# Read JSON data from an online API
url = "https://jsonplaceholder.typicode.com/users"
online_data = pd.read_json(url)
print("\nOnline JSON Dataset:")
print(online_data.head())
print("\nJSON operations completed successfully!")