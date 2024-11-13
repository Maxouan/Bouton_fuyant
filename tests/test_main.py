import pytest
import tkinter as tk
from tkinter import Tk
import eloigner_bouton

def test_eloigner_bouton():
    fenetre = Tk()
    fenetre.geometry("1900x900")
    
    bouton = tk.Button(fenetre, text="Cliquez ici")
    bouton.place(x=950, y=450)
    
    event = type('test', (object,), {'x': 960, 'y': 460})()  # Événement fictif

    eloigner_bouton(event)
    
    new_x = bouton.winfo_x()
    new_y = bouton.winfo_y()
    
    assert new_x != 950 or new_y != 450  # Le bouton devrait avoir bougé
