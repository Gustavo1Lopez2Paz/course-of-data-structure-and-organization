# Escribe debajo el codigo de la clase DoublyLinkedList y sus respectivos metodos     
# Recuerda importar la clase Node en este script
import Node_sandbox as Ns

class DoublyLinkedList:
    def __init__(self, head_node = None, tail_node = None): # O(1)
        self.head_node = head_node  
        self.tail_node = tail_node

    def add_to_head(self, new_value): # O(1)
        new_head = Ns.Node(new_value)
        current_head = self.head_node  

        if current_head:
            current_head.set_prev_node(new_head)  
            new_head.set_next_node(current_head)   

        self.head_node = new_head

        if self.tail_node is None:
            self.tail_node = new_head

    def add_to_tail(self, new_value): # O(1)
        new_tail = Ns.Node(new_value)
        current_tail = self.tail_node

        if current_tail:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail 

        if self.head_node is None:
            self.head_node = new_tail

    def remove_tail(self): # O(1)
        removed_tail = self.tail_node

        if removed_tail is None:
            return None
            
        self.tail_node = removed_tail.get_prev_node()
        
        if self.tail_node is not None:
            self.tail_node.set_next_node(None)
        else:
            self.head_node = None

        return removed_tail.get_value()

    def remove_head(self): # O(1)
        removed_head = self.head_node

        if removed_head is None:
            return None
    
        self.head_node = removed_head.get_next_node()

        if self.head_node is not None:
            self.head_node.set_prev_node(None)
        else:
            self.tail_node = None 

        return removed_head.get_value()

    def remove_by_value(self, value_to_remove): # O(N)
        node_to_remove = None
        current_node = self.head_node
        while current_node is not None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break

            current_node = current_node.get_next_node()
        if node_to_remove is None:
            return None
        
        if node_to_remove == self.head_node:
            self.remove_head()
        elif node_to_remove == self.tail_node:
            self.remove_tail()
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)

        return node_to_remove
