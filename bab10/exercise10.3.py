from pathlib import Path

path = Path("learning_python.txt")
isi = path.read_text()

for baris in isi.splitlines():
    print(baris)