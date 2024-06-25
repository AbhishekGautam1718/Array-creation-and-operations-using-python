def Counting_Even_Odd(lst, arr_size):
    even_count = 0
    odd_count = 0
# loop to read all the values in the array
    for itr in range(arr_size): # itr is iteration
# checking if a number is completely divisible by 2
        if(lst[itr]%2 == 0): 
            even_count +=1 # even_count is increased by 1
        else:
            odd_count +=1 # odd_count is increased by 1
    print("Number of even elements = ",even_count)
    print("Number of odd elements = ",odd_count)
lst = [] #lst variable of list
size = int(input("Enter the size of the array: "))
print("Enter array elements: ")
for itr in range(size):
    arr_num = int(input())

    lst.append(arr_num)
len_arr = len(lst)
print("Array is: ", lst)
# calling Funtion
Counting_Even_Odd(lst, len_arr)
