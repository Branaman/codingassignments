class Call(object):
    def __init__(self, call_ID, caller_name, caller_num, call_time, call_length):
        self.call_ID = call_ID
        self.caller_name = caller_name
        self.caller_num = caller_num
        self.call_time = call_time
        self.cost = caller_name
        self.call_length = call_length
        self.displayInfo()
    def displayInfo(self):
        print "Call ID:", self.call_ID
        print "Caller Name:", self.caller_name
        print "Phone #:", self.caller_num
        print "Time:", self.call_time
        print "Call Length:", self.call_length
        print "-------------"
        return self
class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)
    def add(self, calls):
        self.calls.append(calls)
        self.queue_size = len(self.calls)
    def removeNum(self, number):
        for value in range(0, len(self.calls)):
            if self.calls[value].caller_num == number:
                del self.calls[value]
        self.queue_size = len(self.calls)
    def remove(self, idx = 0):
        del self.calls[idx]
        self.queue_size = len(self.calls)
    def info(self):
        for value in range(0,len(self.calls)):
            print self.calls[value].caller_name
            print self.calls[value].caller_num
        print self.queue_size
        print "-------------"
    def getQueue(self):
        for negvalue in range(0, len(self.calls)):
            for count in range(1, len(self.calls)-negvalue):
                if self.calls[count-1].call_time > self.calls[count].call_time:
                    temp = self.calls[count-1]
                    self.calls[count-1] = self.calls[count]
                    self.calls[count] = temp
        for value in range(0,len(self.calls)):
            print self.calls[value].caller_name
            print self.calls[value].caller_num
            print self.calls[value].call_time
        print "-------------"
call1 = Call(12435, "Joe Blow", "313-250-2222", 1800, 120)
call2 = Call(12135, "Jane Blue", "323-260-2252", 1700, 20)
call3 = Call(12415, "The New Guy", "215-251-1234", 1600, 50)
callcenter2 = CallCenter()
callcenter2.info()
callcenter2.add(call3)
callcenter2.add(call1)
callcenter2.add(call2)
callcenter2.info()
callcenter2.removeNum("323-260-2252")
callcenter2.info()
callcenter2.remove()
callcenter2.info()
