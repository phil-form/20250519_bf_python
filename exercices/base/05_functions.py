def search_v1(arr, searched_elem):
    for val in arr:
        if(val == searched_elem):
            print("Found")

def search_v2(arr, searhed_elem):
    length = len(arr)
    found = -1
    for i in range(length):
        if(arr[i] == searhed_elem):
            found = i
        
    return found

def search_v3(arr, searhed_elem):
    length = len(arr)
    for i in range(length):
        if(arr[i] == searhed_elem):
            return i
        
    return -1

def search_v4(arr, searhed_elem):
    for index, val in enumerate(arr):
        if(val == searhed_elem):
            return index
        
    return -1

tab = [5, 13, 44, 23, 12, 55]
search_v4(tab, 13)