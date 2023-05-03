def count_frequency(arr, n):
    freq = [0] * (n+1)
    for i in range(len(arr)):
        if arr[i] <= n:
            freq[arr[i]] += 1
    return freq[1:]

# Example Usage
arr = [2, 3, 2, 4, 5, 3, 5]
n = len(arr)
freq = count_frequency(arr, n)

print("Frequency of elements from 1 to N:")
for i in range(len(freq)):
    print(i+1, ":", freq[i])