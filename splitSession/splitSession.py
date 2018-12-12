import chardet

# chcp 65001
# https://github.com/zengbin93/jddc_solution_4th/tree/bb23cd0e557fc46ab2bf57f7a941a7ec4c54f3c4/preliminary/data_pre
# filePath = 'test.txt'
# filePath_new = 'test_new.txt'

filePath = 'new.txt'
filePath_new = 'chat_zh.txt'

def detectCode(file):
    data = file.read()
    dicts = chardet.detect(data)
    return dicts["encoding"]

def transform_text(text):
    """特殊字符转换"""
    str_tf = {
        "#E-s[数字x]": "(微笑)",
        "#E-j[数字x]": "(愤怒)",
        "&nbsp;": " ",
        
    }
    #     "[数字x]%": "(比例)",
    #     "[金额x]%": "(比例)",
    #     "%": " ",
    #     "#": " ",
    #     "&": " ",
    for k, v in str_tf.items():
        text = text.replace(k, v)
    return text

def read_old():
    with open(filePath,'rb') as file:
        print(file.read().decode('GB2312'))

def split_session(file,file_new):
    """分割会话"""
    # gb18030
    line = file.readline().decode('gb18030')
    line_new = transform_text(line)
    session_id = line_new[:line_new.find('\t')]
    # session_id = line[:line.find('\t')]
    index = 0

    session_line = 'session:' + str(index) + '\n\n'
    print(session_line)
    file_new.write(session_line)
    
    while line:
        tmp = line_new[:line_new.find('\t')]
        # tmp = line[:line.find('\t')]
        if tmp != session_id:
            session_id = tmp
            index += 1
            session_line = '\nsession:' + str(index) + '\n\n'
            print(session_line)
            file_new.write(session_line)
        
        print(line_new)
        file_new.write(line_new)
        line = file.readline().decode('gb18030')
        line_new = transform_text(line)

file = open(filePath,'rb')
file_new = open(filePath_new,'r+')

# split_session(file,file_new)

# encode = detectCode(file)
# read_old()
split_session(file,file_new)

file.close()
file_new.close()

# 32
# print(len("00029c51f92e8f34250d6af329c9a8df"))
# print(len("0006f1fe48ba77fa7f42b0acab6e2fad"))