        #simple example of using input() function
#basically I linked input to key and print key which will contain what we inserted in variable input()
message = input("Write down anything and I will repeat it: ")
print(message)
#+= links current key to previous and adding to the ned variable we assigned
name = input("Enter your first name: ")
name += input("last name here: ")
print(f"Hello, {name}")
### I use Input() and Python will understand it as STRING
your_age = input("enter your age: ")
print(your_age)
your_age >= 18
### I can use Int() and Py will anderstand it as NUMBER
# so I should use int + (key) - to make it number
your_age = input("your age is?: ")
your_age = int(your_age)
print(your_age)
if your_age >= 18:
    print("big boi")
else:
    print("meh")

cars_in_garage = {'Garage_London':['Mustang','Ferrari','McLaren'],
                  'Garage_Paris':['Alpine','Pegeout','Renaut'],
                  'Garage_Kyiv':['Subaru','Lanos']}
wanted_car = input("What car are you looking for?: ")
for garage, cars in cars_in_garage.items():
    if wanted_car in cars:
            print(f"{wanted_car} car is accessible in {garage}")
if wanted_car not in cars:
    print(f"{wanted_car} car is not accessible in our garages")
#in example above I got lost unfortunatelly. But I get an idea to check
#chapters further and decided to use break operator to not expose all iterations
#but it's stopes iterations and stop finding cars level below
#so I put second if(I could use else) out of loop to not see multiple messages 
# for each iteration where car not found

#practicing WHILE loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
#so I defined number as 1, then while number less then 5
# it will print numbers infinite times
# but current_number += 1 defines to add 1 to each iteration
#in result it will increas number and stop loopm on number 5

#stoping programm with input
prompt = "type word to repeat or  "
prompt += "type 'quit' to quit: "
message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
# so defining message to be able assign new value to it
# until message not quit we run
# defining that message = input and input + prompt to contain prompt message
# to input
