from string import punctuation, whitespace


def is_palindrome(arg) -> bool:
    """
    Returns True if string is a palindrome, ignoring whitespace, punctuation and letter case.
    Argument will be converted to str.
    """

    lower_string = del_punc_and_spaces(str(arg)).lower()
    return lower_string == lower_string[::-1]


def del_punc_and_spaces(string: str) -> str:
    """ Return string without punctuation and whitespace characters. """

    translator = str.maketrans('', '', punctuation + whitespace)
    return string.translate(translator)



