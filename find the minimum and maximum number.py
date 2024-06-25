# Minimum Function
def getMin(lst, n):
    res = lst[0] #lst is stand for list
    for i in range(1,n):
        res = min(res, lst[i])
    return res
# Maximum Function
def getMax(lst, n):
    res = lst[0]    #lst is stand for list
    for i in range(1,n):
        res = max(res, lst[i])
    return res
lst =[]
num = int(input("Please Enter the size of the array: "))
print("Please Enter array elements: ")
for i in range(num):
    res_num = int(input())
    lst.append(res_num)
len_list = len(lst)
print ("Minimum element of array:", getMin(lst, len_list))
print ("Maximum element of array:", getMax(lst, len_list))
