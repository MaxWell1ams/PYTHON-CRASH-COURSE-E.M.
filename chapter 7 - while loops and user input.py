#simple example of using input() function
#basically I linked input to key and print key which will contain what we inserted in variable input()
#message = input("Write down anything and I will repeat it: ")
#print(message)
#+= links current key to previous and adding to the ned variable we assigned
#name = input("Enter your first name: ")
#name += input("last name here: ")
#print(f"Hello, {name}")
### I use Input() and Python will understand it as STRING
#your_age = input("enter your age: ")
#print(your_age)
#your_age >= 18
### I can use Int() and Py will anderstand it as NUMBER
# so I should use int + (key) - to make it number
#your_age = input("your age is?: ")
#your_age = int(your_age)
#print(your_age)
#if your_age >= 18:
#    print("big boi")
#else:
#    print("meh")

cars_in_garage = {'Garage_London':['Mustang','Ferrari','McLaren'],
                  'Garage_Paris':['Alpine','Pegeout','Renaut'],
                  'Garage_Kyiv':['Subaru','Lanos']}
wanted_car = input("What car are you looking for?: ")
for garage, cars in cars_in_garage.items():
    if wanted_car in cars:
            print(f"{wanted_car} car is accessible in {garage}")
    else:
            print(f"{wanted_car} car is not accessible in {garage}")

#
#    if customer_input in car:
#        print(f"{customer_input} car is accessible in {garage}")
#    else:
#        print(f"{customer_input} car is not accessible in {garage}")
