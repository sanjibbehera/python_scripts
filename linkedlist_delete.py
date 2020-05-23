##############################################################
#### Arguments to be passed to the program like below:-
#### python linkedlist_delete.py 24 7 12 5 19 4 20 18 16
#### Addition of 2 adjacent nos to be 24, maximum nos to be passed is 7 and then delete from list whose sum is 24.
#### Output desired:-
#### Final Array: [12, 18, 16]
#### Removed Elements [5, 19, 4, 20]
##############################################################

import sys

my_list = []
new_arr = []
temp_arr = []
final_arr = []

def ReplaceElements(arr, n, m):
    if (n <= 1): 
        return
    for i in range(0, n-2):
        curr = int(arr[i])
        nxtItem = int(arr[i + 1])
        #print("New arr:", new_arr)
        #print("curr var:", curr)
        #print("nxt item var:", nxtItem)
        sum2nos = curr + nxtItem
        #print("addup", sum2nos)
        new_arr.append(curr)
        new_arr.append(nxtItem)
        if sum2nos == m:
            while curr in new_arr: 
                new_arr.remove(curr)
            while nxtItem in new_arr: 
                new_arr.remove(nxtItem)
            temp_arr.append(curr)
            temp_arr.append(nxtItem)
    new_arr.append(int(arr[n - 1]))

arg = sys.argv[1:]
for x in arg:
    my_list.append(x)

linked_list_len = len(my_list) - 2
max_params_to_pass = int(my_list[1])
addition_no = int(my_list[0])

if linked_list_len != max_params_to_pass:
    print("Wrong arguments passed.")
else:
    print(my_list, " validate_nos:", linked_list_len, " lentgh of arr:", len(my_list))

my_list.pop(0)
my_list.pop(0)
#print(my_list)

arr_len = len(my_list)
ReplaceElements(my_list, arr_len, addition_no)
final_arr = [item for item in new_arr if item not in temp_arr]
print('Final Array:', final_arr)
print('Removed Elements', temp_arr)
