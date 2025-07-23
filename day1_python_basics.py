# DAY 1: Python Fundamentals for AI/ML
# Complete these exercises step by step

print("=== WELCOME TO YOUR AI/ML JOURNEY ===")
print("Goal: Master Python basics for Data Science & Machine Learning")
print("-" * 50)

# EXERCISE 1: Variables and Data Types
print("\n🏃‍♂️ EXERCISE 1: Variables and Data Types")

# TODO: Create variables for a simple AI project
project_name = "My First ML Project"
start_date = "2025-07-23"
estimated_completion_days = 30
is_beginner_friendly = True
programming_languages = ["Python", "SQL", "R"]

# Print information about your project
print(f"Project: {project_name}")
print(f"Start Date: {start_date}")
print(f"Duration: {estimated_completion_days} days")
print(f"Beginner Friendly: {is_beginner_friendly}")
print(f"Languages: {programming_languages}")

# EXERCISE 2: Lists and Loops (Data Structure Basics)
print("\n📊 EXERCISE 2: Working with Data Lists")

# Sample dataset: Student scores for ML model prediction
student_scores = [85, 92, 78, 96, 87, 73, 89, 94, 82, 91]

# TODO: Calculate basic statistics (like in data analysis)
total_students = len(student_scores)
total_score = sum(student_scores)
average_score = total_score / total_students
max_score = max(student_scores)
min_score = min(student_scores)

print(f"Total Students: {total_students}")
print(f"Average Score: {average_score:.2f}")
print(f"Highest Score: {max_score}")
print(f"Lowest Score: {min_score}")

# Filter high performers (above average) - like data filtering in ML
high_performers = []
for score in student_scores:
    if score > average_score:
        high_performers.append(score)

print(f"High Performers (>{average_score:.1f}): {high_performers}")

# EXERCISE 3: Functions (Code Reusability)
print("\n🔧 EXERCISE 3: Functions for ML")

def calculate_statistics(data_list):
    """
    Function to calculate basic statistics - essential for data analysis
    This is similar to what you'll do in pandas and numpy
    """
    stats = {
        'count': len(data_list),
        'mean': sum(data_list) / len(data_list),
        'max': max(data_list),
        'min': min(data_list),
        'range': max(data_list) - min(data_list)
    }
    return stats

def classify_performance(score, threshold=85):
    """
    Simple classification function - basic ML concept
    """
    if score >= threshold:
        return "High Performer"
    elif score >= 70:
        return "Average Performer"
    else:
        return "Needs Improvement"

# Test the functions
dataset_1 = [88, 76, 92, 84, 79, 95, 87]
dataset_2 = [65, 78, 82, 90, 73, 85, 88, 91]

print("Dataset 1 Statistics:")
stats_1 = calculate_statistics(dataset_1)
for key, value in stats_1.items():
    print(f"  {key}: {value:.2f}")

print("\nStudent Classifications:")
for i, score in enumerate(dataset_1, 1):
    classification = classify_performance(score)
    print(f"  Student {i} (Score: {score}): {classification}")

# EXERCISE 4: Dictionaries (Data Organization)
print("\n📋 EXERCISE 4: Data Organization with Dictionaries")

# Student data structure - similar to pandas DataFrame concept
students_data = {
    'names': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'math_scores': [88, 76, 92, 84, 79],
    'english_scores': [85, 82, 87, 91, 88],
    'science_scores': [90, 78, 95, 86, 84]
}

# Calculate total scores for each student
print("Student Performance Report:")
print("-" * 40)
for i in range(len(students_data['names'])):
    name = students_data['names'][i]
    math = students_data['math_scores'][i]
    english = students_data['english_scores'][i]
    science = students_data['science_scores'][i]
    total = math + english + science
    average = total / 3
    
    print(f"{name:8} | Math: {math:2d} | English: {english:2d} | Science: {science:2d} | Avg: {average:.1f}")

# EXERCISE 5: File Operations (Data I/O)
print("\n💾 EXERCISE 5: File Operations for Data")

# Create a simple dataset file
sample_data = """Name,Age,Programming_Experience,Interested_in_AI
Alice,20,2,Yes
Bob,19,1,Yes
Charlie,21,3,No
Diana,20,0,Yes
Eve,22,4,Yes"""

# Write to file
with open('student_survey.csv', 'w') as file:
    file.write(sample_data)

print("✅ Created 'student_survey.csv' file")

# Read from file
print("\nReading data from file:")
with open('student_survey.csv', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# CHALLENGE EXERCISE: Mini Data Analysis
print("\n🎯 CHALLENGE: Mini Data Analysis")

# Parse the CSV data manually (later you'll use pandas for this)
ai_interested_count = 0
total_experience = 0
student_count = 0

with open('student_survey.csv', 'r') as file:
    lines = file.readlines()[1:]  # Skip header
    for line in lines:
        data = line.strip().split(',')
        name, age, experience, ai_interest = data
        
        if ai_interest == 'Yes':
            ai_interested_count += 1
        
        total_experience += int(experience)
        student_count += 1

ai_percentage = (ai_interested_count / student_count) * 100
avg_experience = total_experience / student_count

print(f"Analysis Results:")
print(f"  Students interested in AI: {ai_interested_count}/{student_count} ({ai_percentage:.1f}%)")
print(f"  Average programming experience: {avg_experience:.1f} years")

# NEXT STEPS PREVIEW
print("\n🔮 COMING UP NEXT (Tomorrow's Session):")
print("1. Introduction to NumPy arrays")
print("2. Basic mathematical operations")
print("3. Introduction to data visualization")
print("4. Setting up your first GitHub repository")

print("\n✨ CONGRATULATIONS! You've completed Day 1!")
print("🎯 Tomorrow we'll dive into NumPy and start working with real data!")

# HOMEWORK
print("\n📝 TONIGHT'S HOMEWORK:")
print("1. Create a GitHub account if you haven't")
print("2. Install Anaconda and Jupyter Notebook")
print("3. Practice: Modify the functions above to add more features")
print("4. Read: 'What is Machine Learning?' (15 minutes)")