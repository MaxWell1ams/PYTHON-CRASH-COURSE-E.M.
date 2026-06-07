from class_for_t import AnonSurvey

question = "What your first language?"
language_survey = AnonSurvey(question)

language_survey.show_question()
print("Enter 'q' to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

print("THX")
language_survey.show_results()