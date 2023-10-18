import os

def create_file(filename):
    with open(filename, 'w') as file:
        print(f"File '{filename}' has been created.")

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' has been deleted.")
    else:
        print(f"File '{filename}' does not exist.")

def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content + '\n')
        print(f"Content appended to '{filename}'.")

def override_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
        print(f"File '{filename}' has been overridden with new content.")

while True:
    print("Choose an option:")
    print("1. Create a file")
    print("2. Delete a file")
    print("3. Append to a file")
    print("4. Override a file")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        filename = input("Enter the filename: ")
        create_file(filename)
    elif choice == '2':
        filename = input("Enter the filename to delete: ")
        delete_file(filename)
    elif choice == '3':
        filename = input("Enter the filename to append to: ")
        content = input("Enter the content to append: ")
        append_to_file(filename, content)
    elif choice == '4':
        filename = input("Enter the filename to override: ")
        content = input("Enter the new content to write: ")
        override_file(filename, content)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4/5).")
