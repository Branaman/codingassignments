words = "It's thanksgiving day. It's my birthday, too!"
print words
print words.find("day")
newString = words.replace("day", "month",1)
print newString
x = [2,52,-2,7,12,98]
print min(x)
print max(x)
x = ["hello",2,54,-2,7,12,98,"world"]
y = [x[0], x[len(x)-1]]
print y
xx = [19,2,54,-2,7,12,98,32,10,-3,6]
print xx
xx.sort()
print xx
# remove variables 0 to ((xx.length/2)-1) and push them to a new array. push new array to old array at the beginning
B = xx[:len(xx)/2]
C = [B] + xx[len(xx)/2:]
print B
print C
