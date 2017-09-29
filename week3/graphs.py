

# https://www.python.org/doc/essays/graphs/




graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}



def find_path(graph, start, end, path=[]):
        #find a path from the start to the end.
