#===========================================================================================================================
# zayd Fliyou et téo dubar
#===========================================================================================================================

import csv

class Conversion:
    """
    Classe dédiée à la lecture, au filtrage et au nettoyage
    des données de consommation énergétique.
    """

    def nettoyer_donnees(self, path, colonnes_a_supprimer):
        """
        Méthode pour faire la lecture et le nettoyage
        """
        data_finale = []
        
        # Lecture du fichier 
        with open(path, 'r', encoding='utf-8-sig') as fichier:
            lecteur = list(csv.reader(fichier, delimiter=';'))
            
            #  l'en-tête 
            en_tete_origine = lecteur[0]
            
            # indices des colonnes qu'on veut GARDER
            indices_a_garder = []
            for i in range(len(en_tete_origine)):
                if en_tete_origine[i] not in colonnes_a_supprimer:
                    indices_a_garder.append(i)

            
            for ligne in lecteur:
                # On construit la ligne avec les colonnes 
                ligne_coupee = [ligne[i] for i in indices_a_garder]
                
                
                if '' not in ligne_coupee and '\\N' not in ligne_coupee:
                    
                    ligne_convertie = []
                    
                    for j in range(len(ligne_coupee)):
                        valeur = ligne_coupee[j]
                        
                        # Si c'est l'en-tête, on laisse en texte
                        if ligne == lecteur[0]:
                            ligne_convertie.append(valeur)
                        
                        # Si c'est l'année (colonne 0) on met en int
                        elif j == 0:
                            ligne_convertie.append(int(valeur))
                            
                        # Sinon en float 
                        else:
                            # On vérifie si c'est un chiffre
                            if valeur.replace(',', '').replace('.', '').isdigit():
                                ligne_convertie.append(float(valeur.replace(',', '.')))
                            else:
                                # C'est du texte (nom département, région...)
                                ligne_convertie.append(valeur)
                    
                    data_finale.append(ligne_convertie)

        
        return data_finale 

# ========================================================================
# Utilisation
# ========================================================================

path_fichier = "C:/Users/zfliyou/Downloads/projet informatique/data/conso-departement-annuelle.csv

# Liste des colonnes à enlever
colonnes_a_virer = [
    'Opérateur', 'Opérateur électricité', 'Opérateur gaz', 
    'Consommation totale (MWh)', 'Consommation électricité totale (MWh)', 
    'Consommation gaz totale (MWh)', 'Géo-shape département', 'Géo-point département'
]

# On lance la classe
convertisseur = Conversion()

# ICI : on récupère le résultat 
ma_liste_propre = convertisseur.nettoyer_donnees(path_fichier, colonnes_a_virer)

print("Nettoyage terminé !")

# Exportation du fichier csv finale propre 
nom_fichier_export = 'conso_nettoyee.csv'

with open(nom_fichier_export, 'w', encoding='utf-8', newline='') as f_export:
    script_export = csv.writer(f_export, delimiter=';')
    
    
    script_export.writerows(ma_liste_propre)#writerows on trouve son utiliter sur https://docs.python.org/3/library/csv.html

print(f"Fichier exporté avec succès sous le nom : {nom_fichier_export}")