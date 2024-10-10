def handle_file():
    try:
        
        with open("MyDataFile.txt", 'r') as file:
            print(f"Contents of MyDataFile.txt:")
            print(file.read())
    except FileNotFoundError:
        
        print(f"MyDataFile.txt not found. Creating the file and writing default content.")
        with open("MyDataFile.txt", 'w') as file:
            default_content = "This is the default content.\n"
            file.write(default_content)

def merge_files(file1, file2, merged_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
           
            content1 = f1.read()
            content2 = f2.read()

        
        with open(merged_file, 'w') as mf:
            mf.write(content1)
            mf.write(content2)
        
        print(f"Files {file1} and {file2} successfully merged into {merged_file}")
    
    except FileNotFoundError as e:
        print(f"Error: {e}. One of the files does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# File handling with exception handling
handle_file()

# Merging two files
file1 = "file1.rtf"
file2 = "file2.rtf"
merged_file = "merged_file.txt"

merge_files(file1, file2, merged_file)
