from abc import ABC, abstractmethod


class Hewan(ABC):
    def __init__(self, nama):
        self.__nama = nama

    @abstractmethod
    def suara(self):
        pass

    def nama(self):
        return self.__nama


class Kucing(Hewan):
    def suara(self):
        return "Meow"


class Anjing(Hewan):
    def suara(self):
        return "Guk"


hewan_peliharaan = [Kucing("Kitty"), Anjing("Buddy")]
for hewan in hewan_peliharaan:
    print(f"{hewan.nama()} suara : {hewan.suara()}")
