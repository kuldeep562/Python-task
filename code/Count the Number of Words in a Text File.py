
# Q-130. Python Program to Count the Number of Words in a Text File

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
        return f"The file '{file_path}' has {word_count} words."
    except FileNotFoundError:
        return f"File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


file_path = '/content/drive/MyDrive/Colab Notebooks/program/130.txt'  

result = count_words(file_path)
print(result)


