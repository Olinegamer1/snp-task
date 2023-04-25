from string import punctuation, whitespace


def is_palindrome(arg) -> bool:
    """
    Return True if string is a palindrome, ignoring whitespace, punctuation and letter case.
    Argument will be converted to str if it's a number (float, int).
    If argument not are str or number, return False.
    """

    if not isinstance(arg, (str, int, float)):
        return False

    string = str(arg)
    lower_string = del_punc_and_spaces(string).lower()

    return lower_string == lower_string[::-1]


def del_punc_and_spaces(string: str) -> str:
    """ Return string without punctuation and whitespace characters. """

    translator = str.maketrans('', '', punctuation + whitespace)
    return string.translate(translator)



