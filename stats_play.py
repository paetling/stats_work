import random
import math

def generate_100_random_numbers():
    numbers = []
    for i in range(100):
        numbers.append(random.randint(0, 1000))
    return numbers

def get_mean_of_list(numbers):
    total = 0
    count = 0
    for x in numbers:
        total += x
        count += 1
    return total * 1.0 / count

def get_absolute_deviation(numbers, comparison=None):
    if not comparison:
        comparison = get_mean_of_list(numbers)

    total = 0
    count = 0
    for x in numbers:
        total += math.fabs(x-comparison)
        count += 1
    return total * 1.0 / count

def get_variance_of_list(numbers, comparison=None):
    if not comparison:
        comparison = get_mean_of_list(numbers)

    total = 0
    count = 0
    for x in numbers:
        total += math.pow(math.fabs(x-comparison), 2)
        count += 1
    return total * 1.0 / count

def get_std_of_list(numbers, comparison=None):
    return math.sqrt(get_variance_of_list(numbers, comparison))

def get_std_as_proprtion_of_ad(numbers):
    ad = get_absolute_deviation(numbers)
    std = get_std_of_list(numbers)

    return (std - ad * 1.0) / ad * 100

def get_median(numbers):
    sorted_numbers = sorted(numbers)
    middle_index = len(numbers) / 2
    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[middle_index] * 1.0 + sorted_numbers[middle_index-1]) / 2
    return sorted_numbers[middle_index]


def get_simple_linear_regression_slope(x_numbers, y_numbers):
    x_mean = get_mean_of_list(x_numbers)
    y_mean = get_mean_of_list(y_numbers)

    total = 0
    for i in range(len(x_numbers)):
        total += (x_numbers[i] - x_mean) * (y_numbers[i] - y_mean) / (x_numbers[i] - x_mean) ** 2
    return total

def get_simple_linear_regression_inserect(x_numbers, y_numbers):
    slope = get_simple_linear_regression_slope(x_numbers, y_numbers)
    x_mean = get_mean_of_list(x_numbers)
    y_mean = get_mean_of_list(y_numbers)

    return y - (slope * x_mean)




# print get_absolute_deviation(list1), get_std_of_list(list1)

for i in range(5):
    numbers = generate_100_random_numbers()
    median = get_median(numbers)
    print "For mean: ", get_absolute_deviation(numbers), get_std_of_list(numbers)
    print "For median: ", get_absolute_deviation(numbers, median), get_std_of_list(numbers, median)
    print ""

numbers = [-3, -2, -1, 1, 2]
median = get_median(numbers)
print "For mean: ", get_absolute_deviation(numbers), get_std_of_list(numbers)
print "For median: ", get_absolute_deviation(numbers, median), get_std_of_list(numbers, median)
print ""

