"""

Scoping in Python is tricky. 

Basic rules

1) Python will look local first, then global
2) When passing in variables, certain datatypes are immutable and result in creation of a new variable
3) Some data structures like lists can be changed in place and affect the original variable defined

"""



#lets try with integers the id() functions returns a unique number for a variable

x = 9

def by_value(x):
    print "x:",x," id:",id(x)
    x = 42
    print "x:",x," id:",id(x)

print id(x)
by_value(x)
print id(x)



def scope_test():
    #There is no local s, so Python looks to the global namespace
    print s

s = "Global:What is going on?"

scope_test()

def scope_test2():
    s = "scope_test2:I am local"
    #Python creates a new s, and it is in the local scope    
    print s

s = "Global:I am global s"

print

scope_test2()


def scope_test3(s):
    #no local s, look global
    print s
    s = "scope_test3:I am local now"
    #we created a new local s, so print that
    print s

print

scope_test3(s)

def scope_test4():
    l = "scope_test4:I am a local"
    print l

print

scope_test4()

#print l 

def scope_test5(s):
    print id(s)
    s += " this is a little crazy, right?"
    print id(s)
    print s
    
s = "I think"

scope_test5(s)

print s


def by_value_list(list_data):
    print "by_value_list:",list_data
    list_data = [1,2]
    print "by_value_list:",list_data

print

ld = [4,5,6]

print ld

by_value_list(ld)

print ld

def by_value_list_in_place(list_data):
    print "by_value_list_in_place:",list_data
    list_data.append(9)
    print "by_value_list_in_place:",list_data

print 
by_value_list_in_place(ld)
print ld



def by_value_list_in_place_new_list(list_data):
#    new_list = list_data
    new_list = list_data[:]
    print "by_value_list_in_place_new_list:",list_data,id(list_data),id(new_list)
    new_list.append(9)
    print "by_value_list_in_place_new_list:",list_data,new_list

print 
by_value_list_in_place_new_list(ld)
print ld



    

