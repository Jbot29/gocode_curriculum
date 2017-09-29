'''

A stack is an array/list, but all operations happen to the end of the list.

Example:

>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]

What follows below is an actual interview question at MapMyFitness. The "trick" to this question is to use a stack. Using a stack is common in interview questions. Armed with that knowledge, try to solve it.


Write a program that determines if a string is valid or invalid.

Examples of valid strings include:

[]
()
()[]
[()]
a(b[c]d)e

Examples of invalid strings include:

[
)
[(])
[(])[]

For example, a command-line program is-string-valid should produce the following outputs for the given inputs:

$ is-string-valid '[]'
true
$ is-string-valid '['
false

'''

# Build methods, using the stack concept and the above code examples, to make these asserts pass

assert valid("()")

assert valid("[[()]]")

assert not valid("(")

assert not valid("([(])")



