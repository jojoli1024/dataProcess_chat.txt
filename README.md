# 基于检索的问答库1.0✨

## 1 拆分会话

分割成多个相互独立的会话

| 输入    | 执行文件        | 输出        |
| ------- | --------------- | ----------- |
| new.txt | splitSession.py | chat_zh.txt |

chat_zh.txt为分割好的10943个sessions

## 2 缩减会话信息

除去对话开头冗余的信息

| 输入        | 执行文件                 | 输出              |
| ----------- | ------------------------ | ----------------- |
| chat_zh.txt | shorterSessionContent.py | chat_rd.txt       |
| chat_rd.txt | modify.py                | chat_rd_after.txt |

chat_rd.txt为缩减后的sessions，格式变为Q/A + session_content。

chat_rd_after.txt为修正个别错误后的新文件（2019.02.20）

## 3 处理成一问一答

将每个会话处理成QAQAQA格式

#### 思路1：按顺序对应QA，删去多余的Q或者A

| 输入 | 执行文件 |  输出 |
|:---|:---|:---|
| chat_rd_after.txt | **createQA1_1.py** | chat_Q.txt / chat_A.txt|
| chat_Q.txt / chat_A.txt | **deleteSession.py** | chat_Q_after.txt / chat_A_after.txt|
| chat_Q_after.txt / chat_A_after.txt | **createQA1_2.py** | chat_Q_after.txt / chat_A_after.txt|

#### 思路2：多个Q或者A合并为一个Q或者A

| 输入              | 执行文件         | 输出         |
| :---------------- | :--------------- | :----------- |
| chat_rd_after.txt | **createQA2.py** | chat_QA2.txt |