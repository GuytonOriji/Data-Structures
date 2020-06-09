
import sys
sys.path.append("../singly_linked_list/singly_linked_list.py")
#need help importing other files
# import LinkedList


# #LinkedList 
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.add_to_tail(value)

#     def dequeue(self):
#         if self.size:
#             self.size -= 1
#             return self.storage.remove_head() 



# #Array 
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def dequeue(self):
#         if self.storage:
#             self.size -= 1
#             removeval = self.storage[0]
#             self.storage = self.storage[1:]
#             return removeval
#         else:
#             return None






#Double stack implementation
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = Stack()
        self.remove_stack = Stack()

    def __str__(self):
        return str(self.storage.storage)
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.push(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            while self.storage.size > 1:
                self.remove_stack.push(self.storage.pop())
            headval = self.storage.pop()
            while self.remove_stack.size > 0:
                self.storage.push(self.remove_stack.pop())
            return headval