from tasks.task_07 import combine_anagrams


def test_combine_anagrams():
    words = ['eat', 'tEa', 'tan', 'aTe', 'nat', 'bat']
    expected_output = [['eat', 'tEa', 'aTe'], ['tan', 'nat'], ['bat']]
    assert combine_anagrams(words) == expected_output

    words = ['race', 'Care', 'acre', 'dog', 'god']
    expected_output = [['race', 'Care', 'acre'], ['dog', 'god']]
    assert combine_anagrams(words) == expected_output

    words = ['Abcdefg', 'gfEdcba', 'abc', 'cba', 'defg', 'gfed']
    expected_output = [['Abcdefg', 'gfEdcba'], ['abc', 'cba'], ['defg', 'gfed']]
    assert combine_anagrams(words) == expected_output

    words = []
    expected_output = []
    assert combine_anagrams(words) == expected_output

    words = ['hello', 'worlD']
    expected_output = [['hello'], ['worlD']]
    assert combine_anagrams(words) == expected_output


if __name__ == '__main__':
    test_combine_anagrams()
