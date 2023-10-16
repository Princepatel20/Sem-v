def NAIVE_STRING_MATCHING(p, t):

n = len(t)
m = len(p)

for i in range(n - m+1):
j = 0

while(j < m) and t[i+j] == p[j]:
j+=1
if (j == m):
print("pattern occures at index ", i)


t = "ACAABC"
p = "AAB"

NAIVE_STRING_MATCHING(p, t)
 
