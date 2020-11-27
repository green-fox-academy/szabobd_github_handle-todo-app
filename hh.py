


#    elif len(list(in_file1)) == 0:
#        print('Ready for some new todos, chief?')
with open('tasks.txt', 'r') as in_file1, open('undone_tasks.txt', 'r') as in_file2:
    print('You have ' + str(len(list(in_file1))) + ' todos, ' + str(len(list(in_file2))) + ' undone')
    print(len(list(in_file1)))

