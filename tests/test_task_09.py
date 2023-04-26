from tasks.task_09 import connect_dicts


def test_connect_dicts():
    d1 = {'a': 13, 'b': 12, 'c': 5}
    d2 = {'b': 11, 'd': 9, 'e': 18}

    expected_result = {'b': 11, 'a': 13, 'e': 18}
    assert connect_dicts(d1, d2) == expected_result

    d1 = {'a': 3, 'b': 4, 'c': 5}
    d2 = {'b': 7, 'd': 1, 'e': 8}

    expected_result = {}
    assert connect_dicts(d1, d2) == expected_result

    d1 = {'a': 5, 'b': 2, 'c': 5}
    d2 = {}

    expected_result = {}
    assert connect_dicts(d1, d2) == expected_result

    d1 = {'a': 13, 'b': 2, 'c': 5}
    d2 = {'d': 1, 'e': 14}

    expected_result = {'a': 13, 'e': 14}
    assert connect_dicts(d1, d2) == expected_result

    d1 = {}
    d2 = {}

    expected_result = {}
    assert connect_dicts(d1, d2) == expected_result


if __name__ == '__main__':
    test_connect_dicts()
