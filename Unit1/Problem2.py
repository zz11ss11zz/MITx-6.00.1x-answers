count = 0
if len(s) >= 3:
    for i in range(len(s)-2):
        if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
            count += 1
print('Number of times bob occurs is: ', count)