"""this program will act as a brain to the whole program"""


class QuizBrain:
    def __init__(self, question_data):
        self.question = question_data
        self.score = 0
        self.question_no = 0

    def next_question(self):
        """this will trigger next question"""
        current_question = self.question[self.question_no]
        self.question_no += 1
        answer = input(f"Q.{self.question_no}:{current_question.question}(True/False)").lower()
        self.check_answer(answer, current_question.answer)
        print(f"your score is {self.score}/{self.question_no}")

    def still_has_questions(self):
        """this will trigger to check still there are questions are not"""
        if len(self.question) > self.question_no:
            return True
        else:
            return False

    def check_answer(self, answer, actual_answer):
        """this will check the answer either true or false"""
        if answer.lower() == actual_answer.lower():
            print("you have given correct answer")
            self.score += 1
        else:
            print("you have given wrong answer")
