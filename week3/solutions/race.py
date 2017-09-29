

class Race(object):
    def __init__(self):
        self.racers = []
        self.length = 40
        self.leaderboard = []
        
    def add_racer(self,new_racer):
        self.racers.append(new_racer)

    @classmethod
    def racer_cmp(cls,ra,rb):
        if ra.position < rb.position:
            return 1
        elif ra.position == rb.position:
            return 0
        else:
            return -1

    def order_leaderboard(self):
        self.leaderboard = self.racers[:]
        self.leaderboard.sort(Race.racer_cmp)
        
    def race(self):
        while True:
            print "|" + "-" * self.length + "|"
            for racer in self.racers:
                racer.move()
            
                if racer.position >= self.length:
                    print "Racer Won"
                    self.order_leaderboard()
                    return 

                racer.draw()


class Racer(object):
    def __init__(self):
        self.position = 0
        self.speed = 0
        self.character = ""
        self.name = ""

    def move(self):
        self.position += self.speed

    def draw(self):
        print " " * self.position + self.character

    def __repr__(self):
        return self.name
    
class Turtle(Racer):
    def __init__(self):
        super(Turtle,self).__init__()
        self.speed = 1
        self.character = '.'
        self.name = "Turtle"

class Rabbit(Racer):
    def __init__(self):
        super(Rabbit,self).__init__()
        self.speed = 3
        self.character = '/'
        self.name = "Rabbit"


class Horse(Racer):
    def __init__(self):
        super(Horse,self).__init__()
        self.speed = 5
        self.character = '='
        self.name = "Horse"
        

r = Race()
r.add_racer(Turtle())
r.add_racer(Horse())
r.add_racer(Rabbit())

r.race()
print r.leaderboard



        
