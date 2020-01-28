from strings.is_palindrome import is_palindrome, max_profit, first_unique_char

def test_palindrome():
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"

    assert is_palindrome(s1)
    assert is_palindrome(s2)

# def test_max_profit():
#     assert max_profit([7,1,5,3,6,4]) == 5
#     assert max_profit([7, 6, 4, 3, 1])==0
#

def test_first_unique_char():
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2