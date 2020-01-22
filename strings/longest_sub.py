def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    curr_count = 0
    max_count = 0
    curr_s = ""
    max_s = ""

    chars = {}

    for char in chars:
        if char not in chars:
            chars[char] = char
            curr_s = curr_s + char
            curr_count += 1
        elif char in chars and curr_count > max_count:
            chars = {}
            max_count = curr_count
            curr_count = 0
            max_s = curr_s
            curr_s = ''
            chars[char] = char

    return max(len(chars), max_count)
