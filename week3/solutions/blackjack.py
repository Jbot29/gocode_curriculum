import random

suits = ('c','s','h','d')
ranks = ('2','3','4','5','6','7','8','9','10','j','q','k','a')

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + self.suit

    def __repr__(self):
        return '%s(%s)' % (self.__class__,self.rank+self.suit)

    def __radd__(self,other):
        if self.rank in ['j','q','k']:
            return 10
        elif self.rank == 'a':
            return 11
        
        return other + int(self.rank)
        
    def value(self):
        if self.rank in ['j','q','k']:
            return (10,10)
        elif self.rank == 'a':
            return (11,1)

        return (int(self.rank),int(self.rank))

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        
    def value(self):
        card_values = [c.value() for c in self.cards]
        for i in range(2):
            self.value = sum([cv[i] for cv in card_values])
            if not self.bust():
                return self.value

        return self.value

    def add(self,card):
        self.cards.append(card)

class Deck:
    def __init__(self):
        self.cards = [Card(suit,rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def one(self):
        return self.cards.pop()


class Player:
    def __init__(self,name):
        self.name = name
        self.hand = Hand()
        
    def __str__(self):
        return ' '.join([str(c) for c in self.cards])   

    def __lt__(self,other):
        return self.value > other.value
    
    def get(self,card):
        self.hand.add(card)

    def value():
        return self.hand.value()
    
    def choose(self):
        print self.name + ": (h)it, (s)tand"
        if raw_input() == 'h':
            return True
        return False

    def bust(self):
        if self.hand.value() > 21:
            return True
        return False

    def won(self):
        if self.hand.value() == 21:
            return True
        return False


class Dealer(Player):
    def __init__(self,name):
       Player.__init__(self,name)

    def __str__(self):
        return '--' + ' '.join([str(c) for c in self.cards[1:]])

    def choose(self):
        
        if self.hand.bust():
            return True

        if self.hand.value() <= 16:
            return True
        
        return False 

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [Dealer("Dealer"),Player("Player1")]
        self.players_still_in = [] 

    def print_table(self,player):
        print "\n"
        print "Player: " + player.name
        print "Hand: " + str(player)
        print "Value: " + str(player.hand())
        print "\n"

    def deal(self):
        for i in range(2):
            for player in self.players:
                player.get(self.deck.one())

    def play(self):
        self.deal()

        self.play_loop()

        self.players_still_in.sort()
        
        if len(self.players_still_in) > 1 and self.players_still_in[0].value == self.players_still_in[1].value:
            print "Draw"
        elif len(self.players_still_in) == 0:
            print "Dealer won"
        else:
            print "Won:" + self.players_still_in[0].name

    def hit_loop(self,player):
        while (True):
            self.print_table(player)
            
            player.hand()
            
            if player.won():
                self.players_still_in.append(player)
                return None
                
            hit = player.choose()
            
            print 'Player ' + 'hit' if hit else 'stayed'
            
            if not hit:
                self.players_still_in.append(player)
                return None
                
            player.get(self.deck.one())
            
            self.print_table(player)
                
            if player.bust():
                print "Player Busted"
                return None
    
    def play_loop(self):
        
        players = self.players[:]
        
        while (players):
            player = players.pop()

            self.hit_loop(player)




    
g= Game()
#g.play()
