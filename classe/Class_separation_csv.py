# -*- coding: utf-8 -*-
# auteur Zayd Fliyou, Teo Dubar 
#et bibliotheque write de phyton
import csv 

class Separateur_Csv:
    def __init__(self, chemin_de_fichier):
        # Stockage du chemin et initialisation des listes
        self.chemin_de_fichier = chemin_de_fichier
        self.en_tete = []
        self.data = []
        
    def lire_fichier(self):
        # Utilisation de utf-8-sig pour ignorer les caracteres speciaux de Windows
        with open(self.chemin_de_fichier, 'r', encoding='utf-8-sig') as fichier:
            lecteur = csv.reader(fichier, delimiter=';')
            
            # Recuperation de la premiere ligne (entete)
            self.en_tete = next(lecteur)
            
            # Stockage des donnees dans self.data
            for ligne in lecteur:
                self.data.append(ligne)
    
    def creer_fichiers_secteurs(self):
        nb_colonnes = len(self.en_tete)
        
        # On commence a la 6eme colonne (index 5)
        for i in range(5, nb_colonnes):
            
            # Nettoyage du nom pour eviter les erreurs de fichier
            nom_secteur = self.en_tete[i].replace(' ', '_').replace('/', '-')
            nom_fichier = f"data/conso_{nom_secteur}.csv"
            
            with open(nom_fichier, 'w', encoding='utf-8', newline='') as f_export:
                scripteur = csv.writer(f_export, delimiter=';')
                
                # Ecriture de l'entete (5 colonnes de base + secteur i)
                nouvel_en_tete = self.en_tete[:5] + [self.en_tete[i]]
                scripteur.writerow(nouvel_en_tete)
                
                # Ecriture des lignes
                for ligne in self.data:
                    if len(ligne) > i:
                        nouvelle_ligne = ligne[:5] + [ligne[i]]
                        scripteur.writerow(nouvelle_ligne)
            
            print("Succes : " + nom_fichier)