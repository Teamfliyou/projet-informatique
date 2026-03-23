#=============================================================================================================
# -*- coding: utf-8 -*-
#  Zayd Fliyou, Teo Dubar 
#=============================================================================================================
class ClasseDonneeEnergie:
    def __init__(self, ligne_secteur, nom_secteur, nom_energie="Total"):
        """
        Initialise un objet representant une ligne de consommation.
        Entrees:
            - ligne_secteur (list): Une ligne de 6 colonnes (5 base + 1 conso)
            - nom_secteur (str): Nom du secteur (ex: Agriculture)
            - nom_energie (str): Type d'energie (par defaut "Total")
        
        """
        self.annee = ligne_secteur[0]
        self.id_dept = ligne_secteur[1]
        self.dept = ligne_secteur[2]
        self.id_region = ligne_secteur[3]
        self.region = ligne_secteur[4]
        
        self.secteur = nom_secteur
        self.energie = nom_energie
        
        
        # Source : Gestion des exceptions (Try/Except) Documentation Python
        try:
            # On tente de convertir la 6eme colonne en nombre decimal
            self.consommation = float(ligne_secteur[5])
        except ValueError:
            # Si la conversion echoue (case vide ou texte), on met 0.0
            self.consommation = 0.0

    def __str__(self):
        """
        Cree une chaine de caracteres pour l'affichage (print).
        Sortie: str (formatte selon la consigne)
        
        """
        return f"{self.annee} : {self.dept} ({self.id_dept}) en {self.region} | {self.secteur} : {self.consommation} MWh ({self.energie})"

    def __lt__(self, autre):
        """
        Definit les regles de tri (comparaison "plus petit que").
        Tri par: 1. Annee, 2. ID Departement, 3. Secteur
        )
        """
        # Comparaison par annee
        if self.annee != autre.annee:
            return self.annee < autre.annee
        
        # Si annee identique, comparaison par departement
        if self.id_dept != autre.id_dept:
            return self.id_dept < autre.id_dept
            
        # Sinon, comparaison par secteur (ordre alphabetique)
        return self.secteur < autre.secteur