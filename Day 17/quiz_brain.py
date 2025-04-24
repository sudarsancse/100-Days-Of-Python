class QuizBrain:
    def __init__(self , q_list):
        self.qustion_list = q_list
        self.qustion_number = 0
        self.score = 0

    def still_has_qustions(self):
        return self.qustion_number < len(self.qustion_list)

    def next_qustion(self):
        current_qustion = self.qustion_list[self.qustion_number]
        self.qustion_number +=1
        user_ans = input(f"Q.{self.qustion_number}: {current_qustion.text} (True/False): ").lower()
        self.check_answer(user_answer = user_ans, current_answer = current_qustion.answer)


    def check_answer(self, user_answer, current_answer):
        if user_answer == current_answer.lower() :
            self.score +=1
            print("You got it right ")
        else:
            print("That's worng")
        print(f"The currect answer is {current_answer}")
        print(f"The currect score is {self.score}/{self.qustion_number}")
        print("\n")

