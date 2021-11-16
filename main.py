
def pyr(rows):
    for i in range(rows):
        for j in range(rows-i):
            print(" ", end=" ")
        for j in range((i-1)+(i+2)):
            print("*", end=" ")
        print()
    for i in range(rows,-1,-1):
        for j in range(i,0,-1):
            print(" ",end="")
        for j in range((i-1)+(i-2)):
            print("*", end=" ")
        print()
pyr(3)