from strings.is_palindrome import is_palindrome, first_unique_char, move_zeroes
from strings.is_palindrome import remove_elements


def test_palindrome():
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"

    assert is_palindrome(s1)
    assert is_palindrome(s2)


def test_first_unique_char():
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2


def test_move_zeros():
    assert move_zeroes([0,1,0,3,12]) == [1,3,12,0,0]
    assert move_zeroes([4, 1, 0, 3, 12, 0]) == [4, 1, 3, 12, 0, 0]


def test_remove_elements():
    assert remove_elements([3,2,2,3], val = 3) == 2
    assert remove_elements([0,1,2,2,3,0,4,2], val = 2,) == 5