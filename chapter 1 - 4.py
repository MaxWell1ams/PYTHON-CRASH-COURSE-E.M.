message = "Simple Messages"
print(message)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
#.title, .lower or upper usefull for formatting and f- is ormating ops which unifies strings
message = f"Hello, {full_name.title()}!"
print(message)

#\t tab, \n new line, removeprefix for removing text, strip, stripl,r for removing spaces 
# (or remove any letter from text - if choose letter r - all r's will be removed)
print("\tLanguages:\n\t\tPy\n\t\tJava")
fav_language = 'httppy '
print(fav_language.removeprefix('http'))
quote = '"A person who never made a mistake never tried anything new."'
quote_fname = "Albert"
quote_lname = "Einstein"
quote_fullname = f"{quote_fname} {quote_lname}"
qute_message = f"{quote_fullname.title()} once said, {quote}"
print(qute_message)

#integers ops; main thing is if dividing we will get floats 
# if we do anything between integers and floats we will receive floats
print(5+3)
print(10-2)
print(4*2, 16/2)

#so indexes goes 0 to .. -1 last item, -2 pre last and so on
#list is []
bicycles = ['trek', 'mountain', 'redline', 'specialized']
print(bicycles[-2].title())

messageBi = f"My first bicycle was a {bicycles[-3].title()} bike"
print(messageBi)

names = ['Johnny','Joppa','Tony']
greeting = "Hello bitch"
#so also for F - formating I using {} to insert varable with value inside of ""
newmessage = f"{names[1]} once said, {quote}, and also he think that he is the next {quote_fullname} but {names[-1]} disagree!"
print(newmessage)

valo_heroes = ['Jett', 'Neon','Fade']
print(valo_heroes[-1])
#changing item in list to new one using indexing and = to place new value to old one
valo_heroes[-1] = 'Sova'
print(valo_heroes[-1])
#to add smth I will use .append after list name and = to add new item at the end of the list
valo_heroes.append('Fade')
print(valo_heroes)
#to add item in specific position I need to use .insert and index placement and this ops will shift values
valo_heroes.insert(-2,'Breach')
print(valo_heroes)
#to permanently remove an item from list smply using "del" space and listname with item index
del valo_heroes[-3]
print(valo_heroes)
#so we can also del item but in way to use it further. Using list name + .pop but it will delete last item in the list 
# (not very flexible but usable for large amount of data)
pop_valo_hero = valo_heroes.pop()
print(valo_heroes)
print(pop_valo_hero)

bicycles.append(pop_valo_hero)
print(bicycles)
#we can add index to pop() to specify what item we want to take
my_first_hero = valo_heroes.pop(0)
valo_message = f"My first Valorant hero were {my_first_hero.upper()}"
print(valo_message)
#if i don't know what index of the item in the list I can remove
#that item using value using remove() method
#and also I mentioned that if we have () in method that eans we can use index inside ()
valo_heroes.append('Killjoy') 
my_best_hero = 'Sova'
valo_heroes.remove(my_best_hero)
print(valo_heroes)
#so if I place in new variable a value equal to value I have in the list and
#when I delete variable from the list using remove and newvalue name which contains
#that variable I will be able to use this variable in the future
print(f"{my_best_hero.upper()} is my best hero")

guest_list = ['Python','Java','C#','C++','C','TS','JS','Ruby','Rust']
guest_list.insert(0,'GO')
guest_list.insert(4,'Kotlin')
guest_list.append('R')
print(guest_list)
guest_list.pop(-2)
del guest_list[-1]
print(guest_list)
invite_count = len(guest_list)
invite_message = f"I inviting around {invite_count} languages representatives, and main host of the party will be CEO of {guest_list[-5]}"
print(invite_message)

#to sort list alphabetically I can use sort() method to sort permanently
f1_teams = ['Alpine','AstonMartin','Williams','McLaren',
            'Ferrari','Cadilac','Audi','Merc','RedBull','RacingBulls']
f1_teams.sort()
print(f1_teams)
#to make oposite there is interesting argument reverse=
f1_teams.sort(reverse=True)
print(f1_teams)
#to sort temporarily and not influence original list I can use sorted()
print(sorted(f1_teams))
#I can reverse list if needed like this
f1_teams.reverse
print(f1_teams)
#to find lenght of the list I can use len()
lenght = len(f1_teams)
print(lenght)

#CHAPTER 4. WORKING WITH LISTS
#so I need to use tab after for to store loop; 
# and for <довільна назва змінної> in range(20): 
# print(<ту змінну що ти придумав>) 
# де замість range(20) будь що iterable
print("####### CHAPTER 4 #########;;")
for language in guest_list:
    #print(language)
    #print(language,end=" is programming language //")
    print(f"{language.title()} is programming language")
    print(f"Which language do you prefer? Is it {language.upper()}",end="\n\n")
print("This is it")
#in range - so it will be in range from number to pre-last number if 1-5 it will provide me with 0,1,2,3,4.
for number in range(5):
    print(number)
for number in range(1,5):
    print(number)
#we can create list using range
range_list = list(range(1,6))
print(range_list)
#so I can multiply by number if I will place 3d number everything will add this number
#range(від, до, крок)
range_list2 = list(range(3, 20, 5))
print(range_list2)
#so there is example of exponential aka square(ступінь) so we made a list
# we added for loop and assigned range to it, after it we assigned expponenta to value usign square and then
#  simply appended result to the list
squares = []
for value in range(1,20):
    #square = value ** 2
    #squares.append(square) ---- is the same as what we wrote below ----
    squares.append(value**2)
print(squares)

print(max(squares)) #so here basic example of sum in and max calculation for list of numbers
print(min(squares))
print(sum(squares))
#list compregensions
#basically do the same as we did with for loop
squares = [value**2 for value in range(1,20)]
print(squares)
#slicing a list - using [:] to start seeing list in print from certain item
print(squares[:4])
print(squares[2:4])
print(squares[3:])
#also we can use this [-3:]
print(squares[-3:])

print("Here is my fav 3 f1 teams")
for teams in f1_teams [:3]:
    print(teams)

my_favourite_f1_teams = ["Ferrari","RedBull","Audi"]
my_friend_fav_f1_teams = my_favourite_f1_teams[:]
print("my f1 teams")
print(my_favourite_f1_teams)
print("my_friend_f1_teams")
print(my_friend_fav_f1_teams)
#coping list with "slice"
my_favourite_f1_teams.append("Alpine")
print("my f1 teams")
print(my_favourite_f1_teams)
my_friend_fav_f1_teams.append("McLaren")
print("my_friend_f1_teams")
print(my_friend_fav_f1_teams)
#copying list without slice
my_food = ['egg','bacon']
my_roomate_food = my_food
my_roomate_food.append('cereals')
print("My food")
print(my_food)
print("Roomate food")
print(my_roomate_food)

### TUPLES
# basicaly tuple is the same list but to this list we cannot append or modify
# we can create it to be static troughtout life of the program 
# to make tuple I should use () instead of [] when creating a list

my_tuple_food = ("sosages","bread", "doner")
print(my_tuple_food)
#only way to overwritee a tuple is to overwrite itself
my_tuple_food = ("coke","bread", "doner")
print(my_tuple_food)
