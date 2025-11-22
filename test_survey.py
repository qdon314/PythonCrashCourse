import pytest
from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored correctly."""
    question = "What is your favorite programming language?"
    survey = AnonymousSurvey(question)
    survey.store_response('Python')

    assert 'Python' in survey.responses
    

# Using Fixtures to test multiple responses
@pytest.fixture
def survey_with_responses():
    """Fixture to create a survey and store multiple responses."""
    question = "What is your favorite programming language?"
    survey = AnonymousSurvey(question)
    responses = ['Python', 'JavaScript', 'C++']
    for response in responses:
        survey.store_response(response)
    return survey

def test_store_multiple_responses(survey_with_responses):
    """Test that multiple responses are stored correctly."""
    survey = survey_with_responses
    for response in ['Python', 'JavaScript', 'C++']:
        assert response in survey.responses