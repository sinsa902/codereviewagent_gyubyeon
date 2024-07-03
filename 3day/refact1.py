def split_and_sum(text: str):
    if __is_not_str(text):
        return 0
    if not __all_digit(text):
        return 0

    return __get_sum(text)


def __get_sum(text):
    result = 0
    values = text.split("-")
    for i in range(len(values)):
        result += int(values[i])
    return result


def __all_digit(text):
    values = text.split("-")
    for i in range(len(values)):
        if not values[i].isdigit():
            return False
    return True


def __is_not_str(text):
    return (not isinstance(text, str)) or len(text) == 0
