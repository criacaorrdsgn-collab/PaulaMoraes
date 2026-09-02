import os

def find_node(start_paths):
    found = []
    for path in start_paths:
        if not os.path.exists(path):
            continue
        print(f"Buscando em: {path} ...")
        for root, dirs, files in os.walk(path):
            # Skip some huge unneeded directories if possible
            if 'Windows' in root and len(root) < 15:
                continue
            if 'node.exe' in files:
                found.append(os.path.join(root, 'node.exe'))
    return found

paths_to_search = [
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    r"C:\Users",
    "H:\\"
]

results = find_node(paths_to_search)
if results:
    print("\nNode.js encontrado em:")
    for r in results:
        print(r)
else:
    print("\nNenhum node.exe encontrado nos diretórios verificados.")
