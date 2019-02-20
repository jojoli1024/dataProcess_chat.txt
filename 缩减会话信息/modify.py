fileInt = 'chat_rd.txt'
fileOut = 'chat_rd_after.txt'

try:
    fin = open(fileInt,'r')
    fout = open(fileOut,'r+')
    while True:
        line = fin.readline()
        if not line:
            break
        if 'session' in line:
            print(line)
            fout.write(line)
            line  = fin.readline()
        newline = ''
        for i in range(len(line)):
            if line[i] == 'Q' or line[i] == 'A':
                if i != 0 and line[i + 1] == '\t':
                    # print()
                    newline += '\n'
                    # fout.write('\n')
            # print(line[i],end='')
            newline += line[i]
        print(newline)
        fout.write(newline)
finally:
    if fin:
        fin.close()
    if fout:
        fout.close()