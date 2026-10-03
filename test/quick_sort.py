def quick_sort(arr):
    """
    快速排序算法实现。

    采用分治策略：
    1. 选择一个基准元素（pivot）
    2. 将数组分为小于、等于和大于基准的三部分
    3. 递归地对左右两部分进行排序
    4. 合并结果
    """
    # 基准情况：数组长度小于等于1时，无需排序，直接返回
    if len(arr) <= 1:
        return arr

    # 选择中间位置的元素作为基准值
    pivot = arr[len(arr) // 2]

    # 将数组分为三部分：
    # left - 所有小于基准值的元素
    left = [x for x in arr if x < pivot]
    # middle - 所有等于基准值的元素（包含基准值本身）
    middle = [x for x in arr if x == pivot]
    # right - 所有大于基准值的元素
    right = [x for x in arr if x > pivot]

    # 递归排序左右两部分，然后合并结果
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    # 测试用例：未排序的整数数组
    test_arr = [64, 34, 25, 12, 22, 11, 90]

    # 输出原始数组
    print(f"原始数组: {test_arr}")
    # 输出排序后的数组
    print(f"排序后: {quick_sort(test_arr)}")
