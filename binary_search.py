"""
Задача: реализовать алгоритм бинарного поиска в простом массиве
Входные данные: коллекция, отсортированная по возрастанию, и любое значение из этой коллекции
Возвращаемые данные: индекс значения, которое было дано на вход
"""
from typing import Any


# implementation
def binary_search(data: list[Any], target_value: Any) -> int | None:
    left, right = 0, len(data) - 1

    while left <= right:
        mid_index = (left + right) // 2

        if target_value == data[mid_index]:
            return mid_index

        if target_value < data[mid_index]:
            right = mid_index - 1
        else:
            left = mid_index + 1

    return None


# ------------------------ TESTS -----------------------
tests_data = {
    ((-5, 1, 3, 6), 3): 2,
    ((-1, 0, 3, 5, 9, 12), 2): None,
    ((-1, 0, 3, 5, 9, 12), 12): 5,
    ((5, ), 1): None,
    ((6, ), 6): 0,
}


def main():
    try:
        for test_data in tests_data:
            result = tests_data[test_data]
            assert binary_search(test_data[0], test_data[1]) == result
    except AssertionError:
        print(f'tests failed on {test_data}')


if __name__ == '__main__':
    main()
