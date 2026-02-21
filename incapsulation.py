                         #1-MASALA
# class Mashina:
#     def __init__(self,brend,rang,tezlik,serail_number):
#         self.brend=brend
#         self.rang=rang
#         self.tezlik=tezlik
#         self.__serail_number=serail_number
#
#     def malumot(self):
#         return f"Brend:{self.brend}, Rang:{self.rang}, Tezlik:{self.tezlik}"
#
#     def s_number(self):
#         return f"Serial Number:{self.__serail_number}\nBrend:{self.brend}"
#
# damas=Mashina("Damas 2","Oq",300,"D5435F")
# labo=Mashina("Labo","Qora",500,"L5768D")
# cobalt=Mashina("Qora","Oq",300,"C5777O")
#
# print(damas.s_number())


                          #2-MASALA
class BankHisobi:
    def __init__(self,egasi,boshlangich_miqdor):
        self.__egasi = egasi
        self.__balans=boshlangich_miqdor
    def get_balans(self):
        return self.__balans
    def get_egasi(self):
        return self.__egasi
    def pul_qosh(self,miqdor):
        if miqdor<=0:
            print("Noto'g'ri miqdor!")
            return
        else:
            self.__balans=miqdor
    def pul_yech(self,miqdor):
        if miqdor<=0:
            print("Noto'g'ri miqdor!")
        elif miqdor>self.__balans:
            print("Mablag' yetarli emas!")
        else:
            self.__balans=miqdor

hisob=BankHisobi("Ali",1_000_000)
print(f"Egasi: {hisob.get_egasi()}")
print(f"Balans: {hisob.get_balans()}")

hisob.pul_qosh(200_000)
print(f"Balans: {hisob.get_balans()} so'm!")

hisob.pul_yech(1_000_000)
print(f"Balans: {hisob.get_balans()} so'm!")

