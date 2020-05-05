from subarray.subarray import subarray_average

def test_subarray_average():
    """find the average of all contiguous subarrays of size ‘K’ in a given array."""
    assert subarray_average(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]) == [2.2, 2.8, 2.4, 3.6, 2.8]