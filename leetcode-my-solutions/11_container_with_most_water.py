"""
Author: Sikder Tahsin Al Amin
Problem: Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

def maxArea(height):
    max_area = 0
    for i in range(0,len(height)-1):
        for j in range(i+1,len(height)):
            area = abs((j-i)* min(height[i],height[j]))
            if area>max_area:
                max_area = area
    return max_area

def maxArea2(height):
    max_area = 0
    left, right = 0, len(height)-1
    while left<right:
        area = abs((left-right)*min(height[left],height[right]))
        if area>max_area:
            max_area = area
        if height[left]<height[right]:
            left = left +1 
        else:
            right = right - 1
    return max_area
