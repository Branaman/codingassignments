name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
def make_dict(arr1, arr2):
    new_dict = {}
    for names in range(0,len(arr1)):
        new_dict[arr1[names]] = arr1[names]
    for count in range(0,len(arr2)):
        new_dict[arr1[count]] = arr2[count]
    print new_dict
make_dict(name, favorite_animal)
