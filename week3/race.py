'''

Race Game.

We are going to buid a simple race game, where racers can be added to the race, and the race run step by step.  The game shows the race on the terminal screen.

Step 1: 


Each race has a hard-coded, fixed length, where that length is the number of characters of the ---- line (see below).

The race progress by calling .move() on each racer for each step of the race.

After completing .move() on each racer, use .draw() to draw their positions on the screen.   This happens over and over again, step by step, until someone wins the race and reaches the end of the --- line.

Below is a sample output. For each step in the race, the long ----- line is printed.

E.G.
. is the turtle
= is the horse
/ is the rabbit

|----------------------------------------|
 .
     =
   /

|----------------------------------------|
  .
          =
      /

|----------------------------------------|
   .
               =
         /

|----------------------------------------|
    .
                    =
            /

|----------------------------------------|
     .
                         =
               /

|----------------------------------------|
      .
                              =
                  /

|----------------------------------------|
       .
                                   =
                     /

|----------------------------------------|

Step 2:

Fill out the Racer parent class and make three children from this class for each of Rabbit, Horse, and Turtle.

Or, you can name them anything you want.


Step 3 (Bonus):

When the race is complete, build a leaderboard of the all the racers and print to screen.

'''

class Race(object):
    def __init__(self):
        """ Constructor for race, add all variables needed for the race """
        pass
        
    def add_racer(self,new_racer):
        """ Has a racer instance given to it, and adds it to an internal data structure  """
        pass
        
    def race(self):
        """ Once all the racers have been added, then you can run the race """
        pass


class Racer(object):
    def __init__(self):
        self.position = 0
        self.speed = 0
        self.character = ""
        self.name = ""

    def move(self):
        """ this updates the position """
        pass

    def draw(self):
        """ this draws the position of the racer in online on the screen """
        pass

        
'''

Example usage:

r = Race()
r.add_racer(Turtle())
r.add_racer(Horse())
r.add_racer(Rabbit())

r.race()
'''



        
