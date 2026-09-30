def quick_sort(arr):
    """
    快速排序算法实现
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    # 简单测试
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"原始数组: {test_arr}")
    print(f"排序后: {quick_sort(test_arr)}")
