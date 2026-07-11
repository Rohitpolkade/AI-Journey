import numpy as np

marks = np.array([10, 20, 30, 40, 50])
# print("marks:", marks)
# print(type(marks))

"""operation -- vectorization"""
# print(marks + 15)
# print(marks * 2)
# print(marks / 5)

"""functions -- statistics"""
# print(np.mean(marks))
# print(np.max(marks))
# print(np.min(marks))
# print(np.sum(marks))
# # var - variance
# print(np.var(marks))
# # std - standard deviation
# print(np.std(marks)) 

"""Filtering -- masking"""
print(marks > 30)

mask = marks > 30
filteredArr = marks[mask]
print(filteredArr)
print(marks[marks > 30])