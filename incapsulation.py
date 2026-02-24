


class BankUser:
    def __init__(self,first_name,last_name,age,card_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__card_number = card_number
    def card_info(self):
        return f"Foydalanuvchi:{self.__first_name} {self.__last_name}\nKarta raqami:{self.__card_number}"

ali=BankUser("Ali","Hechkimov",15,1234567891123456)
print(ali.card_info())







