# 处理成一问一答
# 使用TF-IDF获取前五个关键词及其权值

filePath_chat_rd = 'chat_rd_after.txt'
filePath_chat_Q = 'chat_Q.txt'
filePath_chat_A = 'chat_A.txt'
filePath_chat_QA1 = 'chat_QA1.txt'

# 第一步：计算各个session的QA个数
# 结果：各个session的 Q、A 个数大多数情况下并不对等

# Q = 0
# A = 0

# with open(filePath_chat_rd,'r') as chat_rd:
#     while True:
#         line = chat_rd.readline()
#         if not line:
#             break
#         if "session:" in line:
#             print('Q:{}\tA:{}'.format(Q,A))
#             print(line)
#             Q = 0
#             A = 0
#             line = chat_rd.readline()
#         if '\n' == line:
#             line = chat_rd.readline()
#         if 'Q' in line:
#             Q += 1
#         if 'A' in line:
#             A += 1

# 第二步：简单地按顺序匹配QA
# 方法1：将QA分割成两个文档，再合并成一个文档

try:
    chat_rd = open(filePath_chat_rd,'r')
    chat_Q = open(filePath_chat_Q,'r+')
    chat_A = open(filePath_chat_A,'r+')
    # 分割成两个文档 Q A
    while True:
        line = chat_rd.readline()
        if not line:
            break
        if 'session:' in line:
            print(line)
            chat_Q.write(line)
            chat_A.write(line)
            line = chat_rd.readline()
        if '\n' == line:
            line = chat_rd.readline()
        if 'Q' == line[0]:
            print(line)
            chat_Q.write(line)
        if 'A' == line[0]:
            print(line)
            chat_A.write(line)
        # if 'Q' in line:
        #     print(line)
        #     chat_Q.write(line)
        # if 'A' in line:
        #     print(line)
        #     chat_A.write(line)
finally:
    if chat_rd:
        chat_rd.close()
    if chat_A:
        chat_A.close()
    if chat_Q:
        chat_Q.close()
