def client_profile(first, last, **user_info):  #kwargs (for dictionaries)
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info