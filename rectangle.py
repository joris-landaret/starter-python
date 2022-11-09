l=int(input("largeur : "))
h=int(input("hauteur : "))

for i in range(1, h+1):
    for j in range(1, l+1):
        if i == 1 or i == h :#or j == 1: #or j == c+1:
            #print("* ",end="")
            print("- ",end="")
        elif j == 1 or j == l:
            print("| ",end="")
        else:
            print("  ",end="")
    print()