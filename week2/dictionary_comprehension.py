#Use a dictionary comprehension create a dictionary that matches the following

r = {}

assert r == {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}

r = {}

assert r == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

r = {}

assert r == {0: True, 1: True, 2: True, 3: True, 4: True}

r = {}

assert r == {(0, 1): 1, (1, 2): 3, (3, 2): 5, (0, 0): 0, (3, 3): 6, (3, 0): 3, (3, 1): 4, (2, 1): 3, (0, 2): 2, (2, 0): 2, (1, 3): 4, (2, 3): 5, (2, 2): 4, (1, 0): 1, (0, 3): 3, (1, 1): 2}