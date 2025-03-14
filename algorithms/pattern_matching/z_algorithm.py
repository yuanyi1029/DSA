def z_algorithm(sentence): 
    z_array = [0] * len(sentence) 
    z_array[0] = len(sentence) 

    left = 0 
    right = 0 
    index = 1 

    while index < len(sentence): 
        # Case 2: index is within a z-box
        if index >= left and index <= right: 
            # Case 2a: 
            if z_array[index - left] < right - index + 1:  
                z_array[index] = z_array[index - left]

            # Case 2b: 
            elif z_array[index - left] > right - index + 1:  
                z_array[index] = right - index + 1 

            # Case 2c: 
            else:
                start = right - index + 2 
                current = right + 1   
                matches = right - index + 1

                while sentence[start] == sentence[current]: 
                    start += 1 
                    current += 1 
                    matches += 1 

                z_array[index] = matches

                if matches > 0: 
                    left = index
                    right = current - 1

        # Case 1: index is not within a z-box
        else: 
            start = 0 
            current = index
            matches = 0 

            while sentence[start] == sentence[current]: 
                start += 1 
                current += 1
                matches += 1  

            z_array[index] = matches

            if matches > 0: 
                left = index 
                right = current - 1 
        
        index += 1 

    return z_array

if __name__ == "__main__":
    word = "aabxaabxcaabxaabxay"
    print(z_algorithm(word))
