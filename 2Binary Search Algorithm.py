# Project 2: Binary Search Algorithm

# Problem Statement:
# You want to implement a Binary Search algorithm in Python to efficiently
# search for a target value in a sorted list.

# Question:
# How can I write a Python program that uses the Binary Search algorithm
# to find a target value in a sorted list?

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Sorted list
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# User input
target = int(input("Enter the number to search: "))

# Call the function
result = binary_search(numbers, target)

# Display the result
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")