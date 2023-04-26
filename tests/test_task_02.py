from tasks.task_02 import coincidence


def test_coincidence():
    # Test empty input
    assert coincidence() == []

    # Test with None as range_arr
    assert coincidence([1, 2, 3], None) == []

    # Test with None as arr
    assert coincidence(None, range(1, 4)) == []

    # Test with empty range
    assert coincidence([-1, 0, 1, 2, 4], range(0)) == []

    # Test with empty array
    assert coincidence([], range(1, 4)) == []

    # Test with no coincidences in the array
    assert coincidence([1, 2, 3], range(4, 7)) == []

    # Test with some coincidences in the array
    assert coincidence([1, 2, 3, 4, 5, 6], range(3, 5)) == [3, 4]

    # Test with decimal range
    assert coincidence([1, 2, 3.5, 4, 5], range(2, 5)) == [2, 3.5, 4]


if __name__ == '__main__':
    test_coincidence()
