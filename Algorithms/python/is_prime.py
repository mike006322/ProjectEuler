def is_prime(n):
    """
    Returns boolean whether n is prime
    """
    if n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i <= n**.5:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


if __name__ == '__main__':
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(17)
    assert is_prime(7)
    assert is_prime(31)
    assert not is_prime(4)
    assert not is_prime(18)
    assert not is_prime(32)
