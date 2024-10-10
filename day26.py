def clean_data(data_list):
    valid_data = []
    invalid_data = []
    for item in data_list:
        # Check if the item is an integer
        if isinstance(item, int):
            valid_data.append(item)
        # To Check if the item is a string that can be converted to an integer
        elif isinstance(item, str):
            try:
                
                number = int(item)
                valid_data.append(number)
            except ValueError:
                # If conversion fails
                invalid_data.append(item)
        else:
            invalid_data.append(item)
    # invalid entries
    if invalid_data:
        print("Invalid data found and removed:", invalid_data)
    return valid_data
# Function to get user input
def get_user_input():
    user_input = input("Enter a list of values separated by commas: ")
    data_list = [item.strip() for item in user_input.split(',')]

    for i in range(len(data_list)):
        if data_list[i].lower() == 'none':
            data_list[i] = None
        elif data_list[i].isdigit():
            data_list[i] = int(data_list[i])
    return data_list
    #user 
data = get_user_input()
cleaned_data = clean_data(data)
print("Cleaned Data:", cleaned_data)

data = get_user_input()
cleaned_data=clean_data(data)

