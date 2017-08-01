class Car(object):
    def __init__(self, fuel, price, max_speed, mileage = 0):
        self.fuel = fuel
        self.price = price
        self.max_speed = max_speed
        self.mileage = mileage
        if self.price >= 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.displayInfo()
    def displayInfo(self):
        print "Price: $", self.price
        print "Max Speed:", self.max_speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax
car1 = Car("full", 4999, "20mph", "100mpg")
car2 = Car("full", 9999, "50mph", "20mpg")
car3 = Car("full", 12999, "40mph", "50mpg")
car4 = Car("full", 2999, "450mph", "70mpg")
car5 = Car("full", 10999, "25mph", "10mpg")
car6 = Car("full", 6999, "10mph", "16mpg")
# KonaDewCoco.displayInfo()
# KonaDew.displayInfo()
