n1=int(input("Choisisez une première valeur : "))
n2=int(input("Choisisez la deuxième valeur : "))
x1=range(n1+1, n2)
x2=range(n1-1, n2, -1)

if n1 > n2:
    for n in x2:
        print(n)
elif n1 < n2:
    for n in x1:
        print(n)
elif n1 == n2: 
    print('Valeurs égales')