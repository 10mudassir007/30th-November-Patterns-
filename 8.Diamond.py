x = 4
for i in range(1,x+1):
    spaces = " " * (x-i)
    stars = ' *' * i
    print(spaces + stars)

x = 5
for i in range(x,0,-1):
    spaces = " " * (x-i)
    stars = '* ' * i
    print(spaces + stars)


