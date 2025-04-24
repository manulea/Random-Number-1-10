import tkinter as tk
import random
import pygame
import os
import json

class App:
    def __init__(self, master):
        self.master = master

        # Load layout configuration from JSON
        try:
            with open(os.path.join(os.path.dirname(__file__), "layout.json"), "r") as f:
                config = json.load(f)
                print("Loaded layout.json successfully.")  # Debugging line
        except FileNotFoundError:
            print("Error: layout.json file not found!")
            return
        except json.JSONDecodeError:
            print("Error: layout.json file is not valid JSON!")
            return

        # Configure the main window
        master.title(config["window"]["title"])
        master.configure(bg=config["window"]["background"])

        # Initialize pygame mixer
        pygame.mixer.init()
        if not pygame.mixer.get_init():
            print("Pygame mixer failed to initialize!")

        # Create a frame to hold the buttons
        button_frame = tk.Frame(master, bg=config["window"]["background"])
        button_frame.pack(pady=20)

        # Create buttons dynamically from JSON
        for i, button_config in enumerate(config["buttons"]):
            print(f"Creating button: {button_config['text']} with command: {button_config['command']}")
            if button_config["command"] == "play_audio":
                command = lambda num=i + 1: self.play_audio(num)  # Use default argument to capture `i`
            else:
                command = self.play_random_audio
            button = tk.Button(
                button_frame,
                text=button_config["text"],
                command=command,
                width=button_config["width"],
                height=button_config["height"],
                bg=button_config["bg"],
                fg=button_config["fg"],
                relief=button_config["relief"]
            )
            button.grid(row=i // 5, column=i % 5, padx=5, pady=5)

        # Handle window close event
        master.protocol("WM_DELETE_WINDOW", self.on_close)

        self.play_audio(1)  # Test with number 1

    def play_audio(self, number):
        """Play the audio file corresponding to the given number."""
        audio_file = f"{number}.wav"
        audio_path = os.path.join(os.path.dirname(__file__), "..", "assets", "audio", audio_file)
        audio_path = os.path.abspath(audio_path)
        print(f"Button pressed: {number}, attempting to play: {audio_path}")  # Debugging line
        if not os.path.exists(audio_path):
            print(f"Error: File does not exist at {audio_path}")
            return
        try:
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
            print(f"Playing: {audio_path}")
        except pygame.error as e:
            print(f"Error playing audio: {e}")

    def play_random_audio(self):
        """Play a random audio file."""
        random_number = random.randint(1, 10)
        print(f"Random button pressed, playing number: {random_number}")
        self.play_audio(random_number)

    def on_close(self):
        """Handle application close."""
        pygame.mixer.quit()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()