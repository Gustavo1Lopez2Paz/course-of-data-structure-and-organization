def linear_search_v1(search_list, target_value): # O(N)
    index = 0
    for value in search_list:
        if value == target_value:
            return index
        index += 1
    else:
            raise ValueError("{0} no esta en la lista".format(target_value))

def linear_search_v2(search_list, target_value): # O(N)
    posiciones = []
    index = 0
    for value in search_list:
        if value == target_value:
            posiciones.append(index)
        index += 1

    if not posiciones:
        raise ValueError("{0} no esta en la lista".format(target_value))
    
    return posiciones

def linear_search_v3(search_list): # O(N)
    max_value = 0
    for value in search_list:
        if value > max_value:
            max_value = value
    return max_value