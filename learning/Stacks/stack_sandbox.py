from Node import Node
import logging

# class Stack:
#     def __init__(self):
#         self.top_item = None
#     def peek(self):
#      return self.top_item.get_value()

class Stack:
    def __init__(self):
        self.top_item = None
        
    def push(self, value):
        item = Node(value)
        item.set_next_node(self.top_item)
        self.top_item = item

    def pop(self):
        item_to_remove = self.top_item
        self.top_item = self.top_item.get_next_node()
        return item_to_remove.get_value()

    def peek(self):
        return self.top_item.get_value()

# class Stack:
#     def __init__(self, limit = 1000, size = 0):
#         self.top_item = None
#         self.limit = limit
#         self.size = size
        
#     def push(self, value):
#         if self.has_space():
#             item = Node(value)
#             item.set_next_node(self.top_item)
#             self.top_item = item
#             self.size += 1
#         else:
#             logging.warning("La pila esta llena ¡No queda espacio!")

#     def pop(self):
#         if not self.is_empty():
#             item_to_remove = self.top_item
#             self.top_item = self.top_item.get_next_node()
#             self.size -= 1
#             return item_to_remove.get_value()
#         else:
#             logging.warning("La pila esta totalmente vacia!")

#     def peek(self):
#         if not self.is_empty():
#             return self.top_item.get_value()
#         else:
#             logging.warning("La pila esta totalmente vacia!")

#     def has_space(self):
#         return self.limit > self.size
    
#     def is_empty(self):
#         return self.size == 0