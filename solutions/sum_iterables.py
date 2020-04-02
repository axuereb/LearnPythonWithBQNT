def sum_numbers(iterable, start=0):
    """
       Return the sum of a 'start' value (default: 0) plus an iterable of numbers

        When the iterable is empty, return the start value.
        This function is intended specifically for use with numeric values and may
        reject non-numeric types.
    """
    result = start
    
    for number in iterable:
        result += number
        
    return result

print(sum_numbers(range(0,10), start=100)) # 145 
print(sum_numbers([10,20,30])) # 60 