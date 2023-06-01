# Nama  : M. Akbar Purnama Putra
# NIM   : 121140065

import tkinter as tk
from tkinter import messagebox
import random

# Fungsi untuk memilih pilihan acak komputer
def get_computer_choice():
    choices = ["Gunting", "Batu", "Kertas"]
    return random.choice(choices)

# Fungsi untuk membandingkan pilihan pemain dan komputer
def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Seri"
    elif (
        (player_choice == "Gunting" and computer_choice == "Kertas")
        or (player_choice == "Batu" and computer_choice == "Gunting")
        or (player_choice == "Kertas" and computer_choice == "Batu")
    ):
        return "Pemain Menang"
    else:
        return "Komputer Menang"

# Fungsi untuk menampilkan hasil permainan
def show_result(player_choice, computer_choice, result):
    messagebox.showinfo("Hasil", f"Pemain: {player_choice}\nKomputer: {computer_choice}\n\n{result}")

# Fungsi untuk menghandle klik tombol
def play():
    player_choice = choice.get()
    computer_choice = get_computer_choice()
    result = get_winner(player_choice, computer_choice)
    show_result(player_choice, computer_choice, result)

# Membuat GUI
window = tk.Tk()
window.title("Gunting Batu Kertas")

# Membuat label instruksi
label = tk.Label(window, text="Pilih pilihan Anda:")
label.pack()

# Membuat variabel untuk memilih pilihan
choice = tk.StringVar()

# Membuat radio button untuk pilihan
scissors_button = tk.Radiobutton(window, text="Gunting", variable=choice, value="Gunting")
scissors_button.pack()

rock_button = tk.Radiobutton(window, text="Batu", variable=choice, value="Batu")
rock_button.pack()

paper_button = tk.Radiobutton(window, text="Kertas", variable=choice, value="Kertas")
paper_button.pack()

# Membuat tombol untuk memulai permainan
play_button = tk.Button(window, text="Main", command=play)
play_button.pack()

# Menjalankan event loop utama
window.mainloop()
