def mySqrt(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    res = x
    while res > x / res:
        res = (res + x / res) // 2
    return int(res)