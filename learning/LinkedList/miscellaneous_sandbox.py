# Agrega el codigo de la funcion nth_last_element() debajo
from LinkedList_sandbox import LinkedList

def nth_last_element(ll, n=None):
    
    ll = LinkedList()

    if n is None or n <= 0:
        return None
    
    current_node = ll.get_head_node()
    length = 0
    while current_node is not None:
        length += 1
        current_node = current_node.get_next_node()

    if n > length:
        return None

    position_from_start = length - n

    current_node = ll.get_head_node()
    for _ in range(position_from_start):
        current_node = current_node.get_next_node()

    return current_node.get_value()

linkedlist = LinkedList()
linkedlist.insert_beginning(1)
linkedlist.insert_beginning(2)
linkedlist.insert_beginning(3)
linkedlist.insert_beginning(4)
linkedlist.insert_beginning(5)

print("Lista enlazada:")
print(linkedlist.stringify_list())

penultimo = nth_last_element(linkedlist, 2)
print(f"El penúltimo nodo es: {penultimo}")
