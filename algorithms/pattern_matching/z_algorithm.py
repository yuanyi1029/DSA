def z_algorithm(sentence): 
    z_array = [0] * len(sentence) 
    z_array[0] = len(sentence) 

    left = 0 
    right = 0 
    index = 1 

    while index < len(sentence): 
        # Case 2: index is within a z-box
        # Resolve: Resolution is split into 3 cases 
        if index >= left and index <= right: 

            # Case 2a: corresponding z-value is within z-box
            # Resolve: use the corresponding z-value 
            if z_array[index - left] < right - index + 1:  
                z_array[index] = z_array[index - left]

            # Case 2b: corresponding z-value excludes z-box
            # Resolve: use the remaining space between index and right as z-value
            elif z_array[index - left] > right - index + 1:  
                z_array[index] = right - index + 1 

            # Case 2c: corresponding z-value is equal to the z-box
            # Resolve: perform manual comparison from right onwards 
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
        # Resolve: perform manual comparison 
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
