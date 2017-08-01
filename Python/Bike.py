class Bike(object):
    def __init__(self, model, price, max_speed, miles = 0):
        self.model = model
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "Model:", self.model
        print "Price:", self.price
        print "Max Speed:", self.max_speed
        print "Miles:", self.miles
    def ride(self, num):
        self.miles = self.miles + num
    def reverse(self, num):
        self.miles = self.miles - num
bike1 = Bike("Kona Dew", "$499", "20mph")
bike2 = Bike("Kona DewPlus", "$699", "30mph")
bike3 = Bike("Kona CoCo", "$799", "25mph")
bike2.displayInfo()
bike2.ride(10)
bike2.reverse(5)
bike2.displayInfo()
# KonaDewCoco.displayInfo()
# KonaDew.displayInfo()
