students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def listmaker(arg):
    for student in students:
        print student["first_name"], student["last_name"]
listmaker(students)
print "------------"
def listmaker2(arg):
    for group in arg:
        print group
        count = 0
        for user in arg[group]:
            count += 1
            name = user["first_name"] + " " + user["last_name"]
            print count, "-", name, "-", len(name)-1
listmaker2(users)
