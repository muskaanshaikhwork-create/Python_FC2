# Project 5: Bulk File Renaming

# Problem Statement:
# Often, we have a large number of files in a directory with names that do not
# follow a specific pattern or are not easy to understand. Renaming each file
# manually can be time-consuming and error-prone. To solve this problem, we
# need a program that can rename a large number of files in bulk, based on a
# specified pattern.

# Question:
# Can you develop a Python program that takes a directory path and a pattern
# as input, and renames all the files in the directory that match the pattern
# to a new name that follows the specified pattern?

import os

# Take directory path and pattern as input
directory = input("Enter the directory path: ")
pattern = input("Enter the pattern to search for: ")
new_pattern = input("Enter the new pattern: ")

# Get all files in the directory
files = os.listdir(directory)

count = 1

# Rename matching files
for file in files:
    old_path = os.path.join(directory, file)

    if os.path.isfile(old_path) and pattern in file:
        extension = os.path.splitext(file)[1]
        new_name = new_pattern + str(count) + extension
        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)

        print(f"Renamed: {file} -> {new_name}")
        count += 1

print("All matching files have been renamed successfully.")