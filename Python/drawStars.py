# def multiply(arr,num):
#     for x in range(len(arr)):
#         arr[x] *= num
#         return arr
def layered_multiples(arr):
    new_array = []
    for value in range(len(arr)):
        if isinstance( arr[value], int ):
            print "*" * arr[value]
        else:
            print str(arr[value][0]) * len(arr[value])


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
y = [4, 6, 1, 3, 5, 7, 25]
layered_multiples(y)
layered_multiples(x)
