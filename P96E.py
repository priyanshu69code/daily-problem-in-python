def find_least_index_sum(list1, list2):
    index_sum_dict = {}
    for i in range(len(list1)):
        if list1[i] in list2:
            j = list2.index(list1[i])
            index_sum_dict[list1[i]] = i + j
    min_index_sum = min(index_sum_dict.values())
    return [key for key in index_sum_dict if index_sum_dict[key] == min_index_sum]