x = 5
for i in range(x,0,-1):
    spaces = " " * (x-i)
    stars = '* ' * i
    if i ==1:
        break
    print(spaces + stars)


x = 5
for i in range(1,x+1):
    spaces = " " * (x-i)
    stars = '* ' * i
    print(spaces + stars)