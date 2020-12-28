import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

# Creating interface for the PLayer
music_player = tkr.Tk()
# Name of Music Player
music_player.title('Ankush Chutiya Hai!')
# Setting Music Player GUI dimensions
music_player.geometry('450x350')

# Creating a directory that prompts user to choose the folder location of music
directory = askdirectory()
# change the current directory to user defined directory
os.chdir(directory)
# returns a list of songs in the folder
song_list = os.listdir()

# Creating a playlist out of the given folder items and displaying an interface
play_list = tkr.Listbox(music_player, font='Helverica 12 bold', bg='yellow', selectmode=tkr.SINGLE)

# For loop to select every song and add in the playing Queue
for var in song_list:
    pos=0
    play_list.insert(pos,var)
    pos+=1

# loading Pygame Mixer
pygame.init()
pygame.mixer.init()

# Functions to control media

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var1.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    
def stop():
    pygame.mixer.music.stop()
    
def pause():
    pygame.mixer.music.pause()
    
def unpause():
    pygame.mixer.music.unpause()
    
# Creating GUI Buttons to control media

Button1 = tkr.Button(music_player,width=5,height=3, font='Helvetica 12 bold', text='PLAY', command=play, bg='blue',fg='white')
Button2 = tkr.Button(music_player,width=5,height=3,font='Helvetica 12 bold', text='STOP', command=stop, bg='red', fg='white')
Button3 = tkr.Button(music_player,width=5,height=3,font='Helvetica 12 bold', text='PAUSE', command=pause, bg='purple', fg='white')
Button4 = tkr.Button(music_player,width=5,height=3,font='Helvetica 12 bold', text='UNPAUSE', command=unpause, bg='orange', fg='white')

# Creating a variable to see current playing over the music player
var1 = tkr.StringVar()
song_title = tkr.Label(music_player, font='Helvetica 12 bold', textvariable=var1)

# Packing and arranging buttons on music player
song_title.pack()
Button1.pack(fill='x')
Button2.pack(fill='x')
Button3.pack(fill='x')
Button4.pack(fill='x')
play_list.pack(fill='both',expand='yes')

music_player.mainloop()