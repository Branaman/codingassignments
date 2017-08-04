from Card import Card
from Deck import Deck
from Player import Player

class Table(object):
    def __init__(self):
        self.players = []
        self.turnCount = 0
        self.turnPhase = 0
    def addPlayer(self,player):
        self.players.append(player)
        return self
    def outputScreen(self):
        print "I printed the board!"
        return self

    # GAME LOGIC FUNCTIONS
    def getMana(self,player):
        pass
    def untapCards(self,player):
        pass
    def drawCard(self,player):
        pass
    def playCard(self,player):
        pass
    def combat(self,player):
        pass
    def endTurn(self):
        pass

    # OTHER LOGIC FUNCTIONS
    def checkDeath(self,player):
        pass
    def winState(self,player):
        pass
    def debug(self):
        print "##### PLAYER DEBUG #####"
        print self.players
        print self.turnCount
        print self.turnPhase
        return self
# TEST OUTPUT...
# table = Table()
# table.debug()
# card = Card()
# card.debug()
# deck = Deck("foo","ME")
# deck.debug()
player = Player()
player.debug()
