# -*- coding: utf-8 -*-
"""

Auteurs : Zayd Fliyou & Teo Dubar
"""

import matplotlib.pyplot as plt

class Reporting:
    def __init__(self):
        """Initialise la classe Reporting sans attributs spécifiques."""
        pass # car on n'as pas besoin de stocker de valeur 

    def evolution_conso_dept(self, collection, num_dept, secteur, energie):
        """
        FONCTIONNALITÉ 1 : Évolution annuelle pour un département, un secteur et une énergie.
        Entrées : collection (CollectionEnergie), num_dept (str), secteur (str), energie (str)
        """
        # Filtrage des données selon les critères demandés
        data_filtree = collection.filtre_departement(num_dept).filtre_secteur(secteur).filtre_energie(energie)
        data_filtree.sort() # Tri chronologique pour le tracé de la ligne
        # Extraction des listes d'axes
        x = data_filtree.annee()
        y = data_filtree.consomation()
        plt.figure(figsize=(10, 5))
        # Utilisation de plot pour montrer l'évolution continue
        plt.plot(x, y, marker='o', linestyle='-', color='b', label=f"{secteur} ({energie})")
        plt.title(f"Évolution de la consommation - Dépt {num_dept}")
        plt.xlabel("Années")
        plt.ylabel("Consommation (MWh)")
        plt.legend()
        plt.grid(True, linestyle=':')
        plt.show()

    def comparer_deux_depts(self, collection, d1, d2, secteur="Agriculture"):
        """
        FONCTIONNALITÉ 2 : Comparaison de deux départements par nuage de points (scatter).
        """
        # Filtrage pour le premier département
        c1 = collection.filtre_departement(d1).filtre_secteur(secteur).filtre_energie("Total")
        # Filtrage pour le deuxième département
        c2 = collection.filtre_departement(d2).filtre_secteur(secteur).filtre_energie("Total")
        c1.sort()
        c2.sort()
        plt.figure(figsize=(10, 5))
        # Utilisation de scatter (nuage de points) comme demandé dans le sujet
        plt.scatter(c1.annee(), c1.consomation(), color='red', label=f"Département {d1}")
        plt.scatter(c2.annee(), c2.consomation(), color='green', label=f"Département {d2}")
        plt.title(f"Comparaison de consommation : {d1} vs {d2} (Secteur {secteur})")
        plt.xlabel("Années")
        plt.ylabel("Consommation Totale (MWh)")
        plt.legend()
        plt.show()

    def comparer_secteurs(self, collection, num_dept, annee):
        """
        FONCTIONNALITÉ 3 : Comparaison des secteurs pour une année (Diagramme en barres).
        """
        # On filtre sur l'année et le département choisi
        data = collection.filtre_departement(num_dept).filtre_annee(annee).filtre_energie("Total")
        noms_secteurs = []#création liste vide 
        valeurs_conso = []
        # On parcourt la collection filtrée pour extraire les secteurs (en ignorant le Total global)
        for d in data.DonneEnergie:
            if d.secteur != "Total":
                noms_secteurs.append(d.secteur)
                valeurs_conso.append(d.consommation)
        plt.figure(figsize=(10, 6))
        # Couleurs variées pour distinguer les secteurs
        couleurs = ['#2ecc71', '#e74c3c', '#3498db', '#f39c12', '#95a5a6']
        plt.bar(noms_secteurs, valeurs_conso, color=couleurs)
        plt.title(f"Répartition par secteur - Dépt {num_dept} en {annee}")
        plt.ylabel("Consommation (MWh)")
        plt.show()

    def repartition_elec_gaz(self, collection, num_dept):
        """
        FONCTIONNALITÉ 4 : Analyse de la répartition Élec / Gaz (Histogramme empilé).
        """
        # On prend les totaux du département
        data_dept = collection.filtre_departement(num_dept).filtre_secteur("Total")
        # Récupération des années uniques présentes
        tous_ans = sorted(list(set(data_dept.annee())))
        valeurs_elec = []
        valeurs_gaz = []
        # Pour chaque année, on cherche la valeur correspondante
        for a in tous_ans:
            e_val = 0
            g_val = 0
            for obj in data_dept.DonneEnergie:
                if obj.annee == a:
                    if obj.energie == "Electricité": e_val = obj.consommation
                    if obj.energie == "Gaz": g_val = obj.consommation
            valeurs_elec.append(e_val)
            valeurs_gaz.append(g_val)
        plt.figure(figsize=(10, 5))
        # Histogramme empilé : le gaz commence là où l'élec s'arrête (bottom=valeurs_elec)
        plt.bar(tous_ans, valeurs_elec, label='Électricité', color='gold')
        plt.bar(tous_ans, valeurs_gaz, bottom=valeurs_elec, label='Gaz', color='chocolate')   
        plt.title(f"Répartition Électricité vs Gaz - Département {num_dept}")
        plt.xlabel("Années")
        plt.ylabel("Consommation (MWh)")
        plt.legend()
        plt.show()

    def projection_2030(self, collection, nom_region, annee_cible, secteur, energie):
        """
        FONCTIONNALITÉ 5 : Projection linéaire basée sur le taux d'évolution moyen.
        """
        # Préparation des données historiques
        data = collection.filtre_region(nom_region).filtre_secteur(secteur).filtre_energie(energie)
        data.sort()
        if len(data.DonneEnergie) < 2:
            print("Erreur : Pas assez de données historiques pour projeter.")
            return
        # Calcul selon les formules du sujet
        v_initiale = data.DonneEnergie[0].consommation
        v_finale = data.DonneEnergie[-1].consommation
        n = float(data.DonneEnergie[-1].annee) - float(data.DonneEnergie[0].annee)
        # Taux moyen tm = (vf/vi)^(1/n) - 1
        tm = (v_finale / v_initiale)**(1/n) - 1
        # Nombre d'années entre la dernière connue et la cible
        nb_ans_restants = annee_cible - float(data.DonneEnergie[-1].annee)
        # Prediction = vf * (1 + tm)^nb_ans
        prediction = v_finale * (1 + tm)**nb_ans_restants 
        print(f"--- RÉSULTATS PROJECTION {nom_region} ---")
        print(f"Secteur : {secteur} | Énergie : {energie}")
        print(f"Taux d'évolution moyen calculé : {tm*100:.2f} % par an")
        print(f"Estimation pour l'année {annee_cible} : {prediction:.2f} MWh")
