import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1. CREATE DATASET

data = {
    "Semester": [
        # Semester 1
        1,1,1,1,1,1,1,1,1,

        # Semester 2
        2,2,2,2,2,2,2,2,2,2,

        # Semester 3
        3,3,3,3,3,3,3,3,3,3,

        # Semester 4
        4,4,4,4,4,4,4,4,4,

        # Semester 5
        5,5,5,5,5,5,5,5,5,5,

        # Semester 6
        6,6,6,6,6,6,6,6,6
    ],

    "Subject": [

        # Semester 1
        "Engineering Physics",
        "Engineering Mathematics-I",
        "Fundamentals of Electronics Engineering",
        "Fundamentals of Electrical Engineering",
        "Soft Skills",
        "Engineering Physics Lab",
        "Basic Electronics Engineering Lab",
        "English Language Lab",
        "Workshop Practice Lab",

        # Semester 2
        "Engineering Chemistry",
        "Engineering Mathematics-II",
        "Fundamentals of Electrical Engineering",
        "Programming for Problem Solving",
        "Environment and Ecology",
        "Engineering Chemistry Lab",
        "Basic Electrical Engineering Lab",
        "Programming for Problem Solving Lab",
        "Engineering Graphics & Design Lab",
        "Sports and Yoga",

        # Semester 3
        "Material Science",
        "Technical Communication",
        "Data Structures",
        "Computer Organization and Architecture",
        "Discrete Structures & Theory of Logic",
        "Cyber Security",
        "Data Structure Lab",
        "Computer Organization and Architecture Lab",
        "Web Designing Workshop",
        "Internship Assessment / Mini Project",

        # Semester 4
        "Mathematics-IV",
        "Universal Human Values and Professional Ethics",
        "Operating System",
        "Theory of Automata and Formal Languages",
        "Object Oriented Programming with Java",
        "Operating System Lab",
        "Object Oriented Programming with Java Lab",
        "Cyber Security Workshop",
        "Sports and Yoga-II",

        # Semester 5
        "Database Management System",
        "Web Technology",
        "Design and Analysis of Algorithm",
        "Object Oriented System Design with C++",
        "Application of Soft Computing",
        "Database Management System Lab",
        "Web Technology Lab",
        "Design and Analysis of Algorithm Lab",
        "Mini Project or Internship Assessment",
        "Constitution of India",

        # Semester 6
        "Software Engineering",
        "Compiler Design",
        "Computer Networks",
        "Blockchain Architecture Design",
        "IDEA TO BUSINESS MODEL",
        "Software Engineering Lab",
        "Compiler Design Lab",
        "Computer Networks Lab",
        "Essence of Indian Traditional Knowledge"
    ],

    "Marks": [

        # Semester 1
        85, 60, 86, 76, 79, 98, 96, 98, 98,

        # Semester 2
        80, 74, 88, 73, 82, 96, 97, 97, 97, 95,

        # Semester 3
        71, 79, 93, 77, 84, 83, 99, 99, 99, 70,

        # Semester 4
        79, 70, 80, 94, 84, 98, 99, 99, 99,

        # Semester 5
        74, 83, 65, 87, 82, 100, 100, 100, 100, 74,

        # Semester 6
        82, 75, 84, 71, 80, 100, 100, 100, 85
    ]
}

print(len(data["Semester"]))
print(len(data["Subject"]))
print(len(data["Marks"]))

df = pd.DataFrame(data)
print(df)


# 2. HOW MANY SEMESTERS?

print("\nQ2. Number of semesters:")
print(df["Semester"].nunique())


# 3. HOW MANY SUBJECTS IN TOTAL?

print("\nQ3. Total number of subject records:")
print(len(df))

print("\nUnique subjects:")
print(df["Subject"].nunique())


# 4. HIGHEST MARKS

print("\nQ4. Highest marks:")
print(df["Marks"].max())


# 5. LOWEST MARKS

print("\nQ5. Lowest marks:")
print(df["Marks"].min())


# 6. SEMESTER WITH HIGHEST TOTAL MARKS

semester_total = df.groupby("Semester")["Marks"].sum()

print("\nQ6. Semester-wise total marks:")
print(semester_total)

print("\nSemester with highest total:")
print(semester_total.idxmax())


# 7. SEMESTER WITH LOWEST TOTAL MARKS

print("\nQ7. Semester with lowest total:")
print(semester_total.idxmin())


# 8. FIRST FIVE RECORDS

print("\nQ8. First five records:")
print(df.head())


# 9. AVERAGE MARKS FOR EACH SEMESTER

semester_average = df.groupby("Semester")["Marks"].mean()

print("\nQ9. Semester-wise average marks:")
print(semester_average)


# 10. LINE GRAPH OF SEMESTER-WISE AVERAGE

plt.figure(figsize=(8,5))

plt.plot(
    semester_average.index,
    semester_average.values,
    marker="o"
)

plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.title("Semester-wise Average Marks")
plt.xticks(range(1,7))
plt.grid()

plt.show()

# 11. BAR GRAPH OF SUBJECT-WISE AVERAGE MARKS

subject_average = df.groupby("Subject")["Marks"].mean()

plt.figure(figsize=(14,7))

plt.bar(
    subject_average.index,
    subject_average.values
)

plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.title("Subject-wise Average Marks")

plt.xticks(rotation=90)
plt.tight_layout()

plt.show()

# 12. HIGHEST-PERFORMING SUBJECT

print("\nQ12. Highest-performing subject:")

highest_subject = subject_average.idxmax()
highest_subject_marks = subject_average.max()

print(highest_subject)
print("Marks:", highest_subject_marks)


# 13. LOWEST-PERFORMING SUBJECT

print("\nQ13. Lowest-performing subject:")

lowest_subject = subject_average.idxmin()
lowest_subject_marks = subject_average.min()

print(lowest_subject)
print("Marks:", lowest_subject_marks)


# 14. BEST AND WORST SEMESTER

print("\nQ14. Best semester:")
print(semester_average.idxmax())

print("Worst semester:")
print(semester_average.idxmin())


# 15. IMPROVEMENT BETWEEN SEMESTER 1 AND SEMESTER 6

sem1_avg = semester_average.loc[1]
sem6_avg = semester_average.loc[6]

improvement = sem6_avg - sem1_avg

print("\nQ15. Semester 1 average:", sem1_avg)
print("Semester 6 average:", sem6_avg)
print("Improvement:", improvement)

percentage_improvement = (improvement / sem1_avg) * 100

print("Percentage improvement:", percentage_improvement)


# 16. NUMPY STATISTICS

marks = np.array(df["Marks"])

print("\nQ16. NumPy Statistics")

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Standard Deviation:", np.std(marks))


# 17. PERFORMANCE OF SUBJECTS ACROSS SEMESTERS

plt.figure(figsize=(8,5))

plt.plot(
    semester_average.index,
    semester_average.values,
    marker="o"
)

plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.title("Performance Across Six Semesters")
plt.xticks(range(1,7))
plt.grid()

plt.show()


# 18. ACADEMIC TARGET = 75%

plt.figure(figsize=(8,5))

plt.plot(
    semester_average.index,
    semester_average.values,
    marker="o",
    label="My Average"
)

plt.axhline(
    y=75,
    linestyle="--",
    label="Target = 75%"
)

plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.title("Performance vs Academic Target")

plt.xticks(range(1,7))
plt.legend()
plt.grid()

plt.show()

# 19. CLASS AVERAGE
print("\nQ19.")
print("Class average data is not available.")


# 20. 2 x 2 MATPLOTLIB DASHBOARD

fig, ax = plt.subplots(2, 2, figsize=(15,10))


# Figure 1 - Semester-wise average

ax[0,0].plot(
    semester_average.index,
    semester_average.values,
    marker="o"
)

ax[0,0].set_title("Figure 1: Semester-wise Average")
ax[0,0].set_xlabel("Semester")
ax[0,0].set_ylabel("Average Marks")
ax[0,0].set_xticks(range(1,7))
ax[0,0].grid()


# Figure 2 - Subject-wise average


ax[0,1].bar(
    range(1,7),
    semester_average.values
)

ax[0,1].set_title("Figure 2: Semester Average Comparison")
ax[0,1].set_xlabel("Semester")
ax[0,1].set_ylabel("Average Marks")
ax[0,1].set_xticks(range(1,7))


# Figure 3 - Semester-wise total

ax[1,0].bar(
    semester_total.index,
    semester_total.values
)

ax[1,0].set_title("Figure 3: Semester-wise Total")
ax[1,0].set_xlabel("Semester")
ax[1,0].set_ylabel("Total Marks")
ax[1,0].set_xticks(range(1,7))


# Figure 4 - Performance vs target

ax[1,1].plot(
    semester_average.index,
    semester_average.values,
    marker="o",
    label="My Average"
)

ax[1,1].axhline(
    y=75,
    linestyle="--",
    label="Target = 75%"
)

ax[1,1].set_title("Figure 4: Performance vs Target")
ax[1,1].set_xlabel("Semester")
ax[1,1].set_ylabel("Average Marks")
ax[1,1].set_xticks(range(1,7))
ax[1,1].legend()
ax[1,1].grid()


plt.tight_layout()
plt.show()

# 21. FIVE OBSERVATIONS

print("\nQ21. FIVE OBSERVATIONS")

print("1. Semester 3 and Semester 4 have the highest total marks.")
print("2. Semester 1 has the highest average marks.")
print("3. Semester 6 has a lower average than Semester 1, showing a decline.")
print("4. Practical and laboratory subjects generally have higher marks.")
print("5. The semester averages remain above the academic target of 75%.")