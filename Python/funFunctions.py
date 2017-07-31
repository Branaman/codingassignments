def odd_even():
    for count in range(1,2001):
        if count % 2 != 0:
            print "Number is " + str(count) + ". This is an even number."
        else:
            print "Number is " + str(count) +". This is an odd number."
def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr

def layered_multiples(arr):
    new_array = []
    for value in range(len(arr)):
        new_array += [[1] * arr[value]]
  # your code here
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
