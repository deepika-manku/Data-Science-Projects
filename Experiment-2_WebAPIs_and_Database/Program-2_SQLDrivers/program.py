import sqlite3
import pandas as pd
#Connect to database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
#Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY, name TEXT)''')
cursor.execute("INSERT INTO students VALUES(1,'John')")
cursor.execute("INSERT INTO students VALUES(2,'Jane')")
conn.commit()
#Query the database
df=pd.read_sql_query("SELECT * FROM students", conn)
print(df)
cursor.execute("UPDATE students SET name='Alice' WHERE id=1")
cursor.execute("DELETE FROM students WHERE id=1")
conn.commit()
conn.close()