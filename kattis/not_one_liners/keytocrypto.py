x, k, a = input(), input(), ""
for i in range(len(x)): a,k = (lambda a, k, j: (a+chr(j+65), k+chr(j+65)))(a,k,(ord(x[i]) - ord(k[i]) - 130) % 26)
print(a)

