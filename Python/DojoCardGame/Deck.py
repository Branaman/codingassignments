# notes:
# bottom of the deck is index cards[0]
class Deck(object):
    def __init__(self, name, player, max_deck_size = 50):
        # initiates the deck with a deck name, player associated with deck, max deck size, and current deck size. Also creates empty array for holding future cards.
        self.player = player
        self.cards = []
        self.name = name
        self.max_deck_size = max_deck_size
        self.decksize = 0
    def add(self, card):
        # checks if the deck is full then adds card to deck
        if self.max_deck_size < self.decksize+1:
            print "Deck is Full, Cannot add card"
        else:
            self.decksize += 1
            self.cards.append(card)
    def removeSpec(self, card_name):
        # removes a specific card in the deck by name
        for value in range(0, len(self.patients)):
            if self.cards[value].name == card_name:
                self.remove(value)
    def remove(self, idx = -1):
        # default removes top card
            self.decksize -= 1
            self.cards.remove(value)
    def suffle(self):
        # suffles deck 7 times
        for value in range(0,7):
            random.suffle(self.cards)
    def draw(self, count):
        # pull cards from index -value, pass that card to the player, and remove that card
        for value in range(0, count):
            self.player.cards.append(self.cards[-value])
            self.remove()
    def debug(self):
        # lists all current info for deck
        for value in range(0,len(self.cards)):
            # states all cards in deck as well as their currenty deck index
            print "-------------"
            print self.cards[value].name
            print "index", value
        print "-------------"
        print "Deck Name:", self.name
        print "Player Name:", self.player
        print "max deck size:", self.max_deck_size
        print "decksize:", self.decksize
        print "-------------"
