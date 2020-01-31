
def is_palindrome(s):
    chars = ''

    for char in s:
        if chars.isalnum():
            chars = chars + char

    return chars == chars[::-1]


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


def move_zeroes(l):
    # keep track of where the zero was found
    zero_at = 0

    for i in range(len(l)):
        el = l[i]
        if el != 0:
            l[zero_at], l[i] = l[i], l[zero_at]
            zero_at += 1

    return l

def remove_elements(nums, val):
    count = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1

    return count

