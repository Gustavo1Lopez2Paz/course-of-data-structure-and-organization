class Node:
    def __init__(self, value, next_node = None): # O(1)
        self.value = value
        self.next_node = next_node

    def get_value(self): # O(1)
        return self.value

    def get_next_node(self): # O(1)
        return self.next_node
    
    def set_next_node(self, next_node): # O(1)
        if next_node != None and not isinstance(next_node, dict) and not isinstance(next_node, Node):
            raise TypeError("next_node must be of type Node, dict, or None")
        else:
            self.next_node = next_node