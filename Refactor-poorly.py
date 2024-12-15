def process_numbers(numbers):
        
    result = []
    even_squares = [f"Square of {num} is {num * num}" for num in numbers if num % 2 == 0]
    result.extend(even_squares)
    max_num = max(numbers, default=None) 
    if max_num is not None:
        result.append(f"\nMax number is {max_num}")
    
    from collections import Counter
    count_dict = Counter(numbers)  
     result.append("Number counts:")
    result.extend([f"{num}: {count}" for num, count in count_dict.items()])
    
    return "\n".join(result)