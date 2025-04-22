
# Q-151. Python Program to Return the Length of the Longest Word from the List of Words

def find_longest_length(my_list):
   max_length = len(my_list[0])
   temp = my_list[0]

   for element in my_list:
      if(len(element) > max_length):

         max_length = len(element)
         temp = element
   return max_length

my_list = ["hey", "hi", "hola", "howdy"]
print("The list is :")
print(my_list)
print("The result is :")
print(find_longest_length(my_list))
