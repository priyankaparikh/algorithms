from arrays.maximum_subarray import trap_rainwater
from arrays.merge_sorted import word_puzzles

def test_trap_rainwater():
    assert trap_rainwater([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap_rainwater([4,2,3]) == 1

def test_word_puzzles():
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]

    assert word_puzzles(words, puzzles) == [1,1,3,2,4,0]
