def get_name_formated(first,last):
    """gen formated name"""
    full_name = f"{first} {last}"
    return full_name.title()
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

    #ok I installed pytest
    #Unit Test verifies one specific aspect of a function and Test cases is collection of unit test
    #for pytest important that function starts with test_ (it will look at functions test_)
def test_first_last_name():
    """testing get_name_formated"""
    name =get_name_formated('jack','black')
    assert name == 'Jack Black'  #assert - it's claim that I reckon that result will be like this == ''

#so also important that file also starts with name "test_"
#or I can write like: pytest "chapter 11 - testing my code\test_first_test.py"
#also to run files better in terminal what I discovered
#first I need to use cd + "folder name or direcotry name"
#than if I wnat to run file I should use .\filename.py