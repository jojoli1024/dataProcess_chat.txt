keyStr = 'session'
filePath_chat_Q_after = 'chat_Q_after.txt'
filePath_chat_A_after = 'chat_A_after.txt'
filePath_chat_QA1 = 'chat_QA1.txt'

try:
    chat_Q = open(filePath_chat_Q_after,'r')
    chat_A = open(filePath_chat_A_after,'r')
    chat_QA1 = open(filePath_chat_QA1,'r+')

    # 合并成一个文档 QA
    # 难点:判断是否两个处于同一个session
    # 异常情况：有一个 A 或者 Q 中某个session为空，则后续session错乱 -> session + 编号控制分割

    A_line = chat_A.readline()
    Q_line = chat_Q.readline()

    flag = False
    # 判断是否同一个session下的flag

    while True:
        if not A_line:
            break
        if not Q_line:
            break

        if keyStr in Q_line and keyStr in A_line:
            flag = bool(Q_line == A_line)
            # 判断是否 Q 和 A session的编号相同！
            if flag:
                # Q 和 A 在同一个session下
                # 显示session分割
                print(Q_line)
                chat_QA1.write(Q_line)
                Q_line = chat_Q.readline()
                A_line = chat_A.readline()

        if flag:
            # Q 和 A 在同一个session下
            print(Q_line)
            chat_QA1.write(Q_line)
            Q_line = chat_Q.readline()
            print(A_line)
            chat_QA1.write(A_line)
            A_line = chat_A.readline()
        else:
            print('Q and A are not under the same session!!')
            break;
        
        # 针对后续session的显示与分割
        if 'session' in Q_line and 'session' in A_line:
            # 该情况是 Q 等于 A
            continue
        if 'session' in Q_line:
            # 该情况是 Q 小于 A , Q 提早结束
            # 使 A 跳转至下一个 session
            while 'session' not in A_line and A_line:
                A_line = chat_A.readline()
            continue
        if 'session:' in A_line:
            # 该情况是 Q 大于 A ，A 提早结束 
            # 使 Q 跳转到下一个 session
            while 'session' not in Q_line and Q_line:
                Q_line = chat_Q.readline()
            continue
            
finally:
    if chat_A:
        chat_A.close()
    if chat_Q:
        chat_Q.close()
    if chat_QA1:
        chat_QA1.close()