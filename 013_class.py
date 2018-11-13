class matematika:
    def __init__(self,a,b):
        self.x = a
        self.y = b
    def tambah(self):
        tt=self.x+self.y
        return tt
    def kurang(self):
        return self.x - self.y
    def pangkat(self):
        return self.x ** self.y
    def bagi(self):
        return self.x / self.y

# hasil = matematika(2,3)
#
# print('hasil penjumlahan=', hasil.tambah())
# print('hasil pemangkatan=', hasil.pangkat())
# print('hasil pengurangan=', hasil.kurang())

