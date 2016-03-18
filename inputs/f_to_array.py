def f_to_array(f):
    return [int(i.rstrip()) for i in open(f,"r").readlines()]

def integer_rows_to_array(f):    
    x=[]
    readf = open(f,"r").readlines()
    it = 0
    for row in readf:
        x.append([])
        for i in row.split():
            x[it].append(int(i))
        it += 1
    return x

def integer_rows_to_dict(f):
    g = {}
    data = open(f,"r")
    for line in data:
        lst = [int(s) for s in line.split()]
        g[lst[0]] = lst[1:]
    return g

