x='Au revoir'
c='Bonjour'

while True:
    a=input(">")
    if a==c:
        print("Bonjour à toi")
    elif a == x:
        break
    else:
        print(a)