class Patient(object):
    def __init__(self, patient_ID, patient_Name, allergies, bed_Num = None):
        self.patient_ID = patient_ID
        self.patient_Name = patient_Name
        self.bed_Num = bed_Num
        self.allergies = allergies
        self.cost = patient_Name
        self.displayInfo()
    def displayInfo(self):
        print "Patient ID:", self.patient_ID
        print "Patiente Name:", self.patient_Name
        print "Bed #:", self.bed_Num
        print "Allergies:", self.allergies
        print "-------------"
        return self
class PatientCenter(object):
    def __init__(self, name, h_size = 50):
        self.patients = []
        self.name = name
        self.h_size = h_size
        self.treating = 0
        self.beds = {}
        for value in range(1, h_size+1):
            self.beds[value] = 0
    def add(self, patients):
        self.patients.append(patients)
    def checkIn(self, id_num):
        if self.h_size < self.treating+1:
            print "Hospital is Full... you ded :("
        else:
            self.treating += 1
            for value in range(0, len(self.patients)):
                if self.patients[value].patient_ID == id_num:
                    for bedNum in range(1, len(self.beds)+1):
                        if self.beds[bedNum] == 0:
                            self.beds[bedNum] += 1
                            self.patients[value].bed_Num = bedNum
                            print self.patients[value].patient_Name, "checked into bed #", self.patients[value].bed_Num
                            print "-------------"
                            break
    def removeNum(self, id_num):
        for value in range(0, len(self.patients)):
            if self.patients[value].patient_ID == id_num:
                self.beds[self.patients[value].bed_Num] = 0
                self.patients[value].bed_Num = None
                self.treating -= 1
                print self.patients[value].patient_Name, "Is cured.... or dead"
                print "-------------"
    def remove(self, idx = 0):
        del self.patients[idx]
    def info(self):
        for value in range(0,len(self.patients)):
            print self.patients[value].patient_Name
            print self.patients[value].bed_Num
        print "-------------"
        print self.name
        print "Capacity:", self.h_size
        print "Treating", self.treating
        print "-------------"
patient1 = Patient(1234, "lorem Fansico", "Lorem ipsum dolor sit amet")
patient2 = Patient(1235, "lorem prom", "Lorem ipsum dolor sit amet")
patient3 = Patient(1236, "lorem Papaya", "Lorem ipsum dolor sit amet")
patient4 = Patient(1237, "em sico", "Lorem ipsum dolor sit amet")
patient5 = Patient(1238, "Feldisco prom", "Lorem ipsum dolor sit amet")
patient6 = Patient(1239, "Feldisco Papaya", "Lorem ipsum dolor sit amet")
patient7 = Patient(1240, "Feldisco loremaya", "Lorem ipsum dolor sit amet")
hospital1 = PatientCenter("Death House", 5)
hospital1.info()
hospital1.add(patient3)
hospital1.add(patient1)
hospital1.add(patient2)
hospital1.add(patient4)
hospital1.add(patient5)
hospital1.add(patient6)
hospital1.add(patient7)
hospital1.checkIn(1234)
hospital1.checkIn(1235)
hospital1.checkIn(1236)
hospital1.info()
hospital1.removeNum(1235)
hospital1.info()
hospital1.checkIn(1237)
hospital1.checkIn(1238)
hospital1.checkIn(1239)
hospital1.checkIn(1240)
hospital1.info()
