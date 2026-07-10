#first dictionary - so I suppose dictionaries like a list, but using {} instead of []
# and we can store variables with values using : to store value
alien_0 = {'color': 'green', 'points': 7}
#and here I see that we can call separatelly variables using dicitionary name and ['variable-key']
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"Your reward is {new_points} points")
#to add key-variable I need simply write dictionary name and new key in [] with = value
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(f"I added new key-variables {alien_0}")
#example of how objects could be programmed on the screen using simple logic
print("\nExample:")
cat = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position: {cat['x_position']}")
#basically we assign position
#next logic is for predicting movements
if cat['speed'] == 'slow':
    x_increment = 1
elif cat['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
#so new position is old pos + number from new variable increment which we will get
# based on what type of speed we put
cat['x_position'] = cat['x_position'] + x_increment
print(f"New position: {cat['x_position']}")
# to delete value I can use del
del cat['speed']
print(cat)
cat['speed'] = 'fast'
print(cat)

#practicing get()
alien_1 = {'color': 'red', 'speed': 'ultra'}#,'points':88}
#good example - if we dont have point key in the dict it will text us No point values assigned
#I suppouse command get checks dictionary on key pairs and insted of error in this case 
#I can recieve custom message
#also I can simply use get('key-value-name') - and if its not exist I will recieve 'None'
point_value = alien_1.get('points') #, 'No point values assigned')
print(point_value)

#practicing for loop in dictionary
cat_2 = {
    'chanel':'sayamese',
    'boris':'pers',
    'jinx':'japanese',
    'yamamoto':'japanese'
}
for k, v in cat_2.items(): #items() iterates all the key-values in dictionaries
    print(f"\nKey: {k}")
    print(f"Value:{v}")
# if I need only keys I can use keys() command or values() for value
for nick in cat_2.keys():
    print(f"\nKey:{nick}")
#and I can do same without keys()
for nick in cat_2:
    print(f"\nKey:{nick}")
#to receive values in sorted from I can use sorted() function
for nick in sorted(cat_2):
    print(f"\nKey:{nick.upper()}")
#playing with values()
#book says that values could be repetative and to make us recieve unique
# value we can utilise set()
for nick in set(cat_2.values()):
    print(f"\nKey:{nick.lower()}")

#tough exercise but I nailed it
#I got confused about how my string will understand thta I want languages
#but I assume I assigned name as name than it check using name as key to find its value pair in fav_languages
fav_languages = {
    'Emma':'Python',
    'John':'c#'
}
poll_invitation = ['Emma','John','Patrick','Max']
for name in poll_invitation:
    if name in fav_languages:
        language = fav_languages[name].title()
        print(f"Thank you {name} for participation and choosing {language} ")
    else:
        print(f"Dear {name} its a reminder to take part in our poll")

###NESTING
# nesting dictionary to list
apple_0 = {'color':'green','rank':'5'}
apple_1 = {'color':'black','rank':'9'}
apple_2 = {'color':'white','rank':'10'}
# so I basically creating couple of dictionaries and can call them by name in the list
apples = [apple_0,apple_1,apple_2]
for appleE in apples:
    print(f"\n{appleE}")
print("\n")

#cool example of creating multiple dictionaries using range()
apples = []
#making 30
for apple_number in range(30):
    apple = {'color':'white','rank':'10','power':'100'}
    apples.append(apple)
#making changes on scale
for apple in apples[:3]:
    if apple['color'] == 'white':
        apple['color'] = 'pink'
        apple['rank'] = 8
        apple['power'] = 88
#showing
for apple in apples[:12]:
    print(apple)
print("\n")
#checking how many we have
print(f"Total number of apples: {len(apples)}\n")

#nesting list to dictionary
#creating a dictionary and inside of this dictionary I can create key which have
#variable as list and then utilise it
book = {'tickness':'hard',
        'chapters': ['chapter1', 'chapter2', 'chapter3']}
print(f"You ordered {book['tickness']}-tickness book which contains: ")
for chapter in book['chapters']:
    print(f"\t{chapter}")
#cool example of how to use lists in dictionaries
# I created dict then I created 2 keys and linked em to dict using items and for in
fav_cars = { 'Anna':['Bentley','Ferrari'],
            'Max':['McLaren','BMW','Corvette'],
            'Amina':['Audi','RangeRover']}
for name, cars in fav_cars.items():
    print(f"\n{name.upper()}'S favourite car is:")
    for car in cars:
        print(f"{car}")
print("\n")

##### a dictionary in dictionary
users = {'maxwell':{
    'first_name':'Max',
    'last_name':'Well',
    'geo':'Ukraine'
},
'annawell':{
    'first_name':'Anna',
    'last_name':'Well',
    'geo':'UK'
}}

for username,userinfo in users.items():
    print(f"Username:{username},")
    full_name = f"{userinfo['first_name']} {userinfo['last_name']}"
    geo = f"{userinfo['geo']}"
    print(f"{full_name}\n{geo}\n")