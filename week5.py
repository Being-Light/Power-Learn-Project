# File Creation: Create and write to the file
try:
    # Open file in write mode ('w'). If it doesn't exist, it will be created.
    with open('my_file.txt', 'w') as file:
        file.write("This is the first line.\n")
        file.write("The second line contains a number: 42\n")
        file.write("Third line: Python is fun!\n")
    print("File 'my_file.txt' has been created and data has been written.")
except PermissionError:
    print("Error: You do not have permission to write to this file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File writing process finished.")

# File Reading and Display: Read and display the file contents
try:
    with open('my_file.txt', 'r') as file:
        print("\n--- File Content ---")
        content = file.read()  # Read the entire content of the file
        print(content)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
finally:
    print("File reading process finished.")

# File Appending: Open the file in append mode ('a') and add more lines
try:
    with open('my_file.txt', 'a') as file:
        file.write("Fourth line: Appending new content.\n")
        file.write("Fifth line: More numbers here: 123, 456.\n")
        file.write("Sixth line: The end of this append operation.\n")
    print("\nNew lines have been appended to 'my_file.txt'.")
except PermissionError:
    print("Error: You do not have permission to append to this file.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")
finally:
    print("File appending process finished.")

# File Reading Again: Read and display the updated file contents
try:
    with open('my_file.txt', 'r') as file:
        print("\n--- Updated File Content ---")
        content = file.read()  # Read the entire content again
        print(content)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    print(f"An error occurred while reading the updated file: {e}")
finally:
    print("File reading process finished.")
