from itertools import count
import random



global_next_id = 0

class tally:
    def _intit_ (self):
        global global_next_id
        self.id = global_nest_id

        global_next_id += 1

questions = ['q1', 'q2', 'q3', 'q4']
print(random.choice(questions))

class response:
    answer = input(' : ')
    type(answer)

    if questions == 'q1' :
        if answer == 'a' or answer == 'A':
            global_next_id += 1
            print('Correct, your score: ', global_next_id)
        else:
            print('Incorrect, your score: ', global_next_id)

    elif questions == 'q2' :
        if answer == 'b' or answer == 'B':
            global_next_id += 1
            print('Correct, your score: ', global_next_id)
        else:
            print('Incorrect, your score: ', global_next_id)

    elif questions == 'q3' :
        if answer == 'c' or answer == 'C':
            global_next_id += 1
            print('Correct, your score: ', global_next_id)
        else:
            print('Incorrect, your score: ', global_next_id)

    else:
        if answer == 'd' or answer == 'D':
            global_next_id += 1
            print('Correct, your score: ', global_next_id)
        else:
            print('Incorrect, your score: ', global_next_id)


