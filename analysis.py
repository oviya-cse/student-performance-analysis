import pandas as pd

# Load the student data
df = pd.read_csv("student_data.csv")

print("STUDENT PERFORMANCE ANALYSIS")
print("-----------------------------")

# Display the data
print("\nStudent Data:")
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
