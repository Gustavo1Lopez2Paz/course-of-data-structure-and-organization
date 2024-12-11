# Agrega el codigo de la funcion nth_last_element() debajo
from Node_Sandbox import Node

def nth_last_element(linked_list, n):
    lead = linked_list.get_head_node()
    follow = linked_list.get_head_node()

    # Mover el puntero líder n posiciones adelante
    for _ in range(n):
        if lead is None:  # Si n es mayor que la longitud de la lista
            return None
        lead = lead.get_next_node()

    # Mover ambos punteros hasta que el puntero líder llegue al final
    while lead:
        lead = lead.get_next_node()
        follow = follow.get_next_node()

    return follow  # El puntero de seguimiento apunta al n-ésimo elemento desde el final