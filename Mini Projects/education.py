import pandas as pd

df = pd.read_csv("EducationDataset_2023-24.csv")

print(df)

### Q1. Which district has the highest and lowest number of schools?

highest_school = df.loc[df['No of Schools - Total'].idxmax()]
lowest_school = df.loc[df['No of Schools - Total'].idxmin()]

print(highest_school[['District', 'No of Schools - Total']])
print(lowest_school[['District', 'No of Schools - Total']])

### Q2. Which district has the highest total student enrollment?

result = df.loc[df['No of Students - Total'].idxmax()]
print(result[['District', 'No of Students - Total']])

### Q3. Compare boys and girls. Which district has the largest gender difference?

df['Gender Difference'] = abs(
    df['No of Students - Boys'] - df['No of Students - Girls']
)

result = df.loc[df['Gender Difference'].idxmax()]

print(result[['District',
              'No of Students - Boys',
              'No of Students - Girls',
              'Gender Difference']])

### Q4. Which district has the highest Class X pass percentage?

col_x = ' PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24'

result = df.loc[df[col_x].idxmax()]
print(result[['District', col_x]])

### Q5. Which district has the highest Class XII pass percentage?

col_xii = 'PASS PERCENTAGE IN CLASS XII - (Before Compt.) - 2023-24'

result = df.loc[df[col_xii].idxmax()]
print(result[['District', col_xii]])

### Q6. Compare Class X and Class XII pass percentages across districts.

print(df[['District', col_x, col_xii]])

df['XII-X Difference'] = df[col_xii] - df[col_x]

print(df[['District', col_x, col_xii, 'XII-X Difference']])

### Q7. Does number of schools appear related to Class X pass percentage?

correlation = df['No of Schools - Total'].corr(df[col_x])
print(correlation)

### Q8. Does total student enrollment appear related to Class X pass percentage?

correlation = df['No of Students - Total'].corr(df[col_x])
print(correlation)

### Q9. Calculate students per school. Which district has the highest value?

df['Students per School'] = (
    df['No of Students - Total'] /
    df['No of Schools - Total']
)

result = df.loc[df['Students per School'].idxmax()]

print(result[['District', 'Students per School', col_x]])

correlation = df['Students per School'].corr(df[col_x])
print(correlation)

# Q10. Three important observations using visualizations


### 1. Number of schools by district

import matplotlib.pyplot as plt

plt.figure(figsize=(12,5))
plt.bar(df['District'], df['No of Schools - Total'])
plt.xticks(rotation=90)
plt.xlabel("District")
plt.ylabel("Number of Schools")
plt.title("Number of Schools by District")
plt.show()


### 2. Class X vs Class XII pass percentage

plt.figure(figsize=(12,5))
plt.plot(df['District'], df[col_x], marker='o', label='Class X')
plt.plot(df['District'], df[col_xii], marker='o', label='Class XII')

plt.xticks(rotation=90)
plt.xlabel("District")
plt.ylabel("Pass Percentage")
plt.title("Class X vs Class XII Pass Percentage")
plt.legend()
plt.show()

### 3. Students per school vs Class X performance

plt.figure(figsize=(8,5))
plt.scatter(df['Students per School'], df[col_x])
plt.xlabel("Students per School")
plt.ylabel("Class X Pass Percentage")
plt.title("Students per School vs Class X Pass Percentage")
plt.show()