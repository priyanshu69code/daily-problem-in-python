def isPerfectSquare(num: int) -> bool:
    if num < 2:
        return True

    low = 2
    high = num // 2

    while low <= high:
        mid = (low + high) // 2
        guess = mid * mid

        if guess == num:
            return True
        elif guess > num:
            high = mid - 1
        else:
            low = mid + 1

    return False