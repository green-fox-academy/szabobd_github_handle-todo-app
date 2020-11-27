
with open('tasks.txt', 'r') as in_file:
    content = in_file.readlines()
    lista = []
    checker = 3
    for position, line in enumerate(content):
        if position + 1 == checker:
            list_of_characters = list(line)
            list_of_characters[2] = 'x'
            checked_line = ""
            lista.append(checked_line.join(list_of_characters))
        else:
            lista.append(line)


with open('tasks.txt', 'w') as f:
    for line in lista:
        f.write(line)
