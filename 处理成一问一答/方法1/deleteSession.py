keyStr = 'session:'
# 此脚本是为了删去只有Q或者只有A的session，并重新编号
filePath_Q = 'chat_Q.txt'
filePath_A = 'chat_A.txt'
filePath_Q_after = 'chat_Q_after.txt'
filePath_A_after = 'chat_A_after.txt'
session = ''
sessionList = []
# 要删去的session编号列表

def addSessionList(filePath):
    with open(filePath,'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if keyStr in line:
                session = line
                line = f.readline()
                if keyStr in line:
                    # 第二行也为session，即上一个session为空！
                    sessionList.append(session)

addSessionList(filePath_A)
addSessionList(filePath_Q)
print( sessionList )

# 就三个session，我自己手动删去了【狗头
# ['session:2655\n', 'session:4973\n', 'session:7427\n']

def reOrder(filePath,filePath1):
    # 重新编号
    count = 0
    try:
        f = open(filePath,'r')
        fout = open(filePath1,'r+') 

        while True:
            line = f.readline()
            if not line:
                break
            if keyStr in line:
                line = keyStr + str(count) + '\n'
                count += 1
                print(line)
                fout.write(line)
                line = f.readline()
            print(line)
            fout.write(line)
    finally:
        if f:
            f.close()
        if fout:
            fout.close() 

reOrder(filePath_Q,filePath_Q_after)
reOrder(filePath_A,filePath_A_after)
