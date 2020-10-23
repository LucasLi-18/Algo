# list实现一个数组类
# 实现一个动态扩容的数组
# 实现一个大小固定的数组，支持动态增删改操作
# 实现两个有序数组合并成一个有序数组
class Array:
    def __init__(self, capacity: int) -> None:
        self._data = []
        self._capacity = capacity

    def check_index(self, index: int):
        if index >= self._capacity or index < 0:
            raise IndexError

    def __getitem__(self, index: int) -> object:
        # random access
        self.check_index(index)
        return self._data[index]

    def __setitem__(self, index: int, value: object):
        self.check_index(index)
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def __repr__(self):
        return repr(self._data)

    def find(self, index: int) -> object:
        self.check_index(index)
        return self._data[index]

    def delete(self, index: int) -> bool:
        # why pop? not del or remove
        try:
            self.check_index(index)
            del self._data[index]
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: object) -> bool:
        try:
            self.check_index(index)
            if len(self) >= self._capacity:
                return False
            else:
                return self._data.insert(index, value)
        except IndexError:
            return False


def test_array():
    array = Array(5)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)

    # assert array.insert(0, 100) is False
    # assert len(array) == 5
    # assert array.find(4) == 9
    # assert array.delete(4) is True 会调用函数，所以会执行

    array[3]
    array[3] = 1
    assert array[3] == 1

    print(sorted(array._data))
    array._data.sort()
    array.print_all()

# 合并两个有序数组。方法一：双指针，从前向后比较，往后挪动插入


def sorted_array_merge(array1: Array, len1: int, array2: Array, len2: int) -> Array:
    # 创建指针分别指向数组1和数组2
    i, j = 0, 0
    while(j < len2):
        # 比较两个指针指向数的大小
        if array2[j] <= array1[i]:
            # 若数组2指针指向数小于等于数组1指针指向数
            # 则数组1全部数后移一位，头部插入数组2指针指向数
            for _ in range(len1-1, i-1, -1):
                array1[_+1] = array1[_]
            array1[i] = array2[j]
            # 数组1，数组2指针后移一位，数组1长度增加1
            j += 1
            i += 1
            len1 += 1
        else:
            # 若数组2指针指向数大于数组1指针指向数
            # 如果数组1指针指向最后一个数据，则将数组2拼接在数组1后面
            if i >= len1:
                for _ in range(j, len2):
                    array1[len1] = array2[_]
                    len1 += 1
                break
            # 否则数组1指针后移一位
            else:
                i += 1
    return array1

# 合并两个有序数组。方法二：双指针，从前向后比较，第三方数组存储


def sorted_array_merge2(array1: Array, len1: int, array2: Array, len2: int) -> Array:
    array = Array(len1 + len2)
    i, j, z = 0, 0, 0
    while(i < len1 and j < len2):
        if array1[i] < array2[j]:
            array.insert(z, array1[i])
            z += 1
            i += 1
        else:
            array.insert(z, array2[j])
            z += 1
            j += 1
    if i >= len1 and j < len2:
        for _ in range(j, len2):
            array.insert(z, array2[_])
            z += 1
    elif j >= len2 and i < len1:
        for _ in range(i, len1):
            array.insert(z, array1[_])
            z += 1
    return array

# 合并两个有序数组。方法二：双指针，从后向前比较


def sorted_array_merge3(array1: Array, len1: int, array2: Array, len2: int) -> Array:
    len = len1 + len2
    i, j, z = len1-1, len2-1, len-1
    while(i >= 0 and j >= 0):
        if array1[i] <= array2[j]:
            array1[z] = array2[j]
            j -= 1
            z -= 1
        else:
            array1[z] = array1[i]
            i -= 1
            z -= 1
    if (j >= 0):
        for _ in range(0, j+1):
            array1[_] = array2[_]
    return array1


if __name__ == "__main__":
    # test_array()

    '''  
    说明：
        初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
        你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
    示例:
        输入:
            nums1 = [1,2,3,0,0,0], m = 3
            nums2 = [2,5,6],       n = 3
        输出: [1,2,2,3,5,6] 
    '''

    nums1, m = [2, 3, 3, 9, 10, 0, 0, 0], 5
    nums2, n = [0, 1, 6], 3

    array1 = Array(m+n)
    array2 = Array(n)

    for i in range(m+n):
        array1.insert(i, nums1[i])

    for i in range(n):
        array2.insert(i, nums2[i])
    print(array1, array2)

    result1 = sorted_array_merge(array1, m, array2, n)
    result2 = sorted_array_merge2(array1, m, array2, n)
    result3 = sorted_array_merge3(array1, m, array2, n)
    print(result1, result2, result3, sep='\n')
