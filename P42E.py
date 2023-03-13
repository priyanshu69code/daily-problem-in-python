def summary_ranges(nums):
    ranges = []
    if not nums:
        return ranges

    start = end = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == end + 1:
            end = nums[i]
        else:
            ranges.append((start, end))
            start = end = nums[i]
    ranges.append((start, end))

    formatted_ranges = []
    for start, end in ranges:
        if start == end:
            formatted_ranges.append(str(start))
        else:
            formatted_ranges.append(str(start) + "->" + str(end))

    return formatted_ranges
