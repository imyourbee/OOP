# Superclass
class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.__judul = judul  # Private attribute
        self.__penulis = penulis  # Private attribute
        self.__tahun_terbit = tahun_terbit  # Private attribute

    # Setter untuk judul
    def set_judul(self, judul):
        self.__judul = judul

    # Getter untuk judul
    def get_judul(self):
        return self.__judul

    # Setter untuk penulis
    def set_penulis(self, penulis):
        self.__penulis = penulis

    # Getter untuk penulis
    def get_penulis(self):
        return self.__penulis

    # Setter untuk tahun terbit
    def set_tahun_terbit(self, tahun_terbit):
        if tahun_terbit > 0:  # Validasi tahun terbit
            self.__tahun_terbit = tahun_terbit
        else:
            print("Tahun tidak valid.")

    # Getter untuk tahun terbit
    def get_tahun_terbit(self):
        return self.__tahun_terbit

    def info(self):
        return f"Judul: {self.get_judul()}, Penulis: {self.get_penulis()}, Tahun Terbit: {self.get_tahun_terbit()}"

# Subclass
class Ebook(Buku):
    def __init__(self, judul, penulis, tahun_terbit, format_file):
        super().__init__(judul, penulis, tahun_terbit)  # Memanggil konstruktor superclass
        self.__format_file = format_file  # Private attribute

    # Setter untuk format file
    def set_format_file(self, format_file):
        self.__format_file = format_file

    # Getter untuk format file
    def get_format_file(self):
        return self.__format_file

    def info(self):
        buku_info = super().info()  # Memanggil info dari superclass
        return f"{buku_info}, Format File: {self.get_format_file()}"

# Menggunakan kelas Ebook
ebook_saya = Ebook("Belajar Python", "John Doe", 2023, "PDF")
print(ebook_saya.info())  

# Mengubah data menggunakan setter
ebook_saya.set_judul("Belajar Python Lanjutan")
ebook_saya.set_tahun_terbit(2024)
ebook_saya.set_format_file("Word")

print(ebook_saya.info())  
