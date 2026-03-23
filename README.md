# Projet-informatique-cp1-EIlco-
📋 Présentation du Projet
L'application se concentre sur la consommation annuelle de gaz et d'électricité par département et par secteur. Elle utilise le fichier source officiel conso-departement-annuelle.csv.


Cadre : Cycle Préparatoire Intégré 1ère année - Dunkerque.


Enseignant : B. Fortin.


Auteurs : Zayd FLiyou & Teo Dubar.

🛠️ Prérequis et Bibliothèques
Pour fonctionner, ce programme nécessite Python 3.x et la bibliothèque de visualisation suivante :


Matplotlib : Utilisée pour générer les graphiques d'analyse (comparaisons, projections).

💻 Installation par Éditeur
Selon l'outil que vous utilisez, voici comment préparer votre environnement :

🔹 Visual Studio Code (VS Code)
Ouvrez un terminal intégré (Ctrl + Shift + ù).

Tapez la commande : pip install matplotlib.

🔹 PyCharm
Allez dans File > Settings > Project > Python Interpreter.

Cliquez sur le bouton + et cherchez matplotlib.

Cliquez sur Install Package.

🔹 Thonny / EduPython
Allez dans le menu Outils > Gérer les paquets.

Recherchez matplotlib et cliquez sur Installer.

🏗️ Architecture Logicielle
Le projet repose sur la Programmation Orientée Objet (POO)  avec la structure de classes suivante :


DonneeEnergie : Modélise une ligne de consommation spécifique.


Collection : Gère l'ensemble des données et les algorithmes de filtrage.

📂 Structure des fichiers

main.py : Point d'entrée de l'application.


/data : Contient le fichier conso-departement-annuelle.csv.

/src : Contient les modules Python et les classes.

README.md : Guide d'utilisation et présentation.

.gitignore : Pour exclure les fichiers inutiles (cache, venv).

🚀 Utilisation
Installez la librairie matplotlib.

Placez le fichier CSV dans le dossier data.

Lancez le script principal avec la commande :

⚖️ Licence
Ce projet est distribué sous la Licence MIT – vous êtes libre de l'utiliser et de le modifier.
