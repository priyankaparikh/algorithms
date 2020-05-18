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
    char_frequency = {}
    max_len = 0
    w_start = 0

    for w_end in range(len(chars)):
        right_char = chars[w_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        while len(char_frequency) > k:
            left_char = chars[w_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            w_start += 1
            # shrink the window
            # remember the maximum length so far
            max_len = max(max_len, w_end - w_start + 1)

    return max_len


def longest_substring_no_repeat(str):
    """Given a string find the longest substring with no repeating character"""
    pass
