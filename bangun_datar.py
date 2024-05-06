from abc import ABC, abstractmethod
import math

class Luas(ABC):
    @abstractmethod
    def menghitung(self):
        pass

class Persegi(Luas):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def menghitung(self):
        return self.sisi * self.sisi

class Persegi_panjang(Luas):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def menghitung(self):
        return self.panjang * self.lebar

class Lingkaran(Luas):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    
    def menghitung(self):
        return math.pi * self.jari_jari * 2

class Segitiga(Luas):
    def __init__(self, tinggi, alas):
        self.tinggi = tinggi
        self.alas = alas
    
    def menghitung(self):
        return 0.5 * self.tinggi * self.alas

class Jajar_genjang(Luas):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def menghitung(self):
        return self.alas * self.tinggi





   