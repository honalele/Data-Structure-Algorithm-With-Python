
def get_minimum_n(k):
    S_n = 1
    n = 0
    for i in range(1000):    
        S_n = S_n + 1/(i + 2)
        if S_n > k:
            print(f"Minimum value of n is {i+2}.")
            n  = i + 2
            break
    return i

def main():
    error_count = 0
    while error_count < 3:
        k = int(input("Please input an integer k: "))
        if isinstance(k, int):
            n = get_minimum_n(k)
            break
        else: 
            error_count += 1
            print(f"{k} is not integer, please input integer number")
    
if __name__ == "__main__":
    main()
    