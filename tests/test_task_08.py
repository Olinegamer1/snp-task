from tasks.task_08 import multiply_numbers


def test_multiply_numbers():
    assert multiply_numbers() is None
    assert multiply_numbers('ss') is None
    assert multiply_numbers('1234') == 24
    assert multiply_numbers('sssdd34') == 12
    assert multiply_numbers(2.3) == 6
    assert multiply_numbers([5, 6, 4]) == 120
    assert multiply_numbers((1, 2, 3, 4, 5, 6, 7, 8, 9)) == 362880
    assert multiply_numbers({1, 2, 3, 4, 5, 6, 7, 8, 9}) == 362880


if __name__ == '__main__':
    test_multiply_numbers()