# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.
#
# Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print
# "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:

def compareArrays(arr,arr2):
    if arr == arr2:
        print "The lists are the same"
    else:
        print "The lists are not the same."
a1 = [1,2,3,4,5]
a2 = [1,2,3,4,5]
a3 = [5,4,3,2,1]
compareArrays(a1,a2)
compareArrays(a1,a3)
