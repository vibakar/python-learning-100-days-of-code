class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_no = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no+= 1
        answer = input(f"Q{self.question_no}: {current_question.text} (True/False)?: ")
        self.check_answer(answer, current_question)

    def still_has_question(self):
        return self.question_no != len(self.question_list)
    
    def check_answer(self, answer, current_question):
        if answer.lower() == current_question.answer.lower():
            self.score+= 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was {current_question.answer}")
        print(f"Your current score is: {self.score}/{self.question_no}")
        print("\n")

