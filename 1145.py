x, y = map(int, input().split())
um = 1
con = 0

while um <= y:
    con += 1
    
    if con == x or um == y:
        print(um, end="")  
    else:
        print(um, end=" ") 

    um += 1

    if con == x:
        print()  
        con = 0
