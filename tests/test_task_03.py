from tasks.task_03 import max_odd


def test_max_odd():
    assert max_odd([1, 2, 3, 4, 5]) == 5
    assert max_odd([2, 4, 6, 8]) is None
    assert max_odd([1, 3, 5, 7]) == 7
    assert max_odd([0, 1, 2, 3]) == 3
    assert max_odd([-1, -2, -3, -4]) == -1
    assert max_odd([]) is None
    assert max_odd(['foo', 'bar', 'baz']) is None
    assert max_odd([1, 2, 'foo', 3, 'bar']) == 3
    assert max_odd([1.5, 3.5, 5.5, 4.4, 2.2]) == 5.5


if __name__ == '__main__':
    test_max_odd()
