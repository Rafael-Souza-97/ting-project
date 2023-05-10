from ting_file_management.priority_queue import PriorityQueue
import pytest


mock_txt_list = [
    {
        "nome_do_arquivo": "arquivo_1.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": [
            "linha",
            "linha",
            "linha",
        ],
    },
    {
        "nome_do_arquivo": "arquivo_2.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [
            "linha",
            "linha",
        ],
    },
    {
        "nome_do_arquivo": "arquivo_3.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [
            "linha",
            "linha",
            "linha",
            "linha",
            "linha",
            "linha",
        ],
    },
]


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    for item in mock_txt_list:
        priority_queue.enqueue(item)

    with pytest.raises(IndexError):
        priority_queue.search(5)

    assert len(priority_queue.regular_priority) == 1
    assert len(priority_queue.high_priority) == 2
    assert priority_queue.search(1) == mock_txt_list[1]
    assert priority_queue.dequeue() == mock_txt_list[0]
    assert priority_queue.is_priority(mock_txt_list[2]) is False
    assert priority_queue.is_priority(mock_txt_list[0]) is True
