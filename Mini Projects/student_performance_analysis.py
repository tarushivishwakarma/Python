import numpy as np
import pandas as pd

marks = np.array([
    [85, 80, 90],
    [70, 75, 65],
    [92, 88, 95],
    [60, 72, 68],
    [78, 82, 80]
])

# 1. Total marks obtained by each student
total = np.sum(marks, axis=1)
print("Total marks:", total)


# 2. Average marks of each student
average = np.mean(marks, axis=1)
print("Average marks:", average)


# 3. Average marks in each subject
subject_average = np.mean(marks, axis=0)
print("Subject averages:", subject_average)


# 4. Highest score in each subject
highest = np.max(marks, axis=0)
print("Highest score in each subject:", highest)


# 5. Lowest score in each subject
lowest = np.min(marks, axis=0)
print("Lowest score in each subject:", lowest)


# 6. Students whose average marks are above 80
above_80 = np.where(average > 80)[0]
print("Students with average above 80:", above_80)


# 7. Assign Pass or Fail status using np.where()
# Assuming average >= 50 means Pass
status = np.where(average >= 50, "Pass", "Fail")
print("Status:", status)


# 8. Index of the highest-performing student
highest_student = np.argmax(average)
print("Index of highest-performing student:", highest_student)


# 9. Standard deviation for each subject
std = np.std(marks, axis=0)
print("Standard deviation:", std)


# 10. Convert final results into Pandas DataFrame
df = pd.DataFrame({
    "Python": marks[:, 0],
    "SQL": marks[:, 1],
    "Machine Learning": marks[:, 2],
    "Total": total,
    "Average": average,
    "Status": status
})

print("\nFinal DataFrame:")
print(df)