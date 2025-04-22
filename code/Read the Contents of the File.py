
# Q-125. Python Program to Read the Contents of the File.

"""file 125.txt
      Hello World"""

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

file_path = 'txt file'
file_content = read_file(file_path)

print(file_content)


