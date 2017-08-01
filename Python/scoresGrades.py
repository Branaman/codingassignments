import random

def scoresGrades():
    for value in range(1,11):
        random_num = random.randint(60,100)
        if random_num <=69:
            print "Score: "+ str(random_num) +" Your Grade is D"
        elif random_num <=79:
            print "Score: "+ str(random_num) +" Your Grade is C"
        elif random_num <=89:
            print "Score: "+ str(random_num) +" Your Grade is B"
        elif random_num <=100:
            print "Score: "+ str(random_num) +" Your Grade is A"
    print "Program is done, enjoy your grades!"
scoresGrades()
