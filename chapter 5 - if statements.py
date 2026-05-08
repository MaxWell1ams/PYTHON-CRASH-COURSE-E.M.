#first if statment example
#list
cars = ['Audi','bmw','Ferrari','VOLVO']
#for loop + if
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Conditional Tests
#deciding true or false

car = 'bmw'
print(car == 'bmw')
print(car == 'audi')

#using inequality (!=)

order = 'shoes'
if order != 't-shirt':
    print("Would you like to add a t-shirt?")

#just playing around if
admin_password = 'jeremy123'
#admin_password = 'jdf123'
if admin_password == 'jeremy123':
    print('login succeeded')
else:
    print('wrong password')

#and with != i can simplify my code
admin_password = 'jeremy123'
if admin_password != 'jeremy':
    print("Wrong password")

#but I usually need pass & login - here I can use 'and' to check if both conditions true
admin_password = 'jerald123'
admin_login = 'jerald'
if admin_password == 'jerald123' and admin_login == 'jerald':  #here I tried != - but it didnt worked or worked like 'or'
    print("you are logged in")
else:
    print("wrong login or pass")

#checking value in the list using in - browsing if smth exist in list simply mentioning
# this 'smth' in 'our list' to understand if its exist here
google = ['youtube','vertex','gemini']
print('vertex' in google)

#usin 'not'
ban_list = ['john','nesty','dasha']
user = 'john'
if user not in ban_list:
    print(user + ' you can join our gang if you wish')
    print(f"{user.title()}, you can join us if you envy us")
else:
    print(user.title() + ' wowowow, get out')

#using 'if' and '>'
age = 24
if age >= 25:
    print(f"You are: {age} y.o., you will be drafted soon ma boy!")
else:
    print(f"You little {age} years old shit, get out!")

#if - elif - else chain
age = 10
if age < 4:
    print('Your entry is free')
#if age < 5:
#    print('Your entry cost 1$') -- if I will use multiple if - it will run all of em 1 by 1
# so thats why we have elif as additional construct
elif age < 5:
    print('Your entry cost 1$')
elif age < 10:
    print('Your entry cost 4$')
else:
    print('Your entry fee 40$')

#making it more realistic to use
age = 11
if age < 4:
    price = 0
elif age < 5:
    price = 4
elif age < 10:
    price = 10
else:
    price = 24
print(f"Your admision costs {price} dollars")

#I can use if's if I want code to test each line (example above stops on 1st match)

my_pizza = ['pineapple','papperoni','dupa','cheese']
if 'pineapple' in my_pizza:
    print("\naddin pineapple")
if 'papperoni' in my_pizza:
    print("adding papperoni")
if 'mushrooms' in  my_pizza:
    print("adding mushrooms")
print("\nYour order is ready")

#example of how to make it smarter
for ingradient in my_pizza:
    if ingradient == 'dupa':
        print("sorry we out of dupa")
    else:
        print(f"\nadding {ingradient}")
print("\nYour order is ready")

#working with muiltiple lists
store_pizza = ['pineapple','papperoni','bbq']
for ingradient in my_pizza:
    if ingradient in store_pizza:
        print(f"adding {ingradient}")
    else:
        print(f"we don't have {ingradient}")
print(f"Please take your order")

#exercise - there not solved problem with lower upper case and title case matching
web_current_users = ['John','Max','Anna']
web_new_users = ['Jinny','Zxlecya','Max']
for user in web_new_users:
    if user in web_current_users:
        print(f"the username {user} is already taken")
    else:
        print(f"the username {user} is available to use")