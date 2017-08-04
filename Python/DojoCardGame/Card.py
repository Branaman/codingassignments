import random
def randomName():
    adjective = ("Angry", "Sad", "Crazy", "Lustful", "Greedy", "Wrathful", "Flaming", "Tired", "Insightful", "Slow", "Random")
    title = ("General", "Scout", "Grunt", "Blacksmith", "Farmer", "Bard", "Wizard", "Warrior", "Thief", "Samurai", "Student")
    species = ("Bear", "Badger", "Koala", "Wolf", "Human", "Gorilla", "Python", "Chicken", "Lynx", "Coding Dojo", "Emu")
    return str(random.choice(adjective)+" "+random.choice(species)+" "+random.choice(title))
class Card(object):
    def __init__(self,name = False,cast = False,atk = False,defc = False):
        if name == False:
            self.name = randomName()
        else:
            self.name = name
        if atk == False:
            self.atk = random.randint(0,7)
        else:
            self.atk = atk
        if atk == False:
            self.defc = random.randint(1,7)
        else:
            self.defc = defc
        if cast == False:
            self.cast = ((self.defc+self.atk)/2)+random.randint(-1,1)
            if self.cast < 0:
                self.cast = 0
        else:
            self.cast = cast
    def debug(self):
        print "#### {0} Debug Output ####".format(self.name)
        print "# Name:",self.name
        print "# Cast:",self.cast
        print "# Attack:",self.atk
        print "# Defence",self.defc
        print "##########################"
        return self
