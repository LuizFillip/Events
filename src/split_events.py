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
    
    return [round(p[-1], 2) for p in arr_splited 
            if len(p) != 0]

