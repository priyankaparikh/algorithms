from subarray.subarray import subarray_average, maximum_sum_subarray


def test_subarray_average():
    """find the average of all contiguous subarrays of size ‘K’ in a given array."""
    assert subarray_average(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]) == [2.2, 2.8, 2.4, 3.6, 2.8]


def test_maximum_sum_subarray():
    """Given an array find the subarray with the maximum sum of size k """
    assert maximum_sum_subarray(3, [2, 1, 5, 1, 3, 2]) == 9
    assert maximum_sum_subarray(2, [2, 3, 4, 1, 5]) == 7

