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

    def __setitem__(self, index: int, value: int):
        self.check_index(index)
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

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

    def insert(self, index: int, value: int) -> bool:
        try:
            self.check_index(index)
            if len(self) >= self._capacity:
                return False
            else:
                return self._data.insert(index, value)
        except IndexError:
            return False

    def print_all(self):
        for item in self:
            print(item)


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
    # assert array.delete(4) is True

    array[3]
    array[3] = 1
    assert array[3] == 1

    print(sorted(array._data))
    array._data.sort()
    array.print_all()


def sorted_array_merge(array1: Array, array2: Array) -> Array:
    NotImplemented


if __name__ == "__main__":
    test_array()
