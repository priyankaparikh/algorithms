import math

def subarray_average(k, arr):
    """Given an array, find the average of all contiguous subarrays of size ‘K’ in it."""
    window_start = 0
    window_sum = 0
    out = []

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            out.append(window_sum/k)
            window_sum -= arr[window_start]
            window_start += 1

    return out


def maximum_sum_subarray(k, arr):
    """Given an array find the subarray with the maximum sum of size k."""
    window_start = 0
    max_sum = 0
    window_sum = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            if max_sum < window_sum:
                max_sum = window_sum
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum


def smallest_subarray(k, arr):
    """Given an array find the smallest subarray that sums up to match a target."""
    window_start = 0
    window_sum = 0
    min_size = math.inf

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]
        while window_sum >= k:
            min_size = min(min_size, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_size == math.inf:
        return 0
    return  min_size


def longest_substr_with_distinct_chars(k ,chars):
    """Given a substring find the longest substring with k distinct chars."""
    char_frq = {}
    j = 0
    max_len = 0

    for i in range(len(chars)):
        if chars[i] not in char_frq:
            char_frq[chars[i]] = 0
        char_frq[chars[i]] += 1

        while len(char_frq) > k:
            left = chars[j]
            if left in char_frq:
                char_frq[left] -= 1
            if char_frq[left] == 0:
                del(char_frq[left])
            j += 1
        max_len = max(max_len, i-j+1)

    return max_len

def fruits_in_basket(chars):
    """Given an array of characters where each character represents a fruit tree,
     you are given two baskets and your goal is to put maximum number of fruits in each basket.
    The only restriction is that each basket can have only one type of fruit."""
    char_frq = {}
    j = 0
    max_fruit = 0

    for i in range(len(chars)):
        if chars[i] not in char_frq:
            char_frq[chars[i]] = 0
        char_frq[chars[i]] += 1

        while len(char_frq) > 2:
            left = chars[j]
            if left in char_frq:
                char_frq[left] -= 1
            if char_frq[left] == 0:
                del (char_frq[left])
            j += 1

        max_fruit = max(max_fruit, i-j+1)

    return max_fruit


def longest_substring_no_repeat(str):
    """Given a string find the longest substring with no repeating character"""
    char_idx = {}
    j = 0
    max_count = 0

    for i in range(len(str)):
        if str[i] not in char_idx:
            char_idx[str[i]] = i
        else:
            char_idx[str[i]] = i
            j = i
        max_count = max(max_count, i-j+1)

    return max_count
