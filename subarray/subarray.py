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
    """Given an array find the subarray with the maximum sum of size k """