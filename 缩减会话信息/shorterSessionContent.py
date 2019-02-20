filePath = 'chat_zh.txt'
filePath_new = 'chat_rd.txt'

chat_zh = open(filePath,'r')
chat_rd = open(filePath_new,'r+')

# data = chat_zh.read()
# print(data.find('session:0'))
# print(data[data.find('session:0'):data.find('session:1')])

list = []
dict = {
    'session_id':'test',
    'customer_id':'test',
    'is_sendBy_client':'0',
    'is_rollOut':'1',
    'is_repeat':'1',
    'goods_id':'test',
    'session_content':'test'
    }
# line = chat_zh.readlines()[3]
# print(line)


line = chat_zh.readline()
while line:
    if '\n' == line:
        # list.clear()
        line = chat_zh.readline()
    if 'session:' in line:
        # list.clear()
        print(line)
        chat_rd.write(line)
        line = chat_zh.readline()
    if '\n' == line:
        # list.clear()
        line = chat_zh.readline()
    print(line)
    list = line.split('\t',line.count('\t'))
    # 把列表转为字典
    dict['session_id'] = list[0]
    dict['customer_id'] = list[1]
    dict['is_sendBy_client'] = list[2]
    dict['is_rollOut'] = list[3]
    dict['is_repeat'] = list[4]
    dict['goods_id'] = list[5]
    dict['session_content'] = list[6]

    line_new = ''
    if dict['is_sendBy_client'] == '0':
        line_new += 'Q\t'
    elif dict['is_sendBy_client'] == '1':
        line_new += 'A\t'
    line_new += dict['session_content']
    print(line_new)
    chat_rd.write(line_new)

    list.clear()
    line = chat_zh.readline()


chat_zh.close()
chat_rd.close()