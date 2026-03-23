#on va importer le module csv pour pouvoir lire le fichier csv 
import csv 

path='/home/user/Projet-informatique-cp1-EIlco-/data/conso-departement-annuelle.csv'

#lecture du fichier en encodage utf-8-sig pour eviter les probleme sur l'année 
#creation d'une liste vide 

data=[]
#code pour lire le fichier csv 
with open(path,'r',encoding='utf-8-sig') as fichier :
    lecteur =csv.reader(fichier,delimiter=';')#car on est en france et on utilise ; pour delimiter 

    for ligne in lecteur:
        data.append(ligne[:25])#au dela on ne conserve pas 

print(data[0])
print(data[1])

print(type(data[1][0]))
print(data[1])