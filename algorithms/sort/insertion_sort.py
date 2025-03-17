def insertion_sort(array): 
    for i in range(1, len(array)): 
        sorted_index = i - 1
        item = array[i]
        
        while sorted_index >= 0 and item < array[sorted_index]:
            array[sorted_index + 1] = array[sorted_index] 
            sorted_index -= 1  

        array[sorted_index + 1] = item
 
    return array 

if __name__ == "__main__":
    pass 