x = 'acaabc'
y = 'aab'
a = len(x)
b = len(y)
for i in range(0, a - b):
if y[1:b] == x[i+1:i+b]:
print('Pattern occurred at ', i)
