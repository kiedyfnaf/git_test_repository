import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from mutagen.mp3 import MP3
from tkinter.font import Font
import pygame
import time
import threading
import os
import random
from tkinter import ttk

# Initialize pygame mixer
pygame.mixer.init()

# Store the current position of the music
current_position = 0
paused = False
playlist = []
selected_folder_path = ""  # Store the selected folder path

def update_progress():
    global current_position
    while True:
        if pygame.mixer.music.get_busy() and not paused:
            current_position = pygame.mixer.music.get_pos() / 1000
            pbar["value"] = current_position

            # Check if the current song has reached its maximum duration
            if current_position >= pbar["maximum"]:
                play_next_song()

            window.update_idletasks()  # Update the GUI without blocking
        time.sleep(0.1)

def play_next_song():
    next_index = (lbox.curselection()[0] + 1) % lbox.size()  # Get the index of the next song in the playlist
    lbox.selection_clear(0, tk.END)
    lbox.selection_set(next_index)
    play_selected_song()

# Create a thread to update the progress bar
pt = threading.Thread(target=update_progress)
pt.daemon = True
pt.start()

# Rest of your code remains the same...


def select_music_folder():
    global selected_folder_path
    selected_folder_path = filedialog.askdirectory()
    if selected_folder_path:
        update_playlist()

def update_playlist():
    global playlist
    playlist = []
    if selected_folder_path:
        lbox.delete(0, tk.END)
        for filename in os.listdir(selected_folder_path):
            if filename.endswith(".mp3"):
                playlist.append(os.path.join(selected_folder_path, filename))
                lbox.insert(tk.END, filename)  # Insert only the filename, not the full path

def previous_song():
    pause_music()
    pbar["value"] = 0
    if len(lbox.curselection()) > 0:
        current_index = lbox.curselection()[0]
        if current_index > 0:
            time.sleep(1)
            lbox.selection_clear(0, tk.END)
            lbox.selection_set(current_index - 1)
            play_selected_song()

def next_song():
    pause_music()
    pbar["value"] = 0
    if len(lbox.curselection()) > 0:
        current_index = lbox.curselection()[0]
        if current_index < lbox.size() - 1:
            time.sleep(1)
            lbox.selection_clear(0, tk.END)
            lbox.selection_set(current_index + 1)
            play_selected_song()

def shuffle_playlist():
    global playlist
    random.shuffle(playlist)
    lbox.delete(0, tk.END)
    for filename in playlist:
        lbox.insert(tk.END, os.path.basename(filename))  # Insert only the filename

def play_music():
    global paused
    if paused:
        # If the music is paused, unpause it
        pygame.mixer.music.unpause()
        paused = False
    else:
        # If the music is not paused, play the selected song
        play_selected_song()

def play_selected_song():
    global current_position, paused
    if len(lbox.curselection()) > 0:
        current_index = lbox.curselection()[0]
        selected_song = lbox.get(current_index)
        full_path = os.path.join(selected_folder_path, selected_song)  # Add the full path again
        pygame.mixer.music.load(full_path)  # Load the selected song
        current_position = 0  # Set current position to 0
        pygame.mixer.music.play(start=current_position)  # Play the song from the beginning
        paused = False
        audio = MP3(full_path)
        song_duration = audio.info.length
        pbar["maximum"] = song_duration - 1

def change_volume(value):
    global volume
    volume = float(value) / 100  # Convert the value to a float between 0 and 1
    pygame.mixer.music.set_volume(volume)

def pause_music():
    global paused
    # Pause the currently playing music
    pygame.mixer.music.pause()
    paused = True

def stop_music():
    global paused
    # Stop the currently playing music and reset the progress bar
    pygame.mixer.music.stop()
    paused = False

# Create the main window
window = tk.Tk()
window.title("Music Player App")
window.geometry("350x330")
window['background'] = '#05ce8a'
fun = Font(
    family="Lucida Calligraphy",
    size=19,
    slant="roman"
)

# Create a label for the music player title
l_music_player = tk.Label(window, text="Music Player", font=fun, foreground='black')
l_music_player.pack(pady=(10, 0))

# Create a button to select the music folder
btn_select_folder = tk.Button(window, text="Select Music Folder", command=select_music_folder, font=("TkDefaultFont", 10),
                                foreground='black')
btn_select_folder.pack(pady=(0, 5))

# Create a listbox to display the available songs
lbox = tk.Listbox(window, width=50, height=10, font=("TkDefaultFont", 8), foreground='black')
lbox.pack()

# Create a frame to hold the control buttons
btn_frame = tk.Frame(window)
btn_frame.pack(pady=0)

# Create a button to go to the previous song
btn_previous = tk.Button(btn_frame, text="<", command=previous_song, font=("TkDefaultFont", 10),
                         background='#FF69B4', foreground='black')
btn_previous.grid(row=0, column=0, padx=(0, 2))

# Create a button to play the music
btn_play = tk.Button(btn_frame, text="Play", command=play_music, font=("TkDefaultFont", 8),
                     background='#FF69B4', foreground='black')
btn_play.grid(row=0, column=1, padx=2)

# Create a button to volume
btn_volume = tk.Button(btn_frame, text="All", command=play_music, font=("TkDefaultFont", 8),
                       background='#FF69B4', foreground='black')
volume_scale = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=change_volume,
                        font=("TkDefaultFont", 8), background='#FF69B4')
volume_scale.set(50)  # Set the initial volume level to 50%
volume_scale.pack(pady=(0, 0))
btn_volume.grid(row=0, column=2, padx=2)

# Create a button to pause the music
btn_pause = tk.Button(btn_frame, text="Pause", command=pause_music, font=("TkDefaultFont", 8),
                      background='#FF69B4', foreground='black')
btn_pause.grid(row=0, column=4, padx=2)

# Create a button to go to the next song
btn_next = tk.Button(btn_frame, text=">", command=next_song, font=("TkDefaultFont", 10),
                     background='#FF69B4', foreground='black')
btn_next.grid(row=0, column=5, padx=(2, 0))

# Create a button to go to shuffle
btn_next = tk.Button(btn_frame, text="Shuffle", command=shuffle_playlist, font=("TkDefaultFont", 8),
                     background='#FF69B4', foreground='black')
btn_next.grid(row=0, column=3, padx=(2, 0))

# Create a progress bar to indicate the current song's progress
style = ttk.Style()
style.theme_use("default")
style.configure("Custom.Horizontal.TProgressbar", background="blue")

pbar = ttk.Progressbar(window, length=200, mode="determinate", style="Custom.Horizontal.TProgressbar")
pbar.pack(pady=0)

window.mainloop()