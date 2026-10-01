def binary_search(sorted_list: list[int], target: int) -> int:
    """
    二分查找算法，在已排序列表中查找目标值的索引。

    如果找到目标值，返回其索引；否则返回 -1。
    """
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    # 测试用例
    test_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # 查找存在的元素
    print(f"在 {test_list} 中查找 7:")
    result = binary_search(test_list, 7)
    print(f"索引: {result}")

    # 查找不存在的元素
    print(f"\n在 {test_list} 中查找 6:")
    result = binary_search(test_list, 6)
    print(f"索引: {result}")

    # 查找边界元素
    print(f"\n在 {test_list} 中查找 1:")
    result = binary_search(test_list, 1)
    print(f"索引: {result}")

    print(f"\n在 {test_list} 中查找 19:")
    result = binary_search(test_list, 19)
    print(f"索引: {result}")
