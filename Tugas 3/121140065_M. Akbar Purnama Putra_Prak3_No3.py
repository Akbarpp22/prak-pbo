# Nama  : M. Akbar Purnama Putra
# NIM   : 121140065
# Tugas : 3
# No    : 3

class Mobil:
    # Atribut kelas public
    tahun_produksi = 2003
    
    def __init__(self, merk, model, warna):
        # Atribut instance private
        self.__merk = merk
        # Atribut instance protected
        self._model = model
        # Atribut instance public
        self.warna = warna
        
    # Fungsi instance private
    def __ubah_merk(self, merk_baru):
        self.__merk = merk_baru
        
    # Fungsi instance protected
    def _ubah_model(self, model_baru):
        self._model = model_baru
        
    # Fungsi instance public
    def ubah_warna(self, warna_baru):
        self.warna = warna_baru
        
    def info(self):
        print("Mobil ini adalah {} {} tahun {}, dengan warna {}."
              .format(self.__merk, self._model, Mobil.tahun_produksi, self.warna))

# Membuat objek mobil
mobil_saya = Mobil("Jeep", "Fortuner", "Putih")

# Mengakses atribut kelas public
print("Tahun produksi mobil:", Mobil.tahun_produksi)

# Mengakses atribut instance public
print("Warna mobil:", mobil_saya.warna)

# Mengakses atribut instance private
# Akan menghasilkan error karena atribut private tidak bisa diakses dari luar kelas
# print("Merk mobil:", mobil_saya.__merk)

# Mengakses atribut instance protected
# Bisa diakses, tetapi tidak disarankan karena bisa mengganggu enkapsulasi
print("Model mobil:", mobil_saya._model)

# Memanggil fungsi instance public
mobil_saya.ubah_warna("Hitam")

# Memanggil fungsi instance private
# Akan menghasilkan error karena fungsi private tidak bisa diakses dari luar kelas
# mobil_saya.__ubah_merk("Suzuki")

# Memanggil fungsi instance protected
# Bisa diakses, tetapi tidak disarankan karena bisa mengganggu enkapsulasi
mobil_saya._ubah_model("Rubicon")

# Memanggil fungsi info untuk menampilkan informasi mobil
mobil_saya.info()
