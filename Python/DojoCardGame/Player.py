class Player(object):
    def __init__ (self, name="ME", max_hand_size = 7, mana = 1, health = 20):
        self.name = name
        self.board = []
        self.deck = []
        self.hand = []
        self.grave = []
        self.max_hand_size = max_hand_size
        self.mana = mana
        self.health = health

    def debug(self):
        print "Name:", self.name
        print "Board:", self.board
        print "Deck:", self.deck
        print "Hand:", self.hand
        print "Grave:", self.grave
        print "Max hand size:", self.max_hand_size
        print "Mana:", self.mana
        print "Health:", self.health
        return self
