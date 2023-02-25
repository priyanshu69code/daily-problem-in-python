def climb_stairs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        f_minus_2 = 1
        f_minus_1 = 2
        for i in range(3, n+1):
            f = f_minus_1 + f_minus_2
            f_minus_2 = f_minus_1
            f_minus_1 = f
        return f


students = [['Harry', 37.21], ['Berry', 37.21], [
    'Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
students.sort()
print(students)
