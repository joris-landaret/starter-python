#Créer un programme job12.py qui parcourt le contenu du fichier “data.txt” et qui compte
#le nombre de mots (sans caractère spéciaux) qui s’y trouvent.

import re

f = open("data.txt", "r")
text = f.read()
pattern = '[a-zA-Z]+'
matches = re.findall(pattern, text)   # findall = cherche tout les mots dans pattern

print(matches)