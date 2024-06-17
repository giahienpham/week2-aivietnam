def max_sliding_window(num_list, k):
    if not num_list or k <= 0:
        return []
    n = len(num_list)
    if k > n:
        return [max(num_list)]
    max_list = []
    for i in range(n - k + 1):
        max_list.append(max(num_list[i:i + k]))
    return max_list

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_sliding_window(num_list, k))