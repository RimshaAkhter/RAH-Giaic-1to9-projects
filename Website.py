import streamlit as st
import pandas as pd
import random

# Set page configuration
st.set_page_config(page_title="Students Data Generator", layout="wide")

# Title of the page
st.title("Student CSV File Generator")

# List of sample names for students
names = ["Haider", "Ifra", "Ali", "Noor", "Fatima", "Saad", "Mehmal", "Faris", "Haris", "Maryam", "Zumer", "Imama"]

# List to store student data
students = []

# Generate student data
for i in range(1, 12):  # Create 11 students
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Grade": random.choice(["A", "B", "C", "D", "E", "F"]),
        "Marks": random.randint(40, 100)
    }
    students.append(student)

# Convert data to a DataFrame
df = pd.DataFrame(students)

# Display the generated student data
st.subheader("Generated Students Data")
st.dataframe(df)

# Convert DataFrame to CSV
csv_file = df.to_csv(index=False).encode('utf-8')

# Button to download the CSV file
st.download_button("Download CSV File", csv_file, "students.csv", "text/csv")

# Success message after generation
st.success("✅ Students Record Generated Successfully!")

