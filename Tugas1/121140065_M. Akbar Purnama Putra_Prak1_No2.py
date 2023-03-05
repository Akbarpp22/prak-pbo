# Nama : M. Akbar Purnama Putra
# NIM  : 121140065
# Kelas: RB
# Latihan No 2

username = "informatika"
password = "12345678"
attempt = 0

while attempt < 3:
    username_input = input("Masukkan username: ")
    password_input = input("Masukkan password: ")
    if username_input == username and password_input == password:
        print("Berhasil login!")
        break
    else:
        print("Username atau password salah. Silakan coba lagi.")
        attempt += 1

if attempt >= 3:
    print("Percobaan login lebih dari 3 kali. Akun diblokir.")



