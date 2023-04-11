# Nama  : M. Akbar Purnama Putra
# NIM   : 121140065

from abc import ABC, abstractmethod
import datetime

class AkunBank(ABC):
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo
    
    def lihat_saldo(self):
        print(f"Saldo {self.nama}: Rp {self.saldo:,}")
        
    @abstractmethod
    def transfer_saldo(self, jumlah):
        pass
    
    @abstractmethod
    def lihat_suku_bunga(self):
        pass

class AkunGold(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        
    def transfer_saldo(self, jumlah):
        usia_akun = datetime.date.today().year - self.tahun_daftar
        if jumlah < 100000:
            biaya_administrasi = 0
        elif usia_akun >= 3 and jumlah >= 100000:
            biaya_administrasi = 0
        elif usia_akun < 3 and jumlah >= 100000:
            biaya_administrasi = 2000
        else:
            biaya_administrasi = 0
        total_biaya = jumlah + biaya_administrasi
        if self.saldo < total_biaya:
            print("Maaf, saldo tidak cukup.")
        else:
            self.saldo -= total_biaya
            print(f"Transfer sebesar Rp {jumlah:,} sukses. Biaya administrasi: Rp {biaya_administrasi:,}")
            self.lihat_saldo()
            
    def lihat_suku_bunga(self):
        usia_akun = datetime.date.today().year - self.tahun_daftar
        if self.saldo >= 1000000000:
            if usia_akun >= 3:
                bunga = 0.01
            else:
                bunga = 0.02
        else:
            bunga = 0.03
        print(f"Suku bunga: {bunga*100:.2f}% per bulan")

class AkunSilver(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        
    def transfer_saldo(self, jumlah):
        usia_akun = datetime.date.today().year - self.tahun_daftar
        if jumlah < 100000:
            biaya_administrasi = 0
        elif usia_akun >= 3 and jumlah >= 100000:
            biaya_administrasi = 2000
        elif usia_akun < 3 and jumlah >= 100000:
            biaya_administrasi = 5000
        else:
            biaya_administrasi = 0
        total_biaya = jumlah + biaya_administrasi
        if self.saldo < total_biaya:
            print("Maaf, saldo tidak cukup.")
        else:
            self.saldo -= total_biaya
            print(f"Transfer sebesar Rp {jumlah:,} sukses. Biaya administrasi: Rp {biaya_administrasi:,}")
            self.lihat_saldo()
    
    def lihat_suku_bunga(self):
        usia_akun = datetime.date.today().year - self.tahun_daftar
        if self.saldo >= 10000000:
            if usia_akun >=3:
                bunga = 0.01
            else:
                bunga = 0.02
        else:
            bunga = 0.03
        print(f"suku bunga: {bunga*100:.2f}%per bulan")
                
class AkunReguler(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        
    def transfer_saldo(self, jumlah):
        usia_akun = datetime.date.today().year - self.tahun_daftar
        if jumlah < 100000:
            biaya_administrasi = 5000
        else:
            biaya_administrasi = 0
        total_biaya = jumlah + biaya_administrasi
        if self.saldo < total_biaya:
            print("Maaf, saldo tidak cukup.")
        else:
            self.saldo -= total_biaya
            print(f"Transfer sebesar Rp {jumlah:,} sukses. Biaya administrasi: Rp {biaya_administrasi:,}")
            self.lihat_saldo()

    def lihat_suku_bunga(self):
        print("Akun regular tidak mendapatkan suku bunga.")

akun_gold = AkunGold("M. Akbar Purnama Putra", 2023, 1500000000)
akun_gold.lihat_saldo()
akun_gold.lihat_suku_bunga()
akun_gold.transfer_saldo(20000000) 
akun_gold.lihat_saldo()   
print ("---------------------------------------------------------------")
akun_silver = AkunSilver("Iwan Subagio", 2023, 80000000)
akun_silver.lihat_saldo() 
akun_silver.lihat_suku_bunga() 
akun_silver.transfer_saldo(100000) 
akun_silver.lihat_saldo() 
print ("---------------------------------------------------------------")
akun_regular = AkunReguler("Umi Arsih", 2023, 5000000)
akun_regular.lihat_saldo() 
akun_regular.transfer_saldo(50000)
akun_regular.lihat_saldo() 
akun_regular.lihat_suku_bunga() 


                
