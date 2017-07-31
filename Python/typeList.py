
# def sumsUp(arr):
#     sums = 0
#     for count in range(0,len(arr)):
#         sums += arr[count]
#     return sums
#
# def average(arr):
#     sumsUp(arr)
#     avg = sums / len(arr)
#     print avg
#
def listLoop(arr):
    sums = 0
    newStr = ""
    for count in range(0,len(arr)):
        if isinstance( arr[count], ( int, float ) ):
            sums += arr[count]
        elif isinstance( arr[count], (str) ):
            newStr += arr[count]
    print sums
    print newStr
