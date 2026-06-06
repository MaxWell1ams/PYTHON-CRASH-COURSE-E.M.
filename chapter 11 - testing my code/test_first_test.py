from function_fortest import get_name_formated
def test_first_last_name():
    """testing get_name_formated"""
    name = get_name_formated('jack','black')
    assert name == 'Jack Black'

def test_first_last_middle_name():
    """Do all 3 items work"""
    name = get_name_formated('johnathan', 'gyllis', 'anthony')
    assert name == 'Johnathan Anthony Gyllis'