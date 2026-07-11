db = {}  #emty dict
polling_active = True #flagging
while polling_active:
    nam3 = input("What is your name?")  #prept inputs
    ag3 = input("What is your age?")
    prog_lang = input("What's your favourite programming language?")
    db[nam3] = ag3,prog_lang #storing into db data [defined my key to which I will assign values =]
    print(f"Data we received so far: {db}") #checking is it works
    repeat = input("Would you like to let someone else do it? (yes/no)")
    if repeat == 'no':
        polling_active = False  #stoping the loop
        print("|||||RESULT|||||")
        for name, info in db.items(): # I missed this step trying to make trio nam3,ag3,prog_lang instead of pair
            print(f"Info about {name}:\nAge: {info[0]}\nFav programming language is: {info[1]}")
            #but I can use esier variant - name values of key at start and call them later on print instead of indexing
        for name, (age, lang) in db.items():
            print(f"Info about {name}:\nAge: {age}\nFav programming language is: {lang}")