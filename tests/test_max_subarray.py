from arrays.maximum_subarray import trap_rainwater

def test_trap_rainwater():
    assert trap_rainwater([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap_rainwater([4,2,3]) == 1