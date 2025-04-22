
# Q-129. Python Program to Count the Occurrences of a Word in a Text File.

def count_word_occurrences(file_path, target_word):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            occurrences = content.lower().count(target_word.lower())
        return f"The word '{target_word}' occurs {occurrences} times in the file."
    except FileNotFoundError:
        return f"File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


file_path = '/content/drive/MyDrive/Colab Notebooks/program/129.txt'  
word_to_count = 'Python'  

result = count_word_occurrences(file_path, word_to_count)
print(result)

