# -*- coding: utf-8 -*-
"""
Projet Informatique CP1 - Fichier Principal
Auteurs : Zayd Fliyou & Teo Dubar
"""

import csv
import os
import matplotlib.pyplot as plt
from classe.DonneeEnergie import ClasseDonneeEnergie
from classe.CollectionEnergie import CollectionEnergie
from classe.Reporting import Reporting

# =============================================================================
# 1. PRÉPARATION DES DONNÉES (Chargement direct)
# =============================================================================
path = "data/conso_nettoyee.csv"
ma_base = CollectionEnergie()
visu = Reporting()

print("="*60)
print("      CHARGEMENT DE LA BASE DE DONNÉES")
print("="*60)

# On vérifie si le fichier existe
if not os.path.exists(path):
    print(f"Erreur : Le fichier {path} est introuvable.")
else:
    # Lecture du fichier CSV
    with open(path, 'r', encoding='utf-8-sig') as f:
        lecteur = csv.reader(f, delimiter=';')
        data = list(lecteur)

    # Remplissage de la collection
    for ligne in data[1:]:
        infos = ligne[0:5] # [Année, ID_Dept, Dept, ID_Reg, Reg]
        
        # On définit les secteurs et les colonnes (Total=5, Elec=10, Gaz=15)
        secteurs = ["Agriculture", "Industrie", "Résidentiel", "Tertiaire", "Autre"]
        energies = [("Total", 5), ("Electricité", 10), ("Gaz", 15)]

        for nom_e, idx in energies:
            somme_v = 0.0
            for i in range(5):
                val = float(ligne[idx + i]) if ligne[idx + i] else 0.0
                somme_v += val
                # Création de l'objet et ajout
                ma_base.ajouter(ClasseDonneeEnergie(infos + [val], secteurs[i], nom_e))
            
            # Ajout du Total pour l'énergie (somme des 5 secteurs)
            ma_base.ajouter(ClasseDonneeEnergie(infos + [somme_v], "Total", nom_e))

    print(f"Succès : {len(ma_base)} objets créés.")

    # =============================================================================
    # 2. TEST AUTOMATIQUE (Exemple du 62)
    # =============================================================================
    print("\n" + "!"*60)
    print(" TEST AUTOMATIQUE : Pas-de-Calais (62) - Industrie")
    print("!"*60)
    
    # On force l'affichage pour prouver que ça marche
    visu.evolution_conso_dept(ma_base, "62.0", "Industrie", "Electricité")
    
    print("\nTest terminé. FERMEZ LA FENÊTRE DU GRAPHIQUE pour voir le menu.")

    # =============================================================================
    # 3. MENU GÉNÉRALISÉ (Boucle infinie)
    # =============================================================================
    while True:
        print("\n" + "="*60)
        print("                MENU PRINCIPAL D'ANALYSE")
        print("="*60)
        print(" 1. Évolution d'un secteur (choisir dépt, secteur, énergie)")
        print(" 2. Comparaison de 2 départements (Agriculture)")
        print(" 3. Comparaison par secteur (choisir dépt, année)")
        print(" 4. Répartition Électricité / Gaz (choisir dépt)")
        print(" 5. Projection consommation 2050 (Région, Secteur)")
        print("-" * 60)
        print(" Q. Quitter le programme")
        print("-" * 60)
        
        choix = input("Votre choix : ").upper()

        if choix == "1":
            d = input("Département (ex: 62) : ") + ".0"
            s = input("Secteur (Agriculture, Industrie, Résidentiel, Tertiaire, Autre) : ")
            e = input("Énergie (Electricité, Gaz, Total) : ")
            visu.evolution_conso_dept(ma_base, d, s, e)

        elif choix == "2":
            d1 = input("Premier dépt (ex: 62) : ") + ".0"
            d2 = input("Deuxième dépt (ex: 59) : ") + ".0"
            s = input("Secteur (Agriculture, Industrie, Résidentiel, Tertiaire, Autre) : ")
            visu.comparer_deux_depts(ma_base, d1, d2, s)

        elif choix == "3":
            d = input("Département (ex: 75) : ") + ".0"
            a = input("Année (ex: 2020) : ") + ".0"
            visu.comparer_secteurs(ma_base, d, a)

        elif choix == "4":
            d = input("Département (ex: 69) : ") + ".0"
            visu.repartition_elec_gaz(ma_base, d)

        elif choix == "5":
            reg = input("Région (ex: Hauts-de-France) : ")
            sec = input("Secteur (ex: Industrie) : ")
            visu.projection_2030(ma_base, reg, 2050, sec, "Electricité")

        elif choix == "Q":
            print("\nArrêt du programme. Au revoir !")
            break
        else:
            print("\n[!] Choix invalide.")