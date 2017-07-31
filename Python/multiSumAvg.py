# Write code that prints all the odd numbers from 1-1000. Use for loop, dont use a list
# Create another program that prints all the multiples of 5 from 5-1,000,000
def countup():
    for count in range(1,1000):
        print count
def countUp5():
    show = 0
    for count in range (5,1000000,5):
        print count
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
arr = [1, 2, 5, 10, 255, 3]
def sumsUp(arr):
    sums = 0
    for count in range(0,len(arr)):
        sums += arr[count]
    print sums
    return sums
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
def average(arr):
    sumsUp(arr)
    avg = sums / len(arr)
    print avg
