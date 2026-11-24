
import numpy as np

# Create marks array
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [55, 65, 70]
])

# Print shape, dtype and size
print("Shape:", marks.shape)
print("Data type:", marks.dtype)
print("Size:", marks.size)

# Slice first two students and last subject
print("Sliced values:", marks[:2, 2])

# Calculate averages
print("Student averages:", np.round(marks.mean(axis=1), 2))
print("Subject averages:", marks.mean(axis=0))

# Add 5 grace marks using broadcasting
grace_marks = marks + 5
print("Grace marks:\n", grace_marks)

# Calculate weighted scores
weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.dot(marks, weights)
print("Weighted scores:", weighted_scores)

# Reshape arange into 3x4
arr = np.arange(12).reshape(3, 4)
print("Reshaped array:\n", arr)
