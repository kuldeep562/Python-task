
# Q-128. Python Program to Count the Number of Blank Spaces in a Text File

def count_blank_spaces(file_path):
    try:
        with open(file_path, 'r') as file:
            blank_count = 0
            for line in file:
               
                blank_count += line.count(' ') + line.count('\t')
               
                if line.strip() == '':
                    blank_count += 1
        return f"The file '{file_path}' has {blank_count} blank spaces."
    except FileNotFoundError:
        return f"File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

file_path = 'file_path'  

result = count_blank_spaces(file_path)
print(result)



