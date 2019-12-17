with(open('rosalind_tree.txt', 'r')) as x:
    n = int(x.readline())
    g = [line.split() for line in x]
    
e= n-len(g)-1

print(e)