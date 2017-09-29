'''

Literals. What is a literal?

A literal is anything that Python can just use with out looking anything up.

5 is a literal
7.01 is a literal
"literal string" is a literal
[] is a literal
{} is a literal

If it is not one of these things, then Python will think it is a keyword, function name, or variable.

Keywords:

if, while, not, def...

Variables:

After determing that it is not a keyword or function, Python will try to see if it is a variable.

A variable is a just a name that we tell Python about. We make Python aware of this name in two ways.

One by assigning a value to a variable.

a = 5 

This tells Python to create a new variable named a and assign the literal number 5 to it.

Now Python knows about a variable named a.

If in code or repl you type

>> "a" 

That is not the variable named a that is a string literal.

The other way is in function definition.

def new_func(param_a):
    print param_a

With this line we tell Python that there is a new function named new_func and it takes one parameter param_a

When new_func is called the data that is passed into can then be used or referenced by using param_a

When this line executes

new_func(5)

Python see that new_func requries one argument, it looks at the first, again uses the rules above, see that is it a literal, starts or moves the point
of execution into new_func, and sets param_a to 5

Another example

b = "Test String"

new_func(b)

Again Python calls or sets the execution point to new_func, sees it needs to pass an argument, finds the variable b. Applies the rules above, not a literal, keyword, function, 
assumes it is a variable named b. Fetchs the value of b then passes it to new_func, sets param_a to "Test String"

new_func(b) -> new_func("Test String")

Which then looks something like this

def new_func(param_a):
    param_a = "Test String"


For function returns you can use the substitution model as well.

def return_func():
    a = 6
    return a + 8

We can go through iterations using substitution method. 

   |
   
def return_func():
    a = 6
    return 6 + 8 #subsitute a for the value


Then in the calling and using the return value.


return_func() this gets converted in 14

return_func() -> 14

If there is no variable to "catch" the return value then it is lost.

return_data = return_func() 

gets converted to 

return_data = 14 

after the function gets called.


Use the subsitution model and convert the variable names to the literal values that Python would replace if the code was run/executed.

'''

names = {"first":"Your First Name","last":"Your Last Name"}

def new_dict(a,b):
    return {"a":a,"b":b}

def new_array(a,b):
    return [a,b]


def loop():
    the_datas = []

    times_through = 1
    
    while times_through > 0:

        print the_datas
        
        print times_through

        print 'Mrs' + names['first']
        
        the_data = new_array(new_dict("AAAAH","BAAAAH"),new_dict("CAAAH","DAAAH"))

        times_through -= times_through








