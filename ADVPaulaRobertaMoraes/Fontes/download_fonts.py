import urllib.request
import os

fonts = {
    "Cinzel": "https://raw.githubusercontent.com/google/fonts/main/ofl/cinzel/Cinzel%5Bwght%5D.ttf",
    "Questrial": "https://raw.githubusercontent.com/google/fonts/main/ofl/questrial/Questrial-Regular.ttf"
}

dest_dir = r"c:\RodrigoRochaDesign\Projetos\Websites\ADVPaulaRobertaMoraes\Fontes"
os.makedirs(dest_dir, exist_ok=True)

for name, url in fonts.items():
    print(f"Baixando {name} do GitHub...")
    font_path = os.path.join(dest_dir, f"{name}.ttf")
    try:
        urllib.request.urlretrieve(url, font_path)
        print(f"{name} salvo em {font_path}")
    except Exception as e:
        print(f"Erro ao baixar {name}: {e}")
