from function_fortest import get_name_formated
print("q to quit")
while True:
    first = input("first name:")
    if first == 'q':
        break
    last = input("last name:")
    if last == 'q':
        break
    name = get_name_formated(first,last)
    print(f"{name}")