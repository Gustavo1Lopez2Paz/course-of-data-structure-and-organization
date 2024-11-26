def binary_search(lst, element):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == element:
            return mid
        elif lst[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    else:
        return "Valor no encontrado"



