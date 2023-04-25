def findPoisonedDuration(timeSeries, duration):
    poisoned_time = 0
    start = end = -1
    
    for t in timeSeries:
        if t > end:
            poisoned_time += end - start
            start = t
        end = t + duration
    
    poisoned_time += end - start
    
    return poisoned_time

>>> findPoisonedDuration([1, 4, 5, 7, 9], 2)
8
