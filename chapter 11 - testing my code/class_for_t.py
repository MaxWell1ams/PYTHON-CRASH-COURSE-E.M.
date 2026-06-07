class AnonSurvey:
    """collect surveys"""
    def __init__(self, question):
        """storing question"""
        self.question = question
        self.responses = []
    def show_question(self):
        """show questions"""
        print(self.question)
    def store_response(self, new_response):
        """store response"""
        self.responses.append(new_response)
    def show_results(self):
        """show all the resonses"""
        print("Survey results:")
        for response in self.responses:
            print(f" - {response}")