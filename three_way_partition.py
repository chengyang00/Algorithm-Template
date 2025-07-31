def three_way_partition(arr, pivot):
    """
    对列表 arr 进行原地 3-way partition，使得：
      - arr[0..low-1]   < pivot
      - arr[low..mid-1] == pivot
      - arr[high+1..end] > pivot
    最终返回 (low, high) 两个索引，表示等于区域的左右边界。
    """
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] < pivot:
            # Case 1: 小于 pivot，交换到最左边的 < 区
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] > pivot:
            # Case 3: 大于 pivot，交换到最右边的 > 区
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            # 注意：mid 不变，需要重新检查交换过来的元素
        else:
            # Case 2: 等于 pivot，直接进入下一个元素
            mid += 1

    return low, high
