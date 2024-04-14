import os

path_to_table = r"\Подписчики на рассылку.txt"


async def list_to_text_file(lst):
    with open(path_to_table, 'w') as file:
        for item in lst:
            file.write(str(item) + '')


async def text_file_to_list():
    lst = []
    with open(path_to_table, 'r') as file:
        for line in file:
            lst.append(line.strip())
    return lst