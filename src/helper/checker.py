import re


# Проверка на латиницу
def contains_latin(text):
    """
    :param text: Проверяемый текст
    :return: Выполняется проверка наличия латинских символов
    """
    return bool(re.search(r'[A-Za-z]', text))


# Проверка на кириллицу
def contains_cyrillic(text):
    """
    :param text: Проверяемый текст
    :return: Выполняется проверка наличия кириллических символов
    """
    return bool(re.search(r'[А-Яа-яЁё]', text))


def contains_latin_2(text: str) -> bool:
    # Check if the input contains Latin characters (A-Z, a-z)
    return any('A' <= char <= 'Z' or 'a' <= char <= 'z' for char in text)