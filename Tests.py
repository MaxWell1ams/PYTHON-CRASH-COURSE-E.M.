def borsh(volume, *toppings): #if I will add regular parameter for regular argument
    # the arbitrary pararameter should be placed last like def sss(sdds, sdds, *dssdd)
    # so it's for LISTS - arbitrary with 1 asteriks
    print(f"Making a {volume} borsh with: ")
    for topping in toppings:
        print(topping)
def client_profile(first, last, **user_info):  #kwargs (for dictionaries)
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
order_active = True
while order_active:
    profile = input("What's your first name?:\n")
    profile2 = input("What's your last name?:\n")
    user_profile = client_profile(profile,profile2)
    ingradients = input("Put your ingradient:\n")
    volume = input("What borsh volume you like?(S/M/L/XL):\n")
    borsh(volume, ingradients)
    print(f"Order for {user_profile} will be soon")
    next_order = input("Do you want order one more? (yes/no):\n ")
    if next_order == 'no':
        print("Bye, looking forward for your next visit!")
        order_active = False