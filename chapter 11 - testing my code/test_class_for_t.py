import pytest
from class_for_t import AnonSurvey

@pytest.fixture
def language_survey():
    """survey for all test functions"""
    question = "What is your first lang?"
    language_survey = AnonSurvey(question)
    return language_survey

def test_store_resonse(language_survey):
    """testing if it store response"""
    #question = "What is your first lang?"
    #language_survey = AnonSurvey(question)
    language_survey.store_response('Ukrainian')
    assert 'Ukrainian' in language_survey.responses

def test_store_3_responses(language_survey):
    """testing if stores 3 responses"""
   # question = "What is your first lang?"
   # language_survey = AnonSurvey(question)  - no need in this as its in th main function
    responses = ['Ukrainian','Eng','French']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses