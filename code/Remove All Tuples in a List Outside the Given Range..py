
# Q-122. Python Program to Remove All Tuples in a List Outside the Given Range.

def remove_outside_range(tuples_list, lower, upper):
    filtered_list = [tup for tup in tuples_list if lower <= tup[0] <= upper]
    return filtered_list


list_of_tuples = [(1, 4), (3, 9), (5, 25), (7, 49), (9, 81)]
lower_limit = 3
upper_limit = 7

result = remove_outside_range(list_of_tuples, lower_limit, upper_limit)
print(result)

