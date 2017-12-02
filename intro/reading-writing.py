f = open('rosalind_ini5 (1).txt', 'r')
i = 0 
a = open('outputread.txt', 'w')
for line in f:
    if i%2 == 1:
        
        a.write( line + '\n')
    i = i + 1
a.close()
f.close()