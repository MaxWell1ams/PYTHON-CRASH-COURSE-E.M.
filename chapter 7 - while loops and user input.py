# practicing FLAG
# so concept is that we flag some key with = True
# then defining concept while smth == to key
# it will be False or True
prompt = "type word to repeat or  "
prompt += "type 'quit' to quit: "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        acitve = False
    else:
        print(message)