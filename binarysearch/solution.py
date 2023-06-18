def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l, m, h = 0, len(nums) // 2, len(nums)
    while l < h:
        if nums[m] < target:
            l, m = m + 1, m + (h - m) // 2
        elif nums[m] > target:
            m, h = (m - l) // 2, m - 1
        else:
            return m
    return -1

if __name__ == "__main__":
    print(search(nums = [-1,0,3,5,9,12], target = 2))
    print(search(nums = [-1,0,3,5,9,12], target = 9))