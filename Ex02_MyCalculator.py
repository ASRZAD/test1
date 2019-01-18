c = '15+12*3-1/5+3'
cc = c.split('+')
# print(cc)
L = []
for k in cc:
    # print(k)
    if '-' not in k:
        # print(k)
        L.append(float(k))
    if '-' in k:
        k = k.split('-')
        k[1] = '-'+k[1]
        # print(k)
        for x in k:
            # L1.append(x)
            if '*' in x:
                N = x.split('*')
                M = float(N[0])*float(N[1])
                L.append(M)
            elif '/' in x:
                N = x.split('/')
                M = float(N[0])/float(N[1])
                L.append(M)

print('Answer of This Problem is {}!'.format(sum(L)))