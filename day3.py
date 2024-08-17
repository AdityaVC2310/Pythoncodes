# user input
C = int(input("Enter C:"))
D = int(input("Enter D:"))

temp = C #C is assingned to temp
C = D    # C is assinged to C
D = temp #temp is assinged to D
print('After swapping, C=',C,'and D=',D)
