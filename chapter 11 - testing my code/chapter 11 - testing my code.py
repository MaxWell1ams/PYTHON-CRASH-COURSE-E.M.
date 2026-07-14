#File naming matters — pytest auto-discovers files/functions by naming convention:
#Test files must be named test_*.py or *_test.py (test_survey.py)
#Test functions inside must start with test_ (def test_city_country():)
#Run all tests — navigate to your project folder in terminal, then:
#pytest
#It automatically finds every test_*.py file and runs every test_* function inside.
#Run one specific file:
#pytest test_survey.py
#Run one specific function inside a file:
#pytest test_survey.py::test_city_country
#To see more detail:
#bashpytest -v

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

#ASSERTION
#there most common asssertion
#assert a == b  - assert that two values are equal
#assert a !=  - assert that two values are not equal
#assert a  - assert that evaluates to True
#assert not a  - assert that evaluates to False
#assert element in list  - assert that element in the list
#assert element not in list  - assert that element not in the list

#and so on, basically test is the function and my creativity of what to test for and pytest itself just
# very comfortable to run huge amount of this functions I will write

#fixture - a resourse that using by more than one test
#for that I should use decorator @ and it will looks like that @pytest.fixture