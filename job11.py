#Créer un programme job11.py qui parcourt le contenu du 
#fichier “domains.xml” et qui
#compte le nombre de noms de domaine.

with open ("domains.xml", "r") as fi :
    text = fi.read()
    f = len(text.split('"domain'))
print (f)