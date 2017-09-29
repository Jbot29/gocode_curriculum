

def simple_hash_function(hash,k):
    ret = 0
    for i in hash:
        ret = 31*ret + ord(i)
    return ret % k


#create your one miny hash table, using the simple_hash function.


class Hash():
    def __init__(self):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, item):
        pass




value = 10
h = Hash()
h['key'] = 10
assert h['key'] == 10



    
    

