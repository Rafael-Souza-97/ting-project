import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        print("Formato inválido", file=sys.stderr)
        return None
    try:
        with open(path_file, 'r', encoding="utf_8") as document:
            return document.read().splitlines()
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None
