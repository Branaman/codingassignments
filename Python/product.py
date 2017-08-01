class product(object):
    def __init__(self, item_name, price, weight, brand, status = "for sale"):
        self.item_name = item_name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.cost = price
        self.status = status
        self.displayInfo()
    def displayInfo(self):
        print "Item name:", self.item_name
        print "Price:", self.price
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        return self
    def sell(self):
        self.status = "Sold"
        return self
    def addTax(self, num):
        self.cost = self.cost * (1+num)
        return self
    def Return(self, reason):
        if reason == "Defective":
            self.cost = 0
            self.status = reason
        elif reason == "Opened":
            self.cost = self.cost * 0.80
            self.status = "for sale"
        elif reason == "Box":
            self.status = "for sale"
        return self
print "add items to inv"
product1 = product("Kona Dew", 499, 1.2, "Kona")
product2 = product("Kona Dew Plus", 799, 1.5, "Kona")
product3 = product("Kona Dr.Dew", 999, 1.2, "Kona")
product1.addTax(0.10)
product2.addTax(0.15)
product3.addTax(0.11)
print "add tax"
product1.displayInfo()
product2.displayInfo()
product3.displayInfo()
product1.sell()
product2.sell()
product3.sell()
print "sell items"
product1.displayInfo()
product2.displayInfo()
product3.displayInfo()
product1.Return("Defective")
product2.Return("Box")
product3.Return("Opened")
print "return items"
product1.displayInfo()
product2.displayInfo()
product3.displayInfo()
