from pathlib import Path

# Reading from and writing to files with exception handling
def read_file(file_path):
    """Read and return the contents of a file."""
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
    except FileNotFoundError:
        return f"The file at {file_path} was not found."
    else:
        return contents
    
def write_to_file(file_path, data):
    """Write data to a file."""
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except IOError as e:
        return f"An error occurred while writing to the file: {e}"
    else:
        return f"Data successfully written to {file_path}."
    
# Using pathlib for file paths
def get_file_path(directory, filename):
    """Construct a file path using pathlib."""
    path = Path(directory) / filename
    return path

# Accessing a file's lines
def read_file_lines(file_path):
    """Read and return the lines of a file as a list."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        return f"The file at {file_path} was not found."
    else:
        return [line.strip() for line in lines]
    
    
# Appending data to a file
def append_to_file(file_path, data):
    """Append data to a file."""
    try:
        with open(file_path, 'a') as file:
            file.write(data + '\n')
    except IOError as e:
        return f"An error occurred while appending to the file: {e}"
    else:
        return f"Data successfully appended to {file_path}."
    
# Exceptions

def divide_numbers(num1, num2):
    """Divide two numbers with exception handling."""
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Both inputs must be numbers."
    else:
        return result

