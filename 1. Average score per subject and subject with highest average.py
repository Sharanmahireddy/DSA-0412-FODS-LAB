import numpy as np

# Sample 4x4 matrix (32x4 in real case)
student_scores = np.array([[80, 90, 85, 88],
                           [78, 85, 90, 86],
                           [88, 82, 84, 90],
                           [92, 89, 80, 84]])

# Average score per subject (column-wise)
subject_averages = np.mean(student_scores, axis=0)
subjects = ['Math', 'Science', 'English', 'History']

# Subject with highest average
highest_avg_subject = subjects[np.argmax(subject_averages)]

print("Average scores:", subject_averages)
print("Highest average subject:", highest_avg_subject)
