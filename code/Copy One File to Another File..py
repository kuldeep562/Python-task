
# Q-126. Python Program to Copy One File to Another File.

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        return f"File '{source_file}' copied to '{destination_file}' successfully."
    except FileNotFoundError:
        return f"One of the files not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


source_file_path = 'source_path' 
destination_file_path = 'destine_path'  

result = copy_file(source_file_path, destination_file_path)
print(result)

