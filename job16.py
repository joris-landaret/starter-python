#Créer un programme job16.py. Le programme devra contenir une fonction qui prend en
#paramètres un nombre de paramètres indéfini.
#La fonction écrira tous les paramètres dans le terminal.

def myfunction(*param):
    print(param)

myfunction("et","oui","mais","non")