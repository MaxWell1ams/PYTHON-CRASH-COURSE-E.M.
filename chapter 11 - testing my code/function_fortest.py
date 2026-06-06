def get_name_formated(first,last,middle=''):
    """gen formated name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
