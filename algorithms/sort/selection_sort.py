def selection_sort(array): 
    for i in range(len(array)): 
        min_index = i  

        for j in range(i, len(array)):
            if array[j] < array[min_index]: 
                min_index = j 

        array[i], array[min_index] = array[min_index], array[i]

    return array 

if __name__ == "__main__":
    pass 
