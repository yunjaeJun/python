def pac_torial(n):
    if n == 0 or n ==1:
        return 1
    return n * pac_torial(n-1)