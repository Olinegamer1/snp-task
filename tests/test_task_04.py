from tasks.task_04 import sort_list


def test_sort_list():
    arr = [3, 1, 4, 2]
    expected_result = [3, 4, 1, 2, 1]
    result = sort_list(arr)
    assert result == expected_result, f'Expected {expected_result}, but got {result}'

    arr = []
    expected_result = []
    result = sort_list(arr)
    assert result == expected_result, f'Expected {expected_result}, but got {result}'

    arr = [3, 3, 3, 3]
    expected_result = [3, 3, 3, 3, 3]
    result = sort_list(arr)
    assert result == expected_result, f'Expected {expected_result}, but got {result}'

    arr = [-5, 0, 5]
    expected_result = [5, 0, -5, -5]
    result = sort_list(arr)
    assert result == expected_result, f'Expected {expected_result}, but got {result}'

    arr = [2, 4, 6, 8]
    expected_result = [8, 4, 6, 2, 2]
    result = sort_list(arr)
    assert result == expected_result, f'Expected {expected_result}, but got {result}'

    arr = [1]
    expected_result = [1, 1]
    result = sort_list(arr)
    assert result == expected_result, f'Expected {expected_result}, but got {result}'

    arr = [1, 2, 1, 3]
    expected_result = [3, 2, 3, 1, 1]
    result = sort_list(arr)
    assert result == expected_result, f'Expected {expected_result}, but got {result}'


if __name__ == '__main__':
    test_sort_list()
