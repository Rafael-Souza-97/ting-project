import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file in instance.queue:
        return None
    txt = txt_importer(path_file)
    instance.enqueue(path_file)
    print(str({
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt),
        "linhas_do_arquivo": txt}))


def remove(instance):
    if not len(instance.queue):
        return sys.stdout.write("Não há elementos\n")
    dequeued = instance.dequeue()
    print("Arquivo", dequeued, "removido com sucesso")


def file_metadata(instance, position):
    try:
        path_file = instance.search(position)
        txt = txt_importer(path_file)
        metadata = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt),
            "linhas_do_arquivo": txt
        }
        print(str(metadata))
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
