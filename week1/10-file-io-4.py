'''

Part 1: Make a program that keeps track of your budget.  The user can type in commands via the terminal to make changes/add/show the budget.

- Create a program with a simple ui loop (a function that has a while loop which keeps the program running).  THe loop will repeatedly display a list of commands and ask the user for input. (Commands are listed below)
- Once the input action is complete, display the list of command options again until the user quits (enters "q").
- Each command has an associated function that gets called when the user enters the right letter.  You will write these functions.


Commands:

"a" Add an item to the budget - should ask the user for each field name, amount, monthly
"s" Show items in the budget - calculates the total amount of expenses
"r" Remove an item from the budget
"q" Quit Program


'''



'''
**** Finish part one before moving on to Part 2 ****


A csv file is a very simple file that is used quite often. Usually a csv file will look something like this:

(a simple expenses csv file)

---
name,amount,monthly
food,1000.00,y
rent,2000.00,y
braces,2000.00,n
---


A csv usually starts with a header line that lists the names of the fields so someone reading or importing it into a spreadsheet app knows what each column is for.

Your goal is to write a simple budget app. This application will have a simple interface that shows the list of commands to the user, and allows the user to enter a command and keep doing various commands until they say
quit. 

It will store the data it gets from the user in a csv file. 

Add the following commands

1. "s" - Save file -> this converts your internal data structure to a csv and rights it out
2. "r" - Read File -> reads from a csv and converts the data into your internal data structure.

To test your output, you should be able to open the file in a spreadsheet application (e.g. Excel) after closing.

'''

 
def ui_loop():
	pass 
        
ui_loop()    
    
