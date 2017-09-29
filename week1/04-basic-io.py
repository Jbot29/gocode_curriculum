'''

Every process has three built-in file handles. Standard out, Standard in, and Standard error. Abreiviated as stdout,stdin,stderr.

A process can output data to stdout, read data from stdin, and output errors to stderr.

When you run an application in terminal, these file handles are connected to the terminal you are in.

So if you run a program in terminal and it has a print command in it, the string data gets sent to stdout, which is connected to the terminal screen. 

Unix is based on this idea of chaining commands or processes together, using stdin and stdout.

cat largefile.txt | more

In the case above the cat process prints out the file - largefile.txt to stdout, the more process is invoked which gets that stdout as stdin and can then do further processing on it.


'''


#print "Hello World" to the screen


#print out your name

your_name = ""

print "Hello, I am %s" % your_name

#print out your city, and country 

your_city = ""
your_country = ""

print "I come from %s,%s" % (your_city,your_country)

#use the method raw_input to ask the user for thier city, and then their country, print out both


#ask the user to enter a number, then print out that number


#ask the user to enter their birth year, calculate their age and print it to the screen


#ask the user for the tempature in fahrnheit, convert it to celsius and print out the result
#c = (f - 32) * (5/9)


#ask the user for a price (ex: 20.54) and calculate a 20% tip. Print out both the total amount and the tip amount




