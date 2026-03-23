# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import matplotlib
matplotlib.use('TkAgg') # Indispensable pour l'intégration Tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Import de tes classes
from classe.DonneeEnergie import ClasseDonneeEnergie
from classe.CollectionEnergie import CollectionEnergie
from classe.Reporting import Reporting

# =============================================================================
# CHARGEMENT DES DONNÉES
# =============================================================================
ma_base = CollectionEnergie()
visu = Reporting()

def charger_base():
    path = "data/conso_nettoyee.csv"
    try:
        with open(path, 'r', encoding='utf-8-sig') as f:
            lecteur = csv.reader(f, delimiter=';')
            data = list(lecteur)
            for ligne in data[1:]:
                infos = ligne[0:5]
                secteurs = ["Agriculture", "Industrie", "Résidentiel", "Tertiaire", "Autre"]
                energies = [("Total", 5), ("Electricité", 10), ("Gaz", 15)]
                for nom_e, idx in energies:
                    for i in range(5):
                        val = float(ligne[idx+i]) if ligne[idx+i] else 0.0
                        ma_base.ajouter(ClasseDonneeEnergie(infos + [val], secteurs[i], nom_e))
        return True
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur de fichier : {e}")
        return False

# =============================================================================
# CLASSE DE L'INTERFACE GRAPHIQUE
# =============================================================================
class EnergyDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("ENERGY ANALYTICS - PRO")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1a1a2e") # Bleu très sombre

        self.canvas = None
        self.toolbar = None
        
        self.setup_ui()

    def setup_ui(self):
        # 1. BARRE LATERALE (CONTROLES)
        sidebar = tk.Frame(self.root, width=300, bg="#16213e", padx=20, pady=20)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(sidebar, text="DASHBOARD", font=("Helvetica", 18, "bold"), fg="#e94560", bg="#16213e").pack(pady=(0, 30))

        # --- FILTRES ---
        self.create_label(sidebar, "Département Principal")
        self.cb_dept = self.create_combo(sidebar, [str(i)+".0" for i in range(1, 100)], "62.0")

        self.create_label(sidebar, "Département Comparaison")
        self.cb_dept2 = self.create_combo(sidebar, [str(i)+".0" for i in range(1, 100)], "59.0")

        self.create_label(sidebar, "Année")
        self.cb_annee = self.create_combo(sidebar, [str(float(i)) for i in range(2012, 2023)], "2020.0")

        self.create_label(sidebar, "Secteur")
        self.cb_secteur = self.create_combo(sidebar, ["Agriculture", "Industrie", "Résidentiel", "Tertiaire", "Autre"], "Industrie")

        # --- BOUTONS D'ANALYSES ---
        tk.Label(sidebar, text="ANALYSES", font=("Helvetica", 10, "bold"), fg="#95a5a6", bg="#16213e").pack(pady=(30, 10))
        
        btns = [
            ("📈 Évolution Temporelle", self.plot_evolution, "#0f3460"),
            ("👥 Comparer 2 Depts", self.plot_comp_depts, "#0f3460"),
            ("📊 Répartition Secteurs", self.plot_secteurs, "#0f3460"),
            ("🔋 Mix Énergétique", self.plot_mix, "#0f3460"),
            ("🌍 Vue Régionale", self.plot_regions, "#0f3460"),
            ("🔮 Projection 2050", self.plot_projection, "#e94560")
        ]

        for txt, cmd, color in btns:
            tk.Button(sidebar, text=txt, command=cmd, bg=color, fg="white", bd=0, 
                      height=2, cursor="hand2", font=("Helvetica", 9, "bold")).pack(fill=tk.X, pady=4)

        tk.Button(sidebar, text="QUITTER", command=self.root.quit, bg="#1a1a2e", fg="#95a5a6", bd=0).pack(side=tk.BOTTOM, fill=tk.X)

        # 2. ZONE PRINCIPALE (AFFICHAGE)
        self.main_frame = tk.Frame(self.root, bg="#1a1a2e", padx=20, pady=20)
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.fig_container = tk.Frame(self.main_frame, bg="#16213e", bd=0)
        self.fig_container.pack(fill=tk.BOTH, expand=True)

    def create_label(self, master, txt):
        tk.Label(master, text=txt, fg="white", bg="#16213e", font=("Helvetica", 9)).pack(anchor="w", pady=(10, 0))

    def create_combo(self, master, vals, default):
        c = ttk.Combobox(master, values=vals, state="readonly")
        c.set(default)
        c.pack(fill=tk.X, pady=5)
        return c

    def display(self, fig):
        if self.canvas: self.canvas.get_tk_widget().destroy()
        if self.toolbar: self.toolbar.destroy()

        fig.patch.set_facecolor('#16213e') # Match avec le fond
        self.canvas = FigureCanvasTkAgg(fig, master=self.fig_container)
        self.canvas.draw()
        
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.fig_container)
        self.toolbar.config(background="#16213e")
        self.toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # --- MÉTHODES DE DESSIN ---
    def plot_evolution(self):
        plt.close('all')
        fig, ax = plt.subplots(figsize=(8, 5))
        d, s = self.cb_dept.get(), self.cb_secteur.get()
        data = ma_base.filtre_departement(d).filtre_secteur(s).filtre_energie("Electricité")
        data.sort()
        ax.plot(data.annee(), data.consomation(), color='#e94560', marker='o', linewidth=3)
        self.style_graph(ax, f"Évolution {s} - Dept {d}", "MWh")
        self.display(fig)

    def plot_secteurs(self):
        plt.close('all')
        fig, ax = plt.subplots(figsize=(8, 5))
        d, a = self.cb_dept.get(), self.cb_annee.get()
        data = ma_base.filtre_departement(d).filtre_annee(a).filtre_energie("Total")
        noms, vals = [], []
        for o in data.DonneEnergie:
            if o.secteur != "Total":
                noms.append(o.secteur); vals.append(o.consommation)
        ax.bar(noms, vals, color=['#e94560', '#0f3460', '#533483', '#3282b8', '#bbe1fa'])
        self.style_graph(ax, f"Répartition par Secteur ({a})", "MWh")
        self.display(fig)

    def plot_mix(self):
        plt.close('all')
        fig, ax = plt.subplots(figsize=(8, 5))
        d = self.cb_dept.get()
        data = ma_base.filtre_departement(d).filtre_secteur("Total")
        ans = sorted(list(set(data.annee())))
        e_v = [sum(o.consommation for o in data.DonneEnergie if o.annee == a and o.energie == "Electricité") for a in ans]
        g_v = [sum(o.consommation for o in data.DonneEnergie if o.annee == a and o.energie == "Gaz") for a in ans]
        ax.bar(ans, e_v, label='Élec', color='#0f3460')
        ax.bar(ans, g_v, bottom=e_v, label='Gaz', color='#e94560')
        ax.legend()
        self.style_graph(ax, f"Mix Énergétique - Dept {d}", "MWh")
        self.display(fig)

    def plot_comp_depts(self):
        plt.close('all')
        fig, ax = plt.subplots(figsize=(8, 5))
        d1, d2 = self.cb_dept.get(), self.cb_dept2.get()
        c1 = ma_base.filtre_departement(d1).filtre_secteur("Agriculture").filtre_energie("Total")
        c2 = ma_base.filtre_departement(d2).filtre_secteur("Agriculture").filtre_energie("Total")
        c1.sort(); c2.sort()
        ax.scatter(c1.annee(), c1.consomation(), color='#e94560', s=100, label=f"Dept {d1}")
        ax.scatter(c2.annee(), c2.consomation(), color='#3282b8', s=100, label=f"Dept {d2}")
        ax.legend()
        self.style_graph(ax, "Comparaison Agriculture", "MWh")
        self.display(fig)

    def plot_regions(self):
        plt.close('all')
        fig, ax = plt.subplots(figsize=(8, 6))
        a = self.cb_annee.get()
        data = ma_base.filtre_annee(a).filtre_secteur("Résidentiel").filtre_energie("Electricité")
        regs = {}
        for o in data.DonneEnergie: regs[o.region] = regs.get(o.region, 0) + o.consommation
        ax.barh(list(regs.keys()), list(regs.values()), color='#533483')
        plt.tight_layout()
        self.style_graph(ax, f"Consommation par Région ({a})", "MWh")
        self.display(fig)

    def plot_projection(self):
        d = self.cb_dept.get()
        reg_nom = ma_base.filtre_departement(d).DonneEnergie[0].region
        visu.projection_2030(ma_base, reg_nom, 2050, "Industrie", "Electricité")
        messagebox.showinfo("Projection 2050", f"Estimation effectuée pour : {reg_nom}\nRésultats détaillés dans la console.")

    def style_graph(self, ax, title, ylabel):
        ax.set_title(title, color='white', pad=15)
        ax.set_ylabel(ylabel, color='white')
        ax.set_facecolor('#16213e')
        ax.tick_params(colors='white')
        for s in ax.spines.values(): s.set_color('#533483')
        ax.grid(True, linestyle='--', alpha=0.2)

# --- EXECUTION ---
if charger_base():
    root = tk.Tk()
    app = EnergyDashboard(root)
    root.mainloop()