def linear_search_v1(search_list, target_value):
    index = 0
    for value in search_list:
        if value == target_value:
            return index
        index += 1
    else:
            raise ValueError("{0} no esta en la lista".format(target_value))

def linear_search_v2(search_list, target_value):
    posiciones = []
    index = 0
    for value in search_list:
        if value == target_value:
            posiciones.append(index)
        index += 1

    if not posiciones:
        raise ValueError("{0} no esta en la lista".format(target_value))
    
    return posiciones

def linear_search_v3(search_list):
    max_value = 0
    for value in search_list:
        if value > max_value:
            max_value = value
    return max_value


lst1 = [1, 3, 7, 33, 24, 5, 0, 12, 23, 11]
print(linear_search_v1(lst1, 24))
lst2 = [1, 3, 7, 33, 24, 5, 0, 12, 23, 11, 24, 0, 21, 3, 2, -32, 24]
print(linear_search_v2(lst2, 24))
print(linear_search_v3(lst1))