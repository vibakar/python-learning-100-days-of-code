from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = []
for data in question_data:
    questions.append(Question(data["text"], data["answer"]))

quiz_brain = QuizBrain(questions)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_no}")