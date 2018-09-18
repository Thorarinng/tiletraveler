#blablabla
x = 1
y = 1
position = (x,y)

while position != (3,3):
    if position == (1,1):
        print("You can Travel: , (N)orth")
        print("Your pos:" ,position)
    elif position == (1,2):
        print("You can Travel: , (N)orth or (E)ast or (S)outh")
        print("Your pos:" ,position)
    elif position == (2,2):
        print("You can Travel: , (W)est or (S)outh")
    elif position == (2,1):
        print("You can Travel: , (N)orth")
    elif position == (1,3):
        print("You can Travel: , (E)ast or (S)outh")
    elif position == (2,3):
        print("You can Travel: , (E)ast or (W)est")
    elif position == (3,3):
        print("You can Travel: , (W)est or (S)outh")
    elif position == (3,2):
        print("You can Travel: , (N)orth or (S)outh")
    elif position == (3,1):
        print("Victory")
    entry = input("Enter a direction: ")
    while position != (3,3):
        if entry == 'n' or 'N':
            position = (x,y+1)
            print("Your pos:" ,position)
            break
        elif entry == 's' or 'S':
            position = (x,y-1)
            break
        elif entry == 'e' or 'E':
            position = (x+1,y)
            break
        elif entry == 'w' or 'W':
            position = (x-1,y)
            break
        else:
            print("Invalid input")