a = 4471
b = 8926
oddsum = 0

if a%2 == 1:
    c = a
else:
    c = a + 1

while c <= b:
    oddsum = oddsum + c
    c = c + 2

print oddsum

