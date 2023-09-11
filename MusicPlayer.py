import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        
        pygame.init()
        pygame.mixer.init()
        
        self.playlist = []
        
        self.label = tk.Label(root, text="Music Player", font=("Helvetica", 20))
        self.label.pack(pady=10)
        
        self.playlistbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.playlistbox.pack(padx=20, pady=20)
        
        button_width = 10  # Adjust the width for the buttons
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(padx=20)
        
        self.add_button = self.create_button(self.button_frame, "Add Song", button_width, self.add_song)
        self.play_button = self.create_button(self.button_frame, "Play", button_width, self.play_song)
        self.stop_button = self.create_button(self.button_frame, "Stop", button_width, self.stop_song)
        
    def create_button(self, frame, text, width, command):
        button = tk.Button(frame, text=text, width=width, command=command)
        button.pack(side=tk.LEFT, padx=5)
        button.bind("<Enter>", lambda event, b=button: self.on_enter(event, b))
        button.bind("<Leave>", lambda event, b=button: self.on_leave(event, b))
        return button
        
    def on_enter(self, event, button):
        button.config(bg="lightgreen")
        
    def on_leave(self, event, button):
        button.config(bg="SystemButtonFace")
    
    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if song_path:
            self.playlist.append(song_path)
            song_name = song_path.split("/")[-1]
            self.playlistbox.insert(tk.END, song_name)
    
    def play_song(self):
        selected_song = self.playlistbox.curselection()
        if selected_song:
            song_index = selected_song[0]
            song_path = self.playlist[song_index]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
    
    def stop_song(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()