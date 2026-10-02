"""
冒泡排序算法实现
"""


def bubble_sort(arr):
    """
    对列表进行冒泡排序

    参数:
        arr: 待排序的列表

    返回:
        排序后的列表
    """
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后i个元素已经排好序，所以内层循环可以跳过它们
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    # 测试示例
    test_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"排序前: {test_list}")
    sorted_list = bubble_sort(test_list.copy())
    print(f"排序后: {sorted_list}")

    # 测试已排序的列表
    test_list2 = [1, 2, 3, 4, 5]
    print(f"\n排序前: {test_list2}")
    sorted_list2 = bubble_sort(test_list2.copy())
    print(f"排序后: {sorted_list2}")

    # 测试包含负数的列表
    test_list3 = [-5, 10, -3, 8, 0, 2]
    print(f"\n排序前: {test_list3}")
    sorted_list3 = bubble_sort(test_list3.copy())
    print(f"排序后: {sorted_list3}")
