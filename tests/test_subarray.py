from subarray.subarray import subarray_average, maximum_sum_subarray
from subarray.subarray import smallest_subarray, longest_substr_with_distinct_chars
from subarray.subarray import longest_substring_no_repeat

def test_subarray_average():
    """find the average of all contiguous subarrays of size ‘K’ in a given array."""
    assert subarray_average(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]) == [2.2, 2.8, 2.4, 3.6, 2.8]


def test_maximum_sum_subarray():
    """Given an array find the subarray with the maximum sum of size k """
    assert maximum_sum_subarray(3, [2, 1, 5, 1, 3, 2]) == 9
    assert maximum_sum_subarray(2, [2, 3, 4, 1, 5]) == 7


def test_smallest_subarray():
    """Given an array find the smallest subarray that sums to a given target"""
    assert smallest_subarray(7, [2, 1, 5, 2, 3, 2]) == 2
    assert smallest_subarray(7, [2, 1, 5, 2, 8]) == 1
    assert smallest_subarray(8, [3, 4, 1, 1, 6]) == 3


def test_longest_substr_with_distinct_chars():
    """Given a substring find the longest substring with k distinct chars."""
    assert longest_substr_with_distinct_chars(2, "araaci") == 4
    assert longest_substr_with_distinct_chars(1, "araaci") == 2
    assert longest_substr_with_distinct_chars(3, "cbbebi") == 5

def test_longest_substr_no_repeat():
    """Given a string find the longest substring with no repeating character"""
    pass