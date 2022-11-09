#Créer un programme job19.py. Le programme devra contenir une seule fonction qui
#prend en paramètres un nombre de paramètres indéfini (uniquement des nombres).
#La fonction devra :
#- Remplir une liste myList contenant tous ces paramètres.
#- Trier par ordre croissant la liste à l’aide de la fonction sort (Donc sans la fonction
#sort)
#- Afficher la liste dans un terminal

def mysort(liste):
    permutation = True
    passage = 0
    while permutation == False:
        permutation = False
        passage = passage + 1
        for encour in range(0, len(liste) - passage):
            if liste[encour] > liste[encour + 1]:
                permutation = True
                liste[encour], liste[encour + 1] = \
                liste[encour + 1], liste[encour]
    return liste

def mydisplay(liste2):
    print(liste2)

mydisplay(mysort([78,4,9,87,21]))