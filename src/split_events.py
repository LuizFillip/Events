def split_array_into_three_equal_parts(arr):
    sorted_arr = sorted(arr)
    
    length = len(sorted_arr)
    
    if length < 3:
        raise ValueError("Array should have at least three elements.")
    
    # Calculate the indices to split the array into three parts
    part_size = length // 3
    index1 = part_size
    index2 = 2 * part_size
    
    # Split the sorted array into three parts based on magnitude
    part1 = sorted_arr[:index1]
    part2 = sorted_arr[index1:index2]
    part3 = sorted_arr[index2:]
    
    return part1, part2, part3




def split_in_equal_parts(
        arr, 
        parts = 3
        ):
    
    length = len(arr)
    part_size = length // parts
    
                
    part1 = arr[:part_size]
    part2 = arr[part_size:2*part_size]
    part3 = arr[2*part_size:]
    
    return part1, part2, part3
        
        

def limits_on_parts(df, parts = 2):
    
    arr = sorted(df.values)
    
    arr_splited = split_in_equal_parts(
            arr, 
            parts
            )
    
    arr_splited = arr_splited[:parts - 1]
    
    lst = [round(p[-1], 2) for p in arr_splited 
            if len(p) != 0]
    
    if len(lst) == 1:
        return lst[0]
    
    else:
        return lst

