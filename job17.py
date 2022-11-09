#Créer un programme job17.py. Le programme devra contenir une fonction qui prend en
#paramètres un nombre de paramètres indéfini (uniquement des nombres).
#La fonction devra :
#- Remplir une liste myList contenant tous ces paramètres.
#- Parcourir et afficher dans le terminal uniquement les nombres pairs de la liste.

def myfunction(*params):
    myList=[]
    for param in params:
        if isinstance(param,(int)):
            myList.append(param)
        else:
            print ("Atention")

    for element in myList:
        if element % 2 == 0:
            print(element)

myfunction(3,6,89,78,2,'k')