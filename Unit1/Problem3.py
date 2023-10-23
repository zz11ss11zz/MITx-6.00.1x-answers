count = 0
l = []
for i in range(len(s)-1):
    if s[i] > s[i+1]:
        l.append(i+1)
l.append(len(s))

if len(l) == 1:
    print(s)
else:
    t = []
    tt = l[0]
    for j in range(len(l)-1):
        t.append(l[j+1]-l[j])

    ss = 0
    if max(t) <= tt:
        print('Longest substring in alphabetical order is: ',s[0:l[0]])
    else:
        maxm = t.index(max(t))
        for ii in range(maxm):
            ss += t[ii]
        print('Longest substring in alphabetical order is: ',s[ss+tt:ss+max(t)+tt])