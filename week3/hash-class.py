'''

Mimic classes with just hashes.


'''

def counter_increment(c_self):
    c_self["counter"] += 1

def counter_class():
    return {"counter": 0,
            "count": lambda c_self: c_self["counter"],
            "increment": counter_increment }





c = counter_class()

print c["count"](c)
c["increment"](c)
print c["count"](c)


'''

Build simple inheritance model

'''

def animal_species(c_self):
    print c_self["species"]

def animal_speak(c_self):
    pass

def animal_class():
    return {"species": "unknown animal",
            "get_species":animal_species,
            "speak":animal_speak}

def dog_speak(c_self):
    print "Woof"

def dog_class(animal):
    dog = {"species":"doge",
            "speak":dog_speak}
    a = animal()
    a.update(dog)
    return a


a = animal_class()

a["get_species"](a)
a["speak"](a)

d = dog_class(animal_class)

d["get_species"](d)
d["speak"](d)











