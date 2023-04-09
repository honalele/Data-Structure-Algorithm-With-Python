def get_daffodil_number():
    """AI is creating summary for get_daffodil_number

    Returns:
        [list]: daffodil_numbers
    """    
    daffodil_numbers = []
    i = 100
    while i < 1000:
        # Hundreds digit
        a = int(i/100)
        # Tens digit, here // get the integer number
        b = int(i%100//10)
        # Last digits, % is get remainder
        c = i%10

        if (a**3 + b**3 + c**3) == i:
            daffodil_numbers.append(i)
            print(f"a: {a}, b: {b}, c: {c}, and the daffodil number i: {i}")
        
        i += 1    
    return daffodil_numbers
    
    
if __name__ == "__main__":
    daffodil_numbers = get_daffodil_number()
    

    
    

