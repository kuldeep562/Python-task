
# Q-127. Python Program to Count the Number of Lines in Text File

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return f"The file '{file_path}' has {line_count} lines."
    except FileNotFoundError:
        return f"File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

file_path = '/content/drive/MyDrive/Colab Notebooks/program/127.txt'  

result = count_lines(file_path)
print(result)


