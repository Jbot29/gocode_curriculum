'''
Golf Score Calculator App

The goal of this app is for you to be able to enter scores for different players and print a leaderboard.  You are given a file with the base scores for a default course that you will need to read in (ask an instructor if you don't understand golf!).

# Example UI in the Terminal:
# How many players are in the golf tournament? 2
# What is the name for player 1? Jonathan Lau
# What is the name for player 2? Jeremy Schwartz
# What are the scores for player 1? [3,3,3,3,3...]
# What are the scores for player 2? [3,3,3,3,3]
# Type p to print the leaderboard: p
# LeaderBoard
# 1 - Jonathan Lau, Overall Score: 73, +1
# 2 - Jeremy Schwartz, Overall Score: 76, +5

You will implement this idea and create a golf score calculator using classes.  

You are free to adjust the gameplay, how the app works, and to extend it as you wish.

Here are some basic recommendations for how to design your classes:

1) A CourseLayout class:

In charge of reading in the file with the base scores for the golf course.

You will use the file given to you as the default.  

Optionally, you can allow the user to enter a filename for a different golf course.

2) A PlayerScore class:

In charge of handling player information and scores

3) A AppInterface Class:

This has a simple method that runs the game and talks to the terminal I/O.

It also has a method that uses information from the CourseLayout and PlayerScore and prints a leaderboard.

Ex:

LeaderBoard
1 - Jonathan Lau, Overall Score: 73, +1
2 - Jeremy Schwartz, Overall Score: 76, +4

Note: The last number is simply the overall score minus 72 (it's how golf works...)

'''

class CourseLayout:
    def __init__(self):
        pass

class Player:
    def __init__(self):
        pass

class AppInterface:
    def __init__(self):
        pass


