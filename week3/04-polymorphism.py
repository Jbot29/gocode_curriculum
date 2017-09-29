'''

Polymorphism allows you to treat objects the same even though they maybe be different class instances.

Polymorphism exists when you define a number of subclasses which have commonly named methods. A function can use objects of any of the polymorphic classes without being aware that the classes are distinct.

In some languages, it is essential that the polymorphic classes have the same interface (or be subinterfaces of a common parent interface), or be subclasses of a common superclass. This is sometimes called "strong, hierarchical typing", since the type rules are very rigid and follow the subclass/subinterface hierarchy.

Python implements something that is less rigid, often called "duck typing". The phrase follows from a quote attributed to James Whitcomb Riley: "When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck." In short, two objects are effectively of the class Duck if they have a common collection of methods (walk, swim and quack, for example.)

In a child class, we can change how some methods work whilst keeping the same name. We call this "polymorphism" or "overriding" and it is useful because we do not want to keep introducing new method names for functionality that is pretty similar in each class.

Here is a simple example:

class Food(object):
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    def tastesLike(self):
        raise NotImplementedException("Subclasses are responsible for creating this method")
 
class HotDog(Food):
    def tastesLike(self):
        return "Extremely processed meat" 
 
class Hamburger(Food):
    def tastesLike(self):
        return "grilled goodness" 
 
class ChickenPatty(Food):
    def tastesLike(self):
        return "tastes like chicken" 
 
dinner = []
dinner.append(HotDog('Beef/Turkey BallPark', 230))
dinner.append(Hamburger('Lowfat Beef Patty', 260))
dinner.append(ChickenPatty('Micky Mouse shaped Chicken Tenders', 170))
 
# even though each course of the dinner is a different type 
# we can process them all in the same loop 

for course in dinner:
    print course.name + " is type " + str(type(course))
    print "  has " + str(course.calories) + " calories " 
    print "  and tastes like " + course.tastesLike()
 
 
# output: 
# 
#Beef/Turkey BallPark is type <class '__main__.HotDog'> 
#  has 230 calories 
#  and tastes like Extremely processed meat 
#Lowfat Beef Patty is type <class '__main__.Hamburger'> 
#  has 260 calories 
#  and tastes like grilled goodness 
#Micky Mouse shaped Chicken Tenders is type <class '__main__.ChickenPatty'> 
#  has 170 calories 
#  and tastes like tastes like chicken 

'''


# Part 1
#1) Copy the animal classes from the inheritence exercise.


#2) Add a new method to all of the classes, called speak().


#3) In each speak method add a print that prints an appropriate line for that animal. print "Woof" for a dog, etc.


#4) Create a new array, and create four new instances, one for each of your animal types.


#5) Write a for loop that enumerates each item in the array, calling the speak method on each instance.


# Part 2
#1) Copy the Employee, FullTime, and Executive classes from the last exercise here.


#2) To each class add a new method called wage()

#3) For FullTime employees the method wage returns their salary. For Executives it returns their salary plus a 25% bonus.

#4) Create an array of five FullTime employees with differing salaries, and three executives with differing salaries.

#5) Write a for loop to calculate the wage payout for a year for that company.
