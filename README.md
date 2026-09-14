# Student Performance Analyzer

A Python-based application that analyzes a student's academic performance based on their subject-wise marks.

## Features

* Accepts the student's name
* Allows the user to choose the number of subjects
* Accepts subject names and marks dynamically
* Calculates total marks
* Calculates average marks
* Assigns an overall grade
* Identifies the highest-scoring subject
* Identifies the lowest-scoring subject
* Displays pass/fail status for each subject

## Technologies Used

* Python

## Concepts Used

* Variables
* User input
* Type conversion
* Dictionaries
* Loops
* Conditional statements
* Built-in functions such as `sum()`, `len()`, `max()`, and `min()`

## How It Works

The program first asks the user for their name and the number of subjects.

It then collects each subject name and its corresponding marks and stores them in a dictionary.

The program uses the stored data to calculate the student's total and average, determine a grade, find the highest and lowest performing subjects, and display individual subject performance.

## Example

```text
Enter the student's name: Sanika
How many subjects? 3

Enter subject 1: Python
Enter marks for Python: 92

Enter subject 2: DBMS
Enter marks for DBMS: 78

Enter subject 3: Java
Enter marks for Java: 95

========== STUDENT PERFORMANCE REPORT ==========
Student: Sanika
Total Marks: 265
Average: 88.33
Grade: A

Highest: Java - 95
Lowest: DBMS - 78

---------- Subject Performance ----------
Python : 92 → Pass
DBMS : 78 → Pass
Java : 95 → Pass
==============================================
```

## Future Improvements

* Add input validation
* Support multiple students
* Store student records in CSV files
* Analyze data using Pandas
* Add performance visualizations
* Build a Streamlit dashboard
