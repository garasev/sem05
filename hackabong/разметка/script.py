import os
import string

path = 'threads'
path = os.path.normpath(path)
for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
        if dirnames == "threads":
            with open(dirpath + "//" + file, mode='r', encoding='utf8') as f:
                new_file = open(dirpath + "//new//" + file, mode='w', encoding='utf8')
                jopa = []
                for line in f:
                    if line not in jopa:
                        flag = 1
                        for char in line:
                            if char in string.ascii_lowercase:
                                flag = 0
                                break
                        if flag:
                            jopa.append(line)
                            new_file.write(line[1:])