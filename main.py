"""this program will import all the data from remaining programs """
from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    question = QuestionModel(question_text, question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

