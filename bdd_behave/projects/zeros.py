def zeros(n):
    """Calculates the number of finite zeros in the factorial"""
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count
