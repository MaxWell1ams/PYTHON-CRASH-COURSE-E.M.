def client_profile(first, last, **user_info):  #kwargs (for dictionaries)
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

def borsh(volume, *toppings): #if I will add regular parameter for regular argument
    # the arbitrary pararameter should be placed last like def sss(sdds, sdds, *dssdd)
    # so it's for LISTS - arbitrary with 1 asteriks
    print(f"Making a {volume} borsh with: ")
    for topping in toppings:
        print(topping)