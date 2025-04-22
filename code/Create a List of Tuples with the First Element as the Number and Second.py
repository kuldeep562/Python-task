
# Q-121. Python Program to Create a List of Tuples with the First Element as the Number and Second
Element as the Square of the Number.

def create_tuples(n):
    tuples_list = [(i, i**2) for i in range(1, n+1)]
    return tuples_list


result = create_tuples(5)
print(result)

