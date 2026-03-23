# -*- coding: utf-8 -*-
"""
@author: zayd Fliyou & Teo Dubar 
"""


class CollectionEnergie: 
    def __init__(self):
        # On initialise une liste vide qui contiendra des objets ClasseDonneeEnergie
        self.DonneEnergie = []
        
    def ajouter(self, une_donnee):
        """
        Ajoute un objet ClasseDonneeEnergie déjà créé à la collection.
        """
        self.DonneEnergie.append(une_donnee)

    def __str__(self):
        """
        Représente la collection sous forme de texte (un objet par ligne).
        """
        text_final = ""
        for donnee in self.DonneEnergie:
            text_final += f"{donnee}\n" 
        return text_final
    
    def __len__(self):
        """ Retourne le nombre d'entrées dans la collection """
        return len(self.DonneEnergie)
    
    def sort(self):
        """ Trie la collection en utilisant le __lt__ de la classe DonneeEnergie """
        self.DonneEnergie.sort()

    def departement(self):
        """ Retourne la liste des noms de départements """
        liste_departement = []
        for donnee in self.DonneEnergie:
            liste_departement.append(donnee.dept)
        return liste_departement
    
    def annee(self):
        """ Retourne la liste des années """
        liste_annee = []
        for donnee in self.DonneEnergie:
            liste_annee.append(donnee.annee)
        return liste_annee
    
    def consomation(self):
        """ Retourne la liste des consommations """
        liste_consomation = []
        for donnee in self.DonneEnergie:
            
            liste_consomation.append(donnee.consommation)
        return liste_consomation

    # --- PARTIE FILTRES (Renvoient une NOUVELLE CollectionEnergie) ---

    def filtre_departement(self, num_dept):
        resultat = CollectionEnergie() # On crée une nouvelle collection
        for d in self.DonneEnergie:
            if d.id_dept == num_dept:
                resultat.ajouter(d)
        return resultat

    def filtre_region(self, nom_region):
        resultat = CollectionEnergie()
        for d in self.DonneEnergie:
            if d.region == nom_region:
                resultat.ajouter(d)
        return resultat

    def filtre_annee(self, num_annee):
        resultat = CollectionEnergie()
        for d in self.DonneEnergie:
            if d.annee == num_annee:
                resultat.ajouter(d)
        return resultat

    def filtre_energie(self, libelle_energie):
        resultat = CollectionEnergie()
        for d in self.DonneEnergie:
            if d.energie == libelle_energie:
                resultat.ajouter(d)
        return resultat

    def filtre_secteur(self, libelle_secteur):
        resultat = CollectionEnergie()
        for d in self.DonneEnergie:
            if d.secteur == libelle_secteur:
                resultat.ajouter(d)
        return resultat