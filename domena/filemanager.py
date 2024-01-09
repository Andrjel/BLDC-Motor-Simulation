from domena.symulacja import Symulacja
from datetime import datetime
import os


class FileManager:
    @staticmethod
    def zapisz_dane(data: Symulacja):
        """
        zapisuje aktualne dane symulacji do pliku
        """
        path = "data/" + datetime.today().strftime("%Y-%m-%d") + "/"
        if not os.path.isdir(path):
            os.mkdir(path)
        file_name = datetime.today().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
        with open(path + file_name, "w") as file:
            file.write("czas,wejscie,wyjscie\n")
            for i in range(len(data.dane["czas"].aktualna_kolejka())):
                file.write(str(data.dane["czas"].aktualna_kolejka()[i]) + ",")
                file.write(str(data.dane["wejscie"].aktualna_kolejka()[i]) + ",")
                file.write(str(data.dane["wyjscie"].aktualna_kolejka()[i]) + "\n")
