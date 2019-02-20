### 1 方法一思路：

------
分割成两个文档 Q 和 A ，再合并成为一个QAQAQA格式的文档

在同一个session，Q A 不相等的情况下删去多余的部分

### 2 执行顺序：

------

| 输入 | 执行文件 |  输出 |
|:---|:---|:---|
| chat_rd_after.txt | **createQA1_1.py** | chat_Q.txt / chat_A.txt|
| chat_Q.txt / chat_A.txt | **deleteSession.py** | chat_Q_after.txt / chat_A_after.txt|
| chat_Q_after.txt / chat_A_after.txt | **createQA1_2.py** | chat_Q_after.txt / chat_A_after.txt|

### 3 已解决问题：

------

| 问题                                                        | 办法                                                 |
| ----------------------------------------------------------- | ---------------------------------------------------- |
| 长度不对应，文件位置跳转麻烦                                | 直接遍历到对应session，**同时判断是否到达文档底部 ** |
| 分割后，QA有部分混杂                                        | 逻辑写错，已修正                                     |
| 合并后，一个会话下的Q对应了不同会话下的A，（个别会话Q为空） | deleteSession.py删去为空的会话，并重新编号           |



