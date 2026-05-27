import module_borsh
import module_client_profile
order_active = True
while order_active:
    profile = input("What's your first and last name?:\n")
    user_profile = client_profile(profile)
    ingradients = input("Put your ingradient:\n")
    volume = input("What borsh volume you like?(S/M/L/XL):\n")
    borsh(volume, ingradients)
    print(f"Order for {user_profile} will be soon")
    next_order = input("Do you want order one more? (yes/no):\n ")
    if next_order == 'no':
        print("Bye, looking forward for your next visit!")
        order_active = False