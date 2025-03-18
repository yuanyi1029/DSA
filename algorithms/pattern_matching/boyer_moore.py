from z_algorithm import z_algorithm

def generate_bad_character_table(pattern):
    NUMBER_OF_CHARACTERS = 26 
    table = [None] * NUMBER_OF_CHARACTERS

    for i in range(len(pattern) - 1, -1, -1):
        character_position = ord(pattern[i]) - 97 

        if table[character_position] is None: 
            table[character_position] = [None] * len(pattern)

        table[character_position][i] = i

        current = i + 1 
        while current < len(pattern) and table[character_position][current] is None:
            table[character_position][current] = i 
            current += 1  

    return table  

def generate_good_suffix_array(pattern):
    array = [None] * (len(pattern) + 1)
    
    reversed_pattern = pattern[::-1]
    z_array = z_algorithm(reversed_pattern)[::-1]

    for i in range(len(pattern) - 1):
        j = len(pattern) - z_array[i]
        array[j] = i

    return array  

def generate_matched_prefix_array(pattern): 
    array = [None] * len(pattern)

    z_array = z_algorithm(pattern) 

    array[len(pattern) - 1] = z_array[len(pattern) - 1]
    for i in range(len(pattern) - 2, -1, -1):
        if z_array[i] + i == len(pattern): 
            array[i] = z_array[i]
        else: 
            array[i] = array[i + 1]
        
    array.append(0)    
    return array

def boyer_moore(sentence, pattern): 
    matched_array = []
    bad_character_table = generate_bad_character_table(pattern)
    good_suffix_array = generate_good_suffix_array(pattern) 
    matched_prefix_array = generate_matched_prefix_array(pattern)

    index = 0 
    bad_character_shift = 0
    good_suffix_shift = 0 
    start = None
    end = None 

    while (index + len(pattern)) <= len(sentence): 
        # Right to left scanning 
        current_sentence_index = index + len(pattern) - 1 
        current_pattern_index = len(pattern) - 1

        number_of_matches = 0
        while current_pattern_index >= 0: 
            if (good_suffix_shift >= bad_character_shift) and (end is not None and current_pattern_index == end): 
                current_sentence_index = current_sentence_index - (end - start + 1)
                current_pattern_index = start - 1 
                number_of_matches += end - start + 1
                continue
            if sentence[current_sentence_index] == pattern[current_pattern_index]: 
                number_of_matches += 1 
            else: 
                mismatch_character = sentence[current_sentence_index]
                break 

            current_sentence_index -= 1 
            current_pattern_index -= 1   

        start = None 
        end = None 
        if number_of_matches == len(pattern): 
            matched_array.append(index) 
            matched_prefix_index = matched_prefix_array[1]
            index += len(pattern) - matched_prefix_index
            start = 0
            end = matched_prefix_index - 1

        else: 
            # Check bad character shifts 
            bad_character_shift = 0

            bad_character_table_row = bad_character_table[ord(mismatch_character) - 97]
            if bad_character_table_row is None: 
                bad_character_shift = current_pattern_index + 1
            else: 
                bad_character_index = bad_character_table_row[current_pattern_index]
                if bad_character_index is None: 
                    bad_character_shift = current_pattern_index + 1 
                else: 
                    bad_character_shift = current_pattern_index - bad_character_index

            # Check good suffix shifts 
            good_suffix_shift = 0 

            good_suffix_index = good_suffix_array[current_pattern_index + 1]
            if good_suffix_index is not None: 
                good_suffix_shift = len(pattern) - good_suffix_index - 1
                if number_of_matches > 0: 
                    start = current_pattern_index - good_suffix_shift + 1  
                    end = start + number_of_matches - 1    
            else: 
                matched_prefix_index = matched_prefix_array[current_pattern_index + 1]
                good_suffix_shift = len(pattern) - matched_prefix_index 
                start = 0 
                end = matched_prefix_index - 1

            index += max(bad_character_shift, good_suffix_shift)

    return matched_array

if __name__ == "__main__": 
    pass
    # # [2, 7, 10, 13]
    # sentence = "ababcababcabcabc"  
    # pattern = "abc"               
    # print(boyer_moore(sentence, pattern))

    # # [0, 1, 2, 3]
    # sentence = "aaaaaa"  
    # pattern = "aaa"               
    # print(boyer_moore(sentence, pattern))
    
    # # [2, 8, 14]
    # sentence = "xxabcxxxabcxxxabc"  
    # pattern = "abc"               
    # print(boyer_moore(sentence, pattern))
    
    # # [0, 4, 8, 12]
    # sentence = "acgtacgtacgtacgt"  
    # pattern = "acgt"               
    # print(boyer_moore(sentence, pattern))
    
    # # [8]
    # sentence = "aabacabazabacabacabaa"  
    # pattern = "zabacabacaba"               
    # print(boyer_moore(sentence, pattern))
    
    # # Test
    # sentence = "xpbctbxabacbxtbpqa"  
    # pattern = "tbapxab"               
    # print(boyer_moore(sentence, pattern))
    
    # # [] Good Suffix Test 
    # sentence = "aabacabazabacabacabaa"  
    # pattern = "aabazabacaba"               
    # print(boyer_moore(sentence, pattern))
    
    # # [1, 5] Galil's Optimization Test 
    # sentence = "axyzaxyza"  
    # pattern = "xyz"               
    # print(boyer_moore(sentence, pattern))