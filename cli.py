from sys import argv
from main import CsvDavinciConverter as dr

converter = dr()
converter.convert(argv[1], argv[2])
print("FINALIZADO")
