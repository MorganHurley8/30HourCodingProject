import random


class q1:
    q1 = "What was the study of man called? "
class q2:
    q2 = "Who was the first chancellor of germany?" 
class q3:
    q3 = "What was early italy divided into?"

question = ['q1', 'q2', 'q3',]

answer = input(random.choice(question))
type(answer)
if random.choice == 'q3':
    if answer == "italian city states":
        print("correct")
    else:
        print("incorrect")
elif random.choice == 'q2':
    if answer == "bismark":
        print("correct")
    else:
        print("incorrect")
else:
    if answer == "humanism":
        print("correct")
    else:
        print("incorrect")




