h=int(input('hauteur :' ))
#l="/"       #left
#r="\\"      #right
#b= "_"      #base

#for i in range(h):
 #   print((h - i) * " " + l + ((i * 2) *  " ") + r)      # la pointe
  #  if i == h - 1:
   #     print(l + b * h * 2 + r)

for i in range(1,h+1):
    for j in range(1,h-i+1):
        print(" ",end="")
    for j in range(1,2*i-1+1):
        if j == 1 or j == 2*i-1 or 1 == h :
            print("* ",end="")
        else:
            print("  ",end="")
    print()