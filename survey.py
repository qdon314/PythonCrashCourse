class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Initialize the survey with a question and an empty list of responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Display the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Display all the responses collected from the survey."""
        print("Survey Results:")
        for response in self.responses:
            print(f"- {response}")

