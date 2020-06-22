# -*- coding: utf-8 -*-
# author: Jclian91
# place: Pudong Shanghai
# time: 2020-04-03 21:50

import json
import numpy as np
from keras.models import load_model

from att import Attention
from albert_zh.extract_feature import BertVector
load_model = load_model("event_type.h5", custom_objects={"Attention": Attention})

# 预测语句
text = "早上气候如何"
text = text.replace("\n", "").replace("\r", "").replace("\t", "")

labels = []

bert_model = BertVector(pooling_strategy="NONE", max_seq_len=200)

# 将句子转换成向量
vec = bert_model.encode([text])["encodes"][0]
x_train = np.array([vec])

# 模型预测
predicted = load_model.predict(x_train)[0]

indices = [i for i in range(len(predicted)) if predicted[i] > 0.5]

with open("event_type.json", "r", encoding="utf-8") as g:
    movie_genres = json.loads(g.read())

print("预测语句: %s" % text)
print("意图分析: %s" % "|".join([movie_genres[index] for index in indices]))




