from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    word = word.lower()
    result = []
    for file in instance.queue:
        txt_file = txt_importer(file)
        occurrences = []
        for index, line in enumerate(txt_file):
            if word in line.lower():
                occurrences.append({"linha": index + 1})
        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file,
                "ocorrencias": occurrences
            })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
