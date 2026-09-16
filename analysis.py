import pandas as pd

# Student data
data = {
    "Name": ["Anu", "Bala", "Divya", "Karthik", "Meena"],
    "Marks": [85, 72, 91, 65, 78],
    "Attendance": [95, 82, 98, 70, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student Performance Analysis")
print("----------------------------")

# Display student data
print(df)

# Calculate average marks
average_marks = df["Marks"].mean()
print("\nAverage Marks:", average_marks)

# Find highest marks
highest_marks = df["Marks"].max()
print("Highest Marks:", highest_marks)

# Find lowest marks
lowest_marks = df["Marks"].min()
print("Lowest Marks:", lowest_marks)

# Calculate average attendance
average_attendance = df["Attendance"].mean()
print("Average Attendance:", average_attendance)
