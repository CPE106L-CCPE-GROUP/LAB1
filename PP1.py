'''
Group #: CCPE
Group Members: Cielo Joyce Ando, Pamela Nicole de Guzman, Gabriel Vargas
Date Submitted: March 2, 2023
Program Description: 
This program takes a list of numbers as input and calculates its mean, median, and mode. 
The mean is the average of all the numbers in the list. The median is the number that would 
appear at the midpoint of a list if it were sorted. If the list has an even number of values, 
the median is the average of the two middle values. The mode is the number that appears most 
frequently in the list. A single or a multiple number of modes can be displayed.
Filename: PP1.py
'''


# This function is used to find the mean of an input list
def mean(numbers):
    # Check if the input list is empty
    if len(numbers) == 0:
        return None

    # Return the mean
    total = sum(numbers)
    return total / len(numbers)


# This function is used to find the median of an input list
def median(numbers):
    # Sort the elements in the input list
    numbers.sort()
    length = len(numbers)

    # Return the median of the list
    if length % 2 == 0:
        return (numbers[length//2] + numbers[length//2 - 1]) / 2
    else:
        return numbers[length//2]


# This function is used to find the mode/s of an input list
def mode(numbers):
    # Compute the frequency count of each element in the input list
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_count = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_count]

    # Return the mode/s of the list
    if len(modes) == 1:
        return modes[0]
    else:
        return modes


# This part outputs the elements of the list, including its mean, median, and mode
numbers = [8, 5, 6, 1, 6, 5, 6, 3, 5, 3]
print("Elements in the list:", numbers)
print("Mean: ", mean(numbers))
print("Median:", median(numbers))
print("Mode/s:", mode(numbers))
