class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *arg):
        for i in arg:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result += k
            else:
                self.result += i
        return self
    def subtract(self, *arg):
        for i in arg:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result -= k
            else:
                self.result -= i
        return self
md = MathDojo()
print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
