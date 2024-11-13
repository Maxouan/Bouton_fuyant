import tkinter as tk
import webbrowser  # Pour ouvrir l'URL dans le navigateur

# Fonction qui éloigne le bouton lorsque la souris s'en rapproche
def eloigner_bouton(event):
    # Récupérer la position de la souris
    souris_x = event.x
    souris_y = event.y
    
    # Récupérer la position actuelle du bouton
    bouton_x = bouton.winfo_x()
    bouton_y = bouton.winfo_y()
    
    # Calculer la distance entre le curseur et le bouton
    distance = ((souris_x - bouton_x) ** 2 + (souris_y - bouton_y) ** 2) ** 0.5
    
    # Si la distance est inférieure à 100 pixels, éloigner le bouton
    if distance < 75:
        # Calculer un nouvel emplacement pour éloigner le bouton
        direction_x = 5 if souris_x < bouton_x else -5
        direction_y = 5 if souris_y < bouton_y else -5
        new_x = bouton_x + direction_x
        new_y = bouton_y + direction_y

        # Vérification si le bouton touche un bord de la fenêtre
        if new_x < 0 or new_x > 1850:  # 1850 est la limite droite (1900 - 50 pour la largeur du bouton)
            new_x = 950  # Revenir au centre horizontal
        if new_y < 0 or new_y > 850:  # 850 est la limite basse (900 - 50 pour la hauteur du bouton)
            new_y = 450  # Revenir au centre vertical

        bouton.place(x=new_x, y=new_y)

# Fonction qui affiche la fenêtre "BRAVO CHAMPION" avec texte clignotant
def afficher_fenetre_felicitation():
    # Création de la fenêtre de félicitations
    fenetre_felicitation = tk.Toplevel(fenetre)  # Fenêtre secondaire
    fenetre_felicitation.title("Félicitations")
    fenetre_felicitation.geometry("400x200")

    # Label avec texte clignotant
    label_felicitation = tk.Label(fenetre_felicitation, text="BRAVO CHAMPION", font=("Helvetica", 24), fg="red")
    label_felicitation.pack(expand=True)

    # Fonction pour faire clignoter le texte
    def clignoter():
        current_fg = label_felicitation.cget("fg")
        new_fg = "red" if current_fg == "black" else "black"
        label_felicitation.config(fg=new_fg)
        # Appel récursif pour clignoter toutes les 500 ms
        fenetre_felicitation.after(500, clignoter)

    # Démarrer le clignotement
    clignoter()

# Fonction qui ouvre la page YouTube
def ouvrir_video():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Fenêtre avec bouton fuyant")
fenetre.geometry("1900x900")  # Taille de la fenêtre

# Création du bouton "Cliquez ici"
bouton = tk.Button(fenetre, text="Cliquez ici", command=afficher_fenetre_felicitation)
bouton.place(x=950, y=450)  # Initialement au centre de la fenêtre

# Création du bouton "Je suis nul" en haut à gauche
button_nul = tk.Button(fenetre, text="Je suis nul", command=ouvrir_video)
button_nul.place(x=10, y=10)  # Position en haut à gauche (marge de 10 pixels)

# Événement qui capte la position de la souris
fenetre.bind("<Motion>", eloigner_bouton)

# Lancement de la boucle principale de l'interface graphique
fenetre.mainloop()
