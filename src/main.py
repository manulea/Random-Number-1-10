import tkinter as tk
import random
import pygame
import os
from gui.app import App

def main():
    try:
        pygame.mixer.init()
        root = tk.Tk()
        app = App(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()