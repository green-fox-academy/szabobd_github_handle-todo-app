#in!!

k = 'roka'

if 'o' in k:
    print('yes')


with open('tasks.txt', 'r') as in_file:
    checker = []
    for position, line in enumerate(in_file):
        if list(line)[2] == ' ':
            checker.append(line)

with open('undone_tasks.txt', 'w') as in_file:
    for line in checker:
        in_file.write(line)

   #     if position in checker:
            #global a
            #a = line.replace('[ ]', '[x]')



#with open('tasks.txt', 'w') as k_file:
   # print(a)
  #  for i in enumerate(k_file):
   #     if i == a:
    #        k_file.write(a)


