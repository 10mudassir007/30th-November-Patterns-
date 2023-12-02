for i in range(6,0,-1):
    for j in range(1,i+1):
        if j == 1 or j == i or i == 6:

            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()