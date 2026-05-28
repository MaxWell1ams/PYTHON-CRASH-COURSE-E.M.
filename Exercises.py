from modules import *
order_active = True
while order_active:
    profile = input("What's your first and last name?:\n").split() #utilised split to have 2 values when writing input
    user_profile = client_profile(*profile) #so I called it to feed 1 and last name cuz without * it would not work
    #and when I use import program behave differently - I need do additional logic
    ingradients = input("Put your ingradient:\n")
    volume = input("What borsh volume you like?(S/M/L/XL):\n")
    borsh(volume, ingradients)
    print(f"Order for {user_profile} will be soon")
    next_order = input("Do you want order one more? (yes/no):\n ")
    if next_order == 'no':
        print("Bye, looking forward for your next visit!")
        order_active = False