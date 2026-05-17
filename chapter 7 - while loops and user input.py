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
