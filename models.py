from django.db import models

# Create your models here.
class question(models.Model):
    question_id = models.IntegerField(max_length=32, default=0)     # 主键
    question = models.CharField(max_length=32, default=0)           # 问句，便于计算句子相似度->需要考虑数据冗余问题
    keyword = models.CharField(max_length=32, default=0)            # 关键词，为一个列表，优先级高的在前
    question_type = models.CharField(max_length=20, default=0)      # 问题的类别：如C语言、python、计算机组成、汇编、数据结构、算法等
    answer_ids = models.IntegerField(max_length=32, default=0)      # 答案id，后期可改为候选答案的id列表，供用户选择
    # value = models.IntegerField(max_length=32, default=0)         # 浏览数，我觉得可以删去

class answer(models.Model):
    answer_id = models.ImageField(max_length=32, default=0)         # 答案主键
    answer = models.CharField(max_length=32, default=0)             # 某个问题的答案，为一个网址，或者文字
    keyword = models.CharField(max_length=32, default=0)
    value = models.IntegerField(max_length=32, default=0)           # 算法打分，或者为用户的满意程度，答案是否解决了问题
