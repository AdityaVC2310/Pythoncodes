def access_element(my_list, index):
    try:
       
        element = my_list[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
       
        print(f"Index {index} is out of range for the list.")

my_list = [10, 20, 30, 40, 50]
access_element(my_list, 2)  
access_element(my_list, 5)
