def creator_task(dir, n, type):
    task = 'task'
    for i in range(n):
        string = dir
        string += task
        if i < 9:
            string += '0'
        string += str(i + 1)
        string += type

        file = open(string, 'r', encoding='utf-8')
        file.close()

creator_task('lab02/', 20, '.sql')