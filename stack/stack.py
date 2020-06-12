"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
""" 



import sys
sys.path.append("../singly_linked_list/")

from singly_linked_list import LinkedList

# #Array implementation
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if self.storage != []:
#             self.size -= 1
#             return self.storage.pop()
#         else:
#             return None

#LinkedList
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_tail()





# test = "57 57 -57 57"
# test = map(int, test.split())



# def run(test):

#   maxNum = max(test)
#   import copy

#   def sec():
#       temp = copy.copy(maxNum)
#       itt = 0
#       nextArr = []
#       for num in test:
#           if num < temp:
#               nextArr.append(num)
#           elif itt == len(test):
#               # third()
#               ans = max(nextArr)
#               break
#           itt = itt + 1
      
#       print(ans)

#   def first():
#       temp = copy.copy(maxNum)
#       temp = temp - 1

#       itt = 0
#       for num in temp:
#           if temp == num:
#               temp = num
#               break
#           elif itt == len(test):
#               sec()
#               break
#           itt = itt + 1
#       print(temp)
#   first()
 
# run(test)




if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

import copy

maxNum = max(arr)




# def third():
#     temp = copy.copy(maxNum)
#     temp = temp - 1
#     itt = 0
#     for num in arr:
#         if temp - 4 == num:
#             temp = num
#             break

#         elif itt == len(arr):
#             break
#         itt = itt + 1
#     print(temp)
    

def sec():
    temp = copy.copy(maxNum)
    itt = 0
    nextArr = []
    for num in arr:
        if num < temp:
            nextArr.append(num)
        # elif itt == len(arr):
        #     # third()
           
        #     break
        itt = itt + 1
    ans = max(nextArr)
    print(ans)

def first():
    temp = copy.copy(maxNum)
    temp = temp - 1

    itt = 0
    for num in arr:
        if temp == num:
            temp = num
            return print(temp)
            break
        elif itt == len(arr):
            sec()
            break
        itt = itt + 1
first()
 
