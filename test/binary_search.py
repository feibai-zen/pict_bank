def binary_search(sorted_list: list[int], target: int) -> int:
    """
    二分查找算法，在已排序列表中查找目标值的索引。

    如果找到目标值，返回其索引；否则返回 -1。
    """
    # 初始化左右指针，分别指向列表的起始和末尾位置
    left, right = 0, len(sorted_list) - 1

    # 当搜索区间有效时继续循环（left 不超过 right）
    while left <= right:
        # 计算中间位置，使用整除确保索引为整数
        mid = (left + right) // 2

        # 比较中间元素与目标值
        if sorted_list[mid] == target:
            # 找到目标值，直接返回其索引
            return mid
        elif sorted_list[mid] < target:
            # 中间元素小于目标值，目标在右半部分，移动左指针
            left = mid + 1
        else:
            # 中间元素大于目标值，目标在左半部分，移动右指针
            right = mid - 1

    # 搜索区间为空仍未找到，返回 -1 表示目标不存在
    return -1


if __name__ == "__main__":
    # 测试用例：已排序的整数列表
    test_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # 查找存在的元素（中间位置）
    print(f"在 {test_list} 中查找 7:")
    result = binary_search(test_list, 7)
    print(f"索引: {result}")

    # 查找不存在的元素（验证返回 -1）
    print()
    print(f"在 {test_list} 中查找 6:")
    result = binary_search(test_list, 6)
    print(f"索引: {result}")

    # 查找边界元素（第一个元素）
    print()
    print(f"在 {test_list} 中查找 1:")
    result = binary_search(test_list, 1)
    print(f"索引: {result}")

    # 查找边界元素（最后一个元素）
    print()
    print(f"在 {test_list} 中查找 19:")
    result = binary_search(test_list, 19)
    print(f"索引: {result}")
