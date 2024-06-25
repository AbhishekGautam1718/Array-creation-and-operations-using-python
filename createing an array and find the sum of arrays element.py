#creating an array using list and total number of values in array
lst = [] #lst is list
size = int(input("Please Enter the size of the array: "))
print("Please Enter array elements: ")
for itr in range(size): # itr is iteration
    res_num = int(input())
    lst.append(res_num)
print("Array is :",lst)
print("Sum of total arrays number is:", sum(lst))
