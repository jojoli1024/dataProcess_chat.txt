# 处理成一问一答 第二步
# 方法2：把多个 Q 或者 A 合并为一个 Q 或者 A ，去重复的 Q 、A

filePath_chat_rd = 'chat_rd_after.txt'
filePath_chat_QA2 = 'chat_QA2.txt'
separator_str = 'session:'

# 对列表的元素去重，返回字符串
def de_duplication(list):
    dedup_list = []
    for word in list:
        if not word in dedup_list:
            dedup_list.append(word)
    return ' '.join(dedup_list) + '\n'

try:
    chat_rd = open(filePath_chat_rd,'r')
    chat_QA2 = open(filePath_chat_QA2,'r+')

    Q_flag = True

    questions = []
    answers = []

    line = chat_rd.readline()
    while True:
        if not line:
            break
        if separator_str in line:
            if not questions and not answers:
                # questions 和 answers 两个列表为空
                # 分隔符要分割QA！！
                print(line)
                chat_QA2.write(line)
                line = chat_rd.readline()
            elif Q_flag:
                # 上一个为Q，下一个应为A
                if answers:
                   # 若answers不为空
                    answers.insert(0,'A\t')
                    print(de_duplication(answers))
                    chat_QA2.write(de_duplication(answers))
                    answers.clear() 
                if questions:
                    # 若questions不为空
                    questions.insert(0,'Q\t')
                    print(de_duplication(questions))
                    chat_QA2.write(de_duplication(questions))
                    questions.clear()
            elif not Q_flag:
                # 上一个为A，下一个应为Q
                if questions:
                    # 若questions不为空
                    questions.insert(0,'Q\t')
                    print(de_duplication(questions))
                    chat_QA2.write(de_duplication(questions))
                    questions.clear()
                if answers:
                   # 若answers不为空
                    answers.insert(0,'A\t')
                    print(de_duplication(answers))
                    chat_QA2.write(de_duplication(answers))
                    answers.clear() 
            # elif questions:
            #     # 若questions不为空
            #     questions.insert(0,'Q\t')
            #     print(de_duplication(questions))
            #     # chat_QA2.write(de_duplication(questions))
            #     questions.clear()
            # elif answers:
            #     # 若answers不为空
            #     answers.insert(0,'A\t')
            #     print(de_duplication(answers))
            #     # chat_QA2.write(de_duplication(answers))
            #     answers.clear()
        if 'Q' in line:
            if Q_flag:
                # 上一个是Q开头的
                questions.append(line[2:-1])
                line = chat_rd.readline()
                continue
            else:
                # 这是下第一个Q开头的，上一个是A开头
                if questions:
                    questions.insert(0,'Q\t')
                    print(de_duplication(questions))
                    chat_QA2.write(de_duplication(questions))
                    questions.clear()
                Q_flag = True
        elif 'A' in line:
            if not Q_flag:
                # 上一个是A开头的
                answers.append(line[2:-1])
                line = chat_rd.readline()
                continue
            else:
                # 这是下第一个A开头的，上一个是Q开头
                if answers:
                    answers.insert(0,'A\t')
                    print(de_duplication(answers))
                    chat_QA2.write(de_duplication(answers))
                    answers.clear()
                Q_flag = False  

finally:
    if chat_rd:
        chat_rd.close()
    if chat_QA2:
        chat_QA2.close()