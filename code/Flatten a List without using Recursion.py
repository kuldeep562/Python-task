
# Q-158. Python Program to Flatten a List without using Recursion

def flatten(lst):
    result = []
    for x in lst:
        if isinstance(x, list):
            result.extend(flatten(x))
        else:
            result.append(x)
    return result
 
 
l = [1, 2, [3, 4, [5, 6], 7], [[[8, 9], 10]], [11, [12, 13]]]
ans = flatten(l)
print(ans)
