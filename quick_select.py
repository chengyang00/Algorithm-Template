def quick_select(nums: list, k:int):
    """
    选择nums数组中的第k（0 based）小的数
    """
    pivot = nums[-1]
    i = 0
    n = len(nums) - 1
    for j in range(n):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[-1] = nums[-1], nums[i]
    if i < k:
        return quick_select(nums[i+1:], k - i - 1)
    elif i > k:
        return quick_select(nums[:i], k)
    else:
        return pivot
