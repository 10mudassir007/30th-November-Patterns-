x = 5
for i in range(1,x+1):
    spaces = " " * (x-i)
    if i == 1 or i == x:

        stars = '* ' * i
    else:
        stars = '*' + ' ' *(2*(i-1)-1) +'*'
    print(spaces + stars)