
def is_palindrome(s):
    chars = ''

    for char in s:
        if chars.isalnum():
            chars = chars + char

    return chars == chars[::-1]

def max_profit(lst):
    """https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"""""
    pass

def first_unique_char(s):
    """https://leetcode.com/problems/first-unique-character-in-a-string"""
    uniques = {}

    if s == '':
        return  -1

    for char in s:
        if char in uniques:
            uniques[char] += 1
        else:
            uniques[char] = 1

    for i in range(len(s)):
        if uniques[s[i]] == 1:
            return i

    return -1