'''
In golf_game.py, you've seen how much data manipulation you had to do to pass in the right data to LeaderBoard and to get it to print out the right information.

In Object Oriented Programming, there is a concept called 'coupling'.

A) Tight coupling is when a group of classes are highly dependent on one another.  This scenario arises when a class assumes too many responsibilities, or when one concern is spread over many classes rather than having its own class.

B) Loose coupling is achieved by means of a design that promotes single-responsibility and separation of concerns.  A loosely-coupled class can be tested independently of other (concrete) classes.

In your golf game, none of your classes were "coupled".  They did not need to know about the other classes and could function independently.  The design was loosely-coupled.

This design has its benefts: by not coupling the classes, you can modify and change each class without worrying about how it would affect other classes.

Note that completely loose coupling is not always a good thing.  As in your example, you had to do a lot of extra work to get the data into the right format for your LeaderBoard class.

A trick in Object Oriented Programming is to pass in instance variables to a new class.

This assignment will walk you through a refactor of your code using this concept.

1) Use the classes that you have already built in golf_game.py, but instead of passing tournament_hash into the LeaderBoard class, pass the instance of the CourseLayout as well as an array of with all the Player instances.

2) This will allow you to re-use methods that you have built inside the Player and CourseLayout classes.

3) You can also add new methods inside Player and CourseLayout classes to help with any data processing you need to do in the Leaderboard class.

4) The goal is for the LeaderBoard class to be able to print the leaderboard as well as return a data structure containing all the player and course information (same as in the first assignment)  You can decide what data structures to use to acheive this functionality.  You can decide what helper methods to build to maximize code re-use.

5) You can also extend all the classes to contain additional methods.  What other data should a Player class store?  What about a CourseLayout class?  Name? Age? Height?  Weight?  Model a real golf tournament!

Tip: Inside the LeaderBoard class, you can access the instance variables of the other class instances:

e.g. self.course_layout.array_of_scores => [3,4,3,4,3,4... etc]
e.g. self.players[0].name => "Jonathan Lau"

The LeaderBoard class is an example of an interface.  It is an interface to your Players and your CourseLayout objects.  This is a classic OOP design pattern.

In general, use your intuition and don't get bogged down by theory.  Experience counts for a lot when building Object-Oriented Programs.

Remember that OOP was intended to mimick real world objects, but it doesn't always work perfectly.

KISS - Keep it simple stupid!

If you want to learn more about design patterns, consider the following:

1) https://www.youtube.com/watch?v=0vJJlVBVTFg
2) http://www.aleax.it/gdd_pydp.pdf

'''


# Copy all your code over here and modify your LeaderBoard class to take in the instance variables
# You will need to modify all the methods to use these instance variables instead
# Feel free to create new methods in Player or CourseLayout to help with your LeaderBoard class
# Don't overwrite your old code, save it for comparison!

class LeaderBoard:
    def __init__(self,course_layout_instance,array_of_player_instances):
      self.course_layout = course_layout_instance
      self.players = array_of_player_instances

# Draw a relations diagram for this program

# Draw a scope diagram for this program

# Bonus - Create another interface class called GameInterface that runs the golf tournament in the terminal.

# This class interacts with the terminal to ask for data and uses other classes to store data and write to files.

# It can print the leaderboard to terminal when you type in 'p'

# Example UI:
# How many players are in the golf tournament? 2
# How many holes are in the golf course? 18
# What is the name for player 1? Jonathan Lau
# What is the name for player 2? Jeremy Schwartz
# What are the scores for player 1? [3,3,3,3,3...]
# What are the scores for player 2? [3,3,3,3,3]
# Type p to print the leaderboard: p

# There are many ways to build this program.  Bear in mind the concepts of coupling and dependencies.

# Feel free to create new class/objects, if you think it is needed

# Once you're done, grab an instructor for a code review
