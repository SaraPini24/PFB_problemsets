def isnumeric(input):
    """Return True if input can be converted to float, else False.

    This treats boolean values as numeric because float(True) == 1.0.
    None and non-numeric strings will return False.
    """
    try:
        float(input)
        return True
    except Exception:
        return False
