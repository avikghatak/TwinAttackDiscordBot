import string

t = int(input())
for i in range(t):
    s = input()
    n=len(s)
    ok = 1
    for i in range(n):
        if (s[i] > 'z' or s[i] < 'a'):
            print('not ok')
            ok = 0
            break
    if ok == 0:
        break
    s=s.lower()
    l1=string.ascii_lowercase
    arr=['a']*n
    for i in range(n):
        x=s[i]
        arr[i]=l1[(l1.index(x)+pow(2,n-i-1,26))%26]
    final = ''.join(arr)
    print(final)