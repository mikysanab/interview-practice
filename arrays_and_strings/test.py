def max_area(heights: list[int]) -> int:
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        area = (right - left) * min(heights[left], heights[right])
        best = max(best, area)
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return best


if __name__ == "__main__":
    assert max_area([3, 4, 1, 2, 2, 4, 1, 3, 2]) == 21
    assert max_area([1, 2, 1]) == 2
    print("All tests passed.")
