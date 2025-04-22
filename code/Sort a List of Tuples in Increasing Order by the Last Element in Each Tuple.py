
# Q-123. Python Program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple

def sort_tuples_by_last_element(tuples_list):
    sorted_list = sorted(tuples_list, key=lambda x: x[-1])
    return sorted_list


list_of_tuples = [(3, 9), (1, 4), (5, 25), (7, 49), (9, 1)]

result = sort_tuples_by_last_element(list_of_tuples)
print(result)

