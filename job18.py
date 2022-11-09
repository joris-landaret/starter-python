#Créer un programme job18.py. Le programme devra contenir une fonction qui prend en
#paramètres un nombre de paramètres indéfini (uniquement des nombres).
#La fonction devra :
#- Remplir une liste myList contenant tous ces paramètres.
#- Trier par ordre croissant la liste à l’aide de la fonction sort
#- Afficher la liste dans un terminal

def myfunction(*params):
    mylist=[]
    
    for param in params:
        if isinstance(param,(int)):
            mylist.append(param)
            mylist.sort
        else:
            print ("Atention")
    
    print(mylist)

myfunction(3,6,89,78,2,'r')