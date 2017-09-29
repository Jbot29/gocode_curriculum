# Write a function which implements the Pascal's triangle:

# 1
# 1    1
# 1    2    1
# 1    3    3    1
# 1    4    6    4    1
# 1    5    10    10    5    1

# The desired output should be a list of lists where each internal list contains one row of the triangle. Like so:

# [[1], [1, 1], [1, 2, 1]...]

def pascal(n):
	pass

assert pascal(3) == [[1], [1, 1], [1, 2, 1]]

def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result

def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

def pascal(n):
    if n == 1:
        return [1]
    else:
        p_line = pascal(n-1)
        line = [ p_line[i]+p_line[i+1] for i in range(len(p_line)-1)]
        line.insert(0,1)
        line.append(1)
    return line

print(pascal(6))

print(pascal(6))