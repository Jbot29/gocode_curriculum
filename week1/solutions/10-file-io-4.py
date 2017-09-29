'''

A csv file is a very simple file that is used quite often. Usually a csv file will look something like this

A simple expenses csv file

---
name,amount,monthly
food,1000.00,y
rent,2000.00,y
braces,2000.00,n
---


A csv usually starts with a header line that lists the names of the fields so someone reading or importing it into a spreadsheet app knows what each column is for.

The task is to write a simple budget app. This application will have a simple interface that shows the list of commands to the user, and allows to enter a command and keep doing it until they say
quit. 

It will store the data it gets from the user in a csv file. 

The program will have the following commands

1. Open a file - should then ask the user for the file name to open
2. Save file
3. Show items in the budget - calculates the total amount of expenses
4. Add an item to the budget - should ask the user for each field name, amount, monthly
5. Remove an item from the budget

On open the program needs to read in the file data, and on save write out the changes. You can only use the tools shown, no extra modules.

To test you should be able to open the file in a spreadsheet application after closing.

'''

from collections import OrderedDict
import os.path
    
def write_data(filename,data):
    with open(filename,"w+") as f:
        f.write(data)

def read_data(filename):
    if not os.path.exists(filename):
        return []
    
    with open(filename,"r") as f:
        return f.readlines()

def ask_user(display):
    return raw_input(display)

def new_budget_item():
    nbi = OrderedDict()

    nbi["name"] = ask_user("Name:")
    nbi["amount"] = ask_user("Amount:")
    nbi["monthly"] = ask_user("monthly:")

    return nbi

def array_dict_to_csv(data):
    if len(data) == 0:
        return ""

    lines = ""
    
    #build header
    lines += ','.join(data[0].keys()) + "\n"
    
    for row in data:
        lines += ','.join(row.values()) + "\n"
        
    return lines

def csv_file_to_dict(data):
    rows = []

    if len(data) == 0:
        return []
    
    columns = data[0].strip('\n').split(',')

    for row in data[1:]:
        row_data = row.strip('\n').split(',')
        nbi = OrderedDict()
        
        for i,column in enumerate(columns):
            nbi[column] = row_data[i]
            
        rows.append(nbi)
        
    return rows

def print_options():
    print "\nCommands:"
    print "o)pen file"
    print "s)ave file"
    print "l)ist items"
    print "a)dd item"
    print "r)emove item"
    print "d)ump state"
    print "q)uit"

def open_command(state):
    state["file_name"] = ask_user("File Name:")
    state["rows"] = csv_file_to_dict(read_data(state["file_name"]))

def save_command(state):
    write_data(state["file_name"],array_dict_to_csv(state["rows"]))
    
def add_budget_item(state):
    state["rows"].append(new_budget_item())

def list_budget_items(state):
    print "Items"
    amounts = []
    for i,row in enumerate(state["rows"]):
        row_string = "%s) " % (i)
        for key,value in row.items():
            row_string += key + ":" + value + " "
            if key == "amount":
                amounts.append(float(value))
        
        print row_string

    print "Total Amount:" + str(sum(amounts))

def remove_budget_item(state):
    item_number = int(ask_user("Item Number:"))
    del state["rows"][item_number]

    
def dump_state(state):
    print state

commands = {'o':open_command,
            's':save_command,
            'a':add_budget_item,
            'l':list_budget_items,
            'r':remove_budget_item,
            'd':dump_state}
    
def ui_loop():

    state = {"file_name": "",
             "rows": []}
    
    while (True):
        print_options()
        command = ask_user(":")
        if command == 'q':
            break

        if commands.has_key(command):
            commands[command](state)
                
        
        
ui_loop()    
    
