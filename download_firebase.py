import urllib.request
import sys

url = "https://firebase.tools/bin/win/instant/latest"
dest = "firebase.exe"

def report(count, block_size, total_size):
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write(f"\rBaixando... {percent}%")
    sys.stdout.flush()

print("Iniciando o download do Firebase...")
urllib.request.urlretrieve(url, dest, reporthook=report)
print("\nDownload concluído!")
