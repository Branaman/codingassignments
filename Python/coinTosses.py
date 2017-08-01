import random
def cointToss(val):
    head = 0
    tail = 0
    for count in range(1,val+1):
        random_num = random.random()
        random_num = round(random_num)
        if random_num==0:
            head += 1
            print "Throwing a coin.... It's a head!... Got " +str(head)+" head(s) so far and " +str(tail)+" tail(s) so far"
        else:
            tail += 1
            print "Throwing a coin.... It's a tail!... Got " +str(head)+" head(s) so far and " +str(tail)+" tail(s) so far"
        print "Ending the program, thank you!"
cointToss(5000)
