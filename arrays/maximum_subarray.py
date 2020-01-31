"""leetcode problems with arrays"""

def trap_rainwater(heights):
    """https://leetcode.com/problems/trapping-rain-water/solution/"""
    total_area = 0
    sub_area = 0
    curr_max = heights[0]
    sub_area_heights = []

    for height in heights:
        if height < curr_max:
            sub_area += curr_max - height
            sub_area_heights.append(height)
        elif height >= curr_max:
            curr_max = height
            total_area += sub_area
            sub_area = 0
            sub_area_heights = [curr_max]

    if len(sub_area_heights) > 1:
        print(sub_area_heights)
        sub_area_heights = sub_area_heights[::-1]
        remaining_sub_area = trap_rainwater(sub_area_heights)
        print(remaining_sub_area)
        total_area += remaining_sub_area
        print(total_area)

    return total_area
