def validate_non_empty(value):
    if value.strip() == "":
        return False

    return True


def validate_positive_number(value):
    try:
        number = float(value)

        if number > 0:
            return True

        return False

    except:
        return False


def validate_quantity(value):
    try:
        number = int(value)

        if number > 0:
            return True

        return False

    except:
        return False