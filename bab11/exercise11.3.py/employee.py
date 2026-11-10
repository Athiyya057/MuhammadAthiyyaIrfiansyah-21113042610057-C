class Employee:
    

    def __init__(self, nama_depan, nama_belakang, gaji):
        self.first = nama_depan.title()
        self.last = nama_belakang.title()
        self.salary = gaji

    def give_raise(self, jumlah=5000):
      
        self.salary += jumlah