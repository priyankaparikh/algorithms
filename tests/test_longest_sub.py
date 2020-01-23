from strings.longest_sub import lengthOfLongestSubstring

def test_length_of_Substring():
    sub1 = lengthOfLongestSubstring("abcabcbb")
    assert sub1 == 3
    sub2 = lengthOfLongestSubstring("pwwkew")
    assert sub2 == 3
    sub3 = lengthOfLongestSubstring("cdd")
    assert sub3 == 2
