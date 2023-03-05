class Mahasiswa:
    def __init__(self, nama, nim, kelas, sks):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.sks = sks
    def tampil_mahasiswa(self):
        print("M. Akbar Purnama Putra")
        print("121140065")
        print("RB")
        print("20")

Mahasiswa = Mahasiswa("M. Akbar Purnama Putra", 121140065, "RB", 20)
Mahasiswa.tampil_mahasiswa()

   
