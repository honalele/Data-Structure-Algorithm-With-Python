
def get_minimum_n(k):
    """get minimum value of n which makes S_n > k.

    Args:
        k (int): the threshod of S_n

    Returns:
        n (int): the index of S_n
    """    
    S_n = 1
    n = 0
    for i in range(100000):    
        S_n = S_n + 1/(i + 2)
        print(f"Given k is {k}, and n is {n}, and S_n is {S_n}")
        n  = i + 2
        if S_n <= k:
            print(f"Current value of n is {i+2}.")
        else:
            break
    return n

def main():
    try:
        k = int(input("Please input an integer k: "))
        n = get_minimum_n(k)
        print(f"Minimum value of n is {n}.")
    except TypeError as e:
        print(f"{k} is not integer, please input integer number, "+ e)
    
if __name__ == "__main__":
    main()
    