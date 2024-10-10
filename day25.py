from csv import writer

data_list = []
data_list.append(['Name', 'Age', 'Gender'])

for i in range(5):
    name = input('Enter Name: ')
    age = input('Enter Age: ')
    gender = input('Enter Gender: ')
    data_list.append([name, age, gender])
    print()

try:
    with open('MyRecords.csv', 'w', newline='') as file:
        csv_writer = writer(file)
        csv_writer.writerows(data_list)
        print("Data written to CSV file successfully!")
        
except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print(f"An error occurred: {e}")
