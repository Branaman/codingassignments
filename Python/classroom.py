class Kid(object):
    def __init__(self, student_ID, student_name, seat_num = None):
        self.student_ID = student_ID
        self.student_name = student_name
        self.seat_num = seat_num
        self.student_name = student_name
        self.displayInfo()
    def speak(self):
        print "I am", self.name
        return self
    def displayInfo(self):
        print "Kid ID:", self.student_ID
        print "Kide Name:", self.student_name
        print "Seat #:", self.seat_num
        print "-------------"
        return self
class classRoom(object):
    def __init__(self, name, c_size = 20):
        self.kids = []
        self.name = name
        self.c_size = c_size
        self.teaching = 0
        self.seats = {}
        for value in range(1, c_size+1):
            self.seats[value] = 0
    def add(self, kids):
        self.kids.append(kids)
    def checkIn(self, id_num):
        if self.c_size < self.teaching+1:
            print "Classroom is Full... you uneducated :("
        else:
            self.teaching += 1
            for value in range(0, len(self.kids)):
                if self.kids[value].student_ID == id_num:
                    for seatNum in range(1, len(self.seats)+1):
                        if self.seats[seatNum] == 0:
                            self.seats[seatNum] += 1
                            self.kids[value].seat_num = seatNum
                            print self.kids[value].student_name, "checked into seat #", self.kids[value].seat_num
                            print "-------------"
                            break
    def allSpeak(self):
        for value in range(0, len(self.kids)):
            self.kids[value].speak()
    def removeNum(self, id_num):
        for value in range(0, len(self.kids)):
            if self.kids[value].student_ID == id_num:
                if self.kids[value].seat_num == None:
                    print "Kid was not checked in"
                else:
                    self.seats[self.kids[value].seat_num] = 0
                    self.kids[value].seat_num = None
                    self.teaching -= 1
                    print self.kids[value].student_name, "Is cured.... or dead"
                    print "-------------"
    def remove(self, id_num):
        for value in range(0, len(self.kids)):
            if self.kids[value].student_ID == id_num:
                if self.kids[value].seat_num == None:
                    print self.kids[value].student_name, "Was not a student and was deleted from database"
                    del self.kids[value]
                    break
                else:
                    self.seats[self.kids[value].seat_num] = 0
                    self.kids[value].seat_num = None
                    self.teaching -= 1
                    print self.kids[value].student_name, "Was checked out and deleted from database"
                    print "-------------"
                    del self.kids[value]
                    break
    def info(self):
        for value in range(0,len(self.kids)):
            print self.kids[value].student_name
            print self.kids[value].seat_num
        print "-------------"
        print self.name
        print "Capacity:", self.c_size
        print "teaching", self.teaching
        print "-------------"
def makeKids(num):
    for value in range(1, num+1):
        return "Kid"+value = Kid("Kid"+str(value), value)
def addallkids(num, classroom):
    for count in range(1, num+1):
        return classroom.add("Kid"+count)
def checkinAll(num, classroom):
    for counter in range(1, num+1):
        return classroom.checkIn("Kid"+counter)
classroom1 = classRoom("Death House", 5)
makeKids(5)
addallkids(5, classroom1)
checkinAll(5, classroom1)
classroom1.info()
classroom1.remove(3)
classroom1.allSpeak()
