# class User:
#     def __init__(self, user_id, user_name):
#         self.id = user_id
#         self.username = user_name
#         self.followers = 0
#         self.following = 0

#     def follow(self , user):
#         user.followers +=1
#         self.following +=1 


# user_1 = User("001" , "job")
# user_2 = User("002", "Stave")
# user_3 = User("003", "mark")

# user_1.follow(user_2)
# user_1.follow(user_3)


# # user_2 = User()
# # user_2.id = "002"
# # user_2.UserName = "job"

# # user_3 = User()
# # user_3.id = "003"
# # user_3.UserName = "Mark"

# print(user_1.followers)
# print(user_1.following)

# print(user_2.followers)
# print(user_2.following)

# print(user_3.followers)
# print(user_3.following)

from question_model import Qustion
from data import question_data
from quiz_brain import QuizBrain

qustion_bank = []

for qustion in question_data:
    question_text = qustion["text"]
    qustion_answer = qustion["answer"]
    new_qustion = Qustion(question_text, qustion_answer )
    qustion_bank.append(new_qustion)

quiz = QuizBrain(qustion_bank)

while quiz.still_has_qustions():
    quiz.next_qustion()

print("You've completed the quize")
print(f" Your final score was: {quiz.score}/{quiz.qustion_number}")
