def simple_hash_function(hash,k):
    ret = 0
    for i in hash:
        ret = 31*ret + ord(i)
    return ret % k


#create your one miny hash table, using the simple_hash function.


class Hash():
    def __init__(self):
        self.size = 10
        self.data = [None for x in range(0,self.size)]

    def __getitem__(self, key):
        if self.data[simple_hash_function(key,self.size)]:
            return self.data[simple_hash_function(key,self.size)]
        return None

    def __setitem__(self, key, item):
        self.data[simple_hash_function(key,self.size)] = item





h = Hash()
