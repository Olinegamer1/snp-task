from tasks.task_01 import is_palindrome


def test_is_palindrome():
    # Test palindrome strings
    assert is_palindrome('racecar')
    assert is_palindrome('A man a plan a canal Panama!')
    assert is_palindrome('Was it a car or a cat I saw?')

    # Test non-palindrome strings
    assert not is_palindrome('hello world')
    assert not is_palindrome('Python')
    assert not is_palindrome('not a palindrome')

    # Test palindrome numbers
    assert is_palindrome(121)
    assert is_palindrome(1221)
    assert is_palindrome(12321)

    # Test non-palindrome numbers
    assert not is_palindrome(123)
    assert not is_palindrome(1234)

    # Test edge cases
    assert is_palindrome('')
    assert not is_palindrome(None)
    assert is_palindrome([])
    assert is_palindrome({})
    assert not is_palindrome(1.23)
    assert not is_palindrome(True)


if __name__ == '__main__':
    test_is_palindrome()
