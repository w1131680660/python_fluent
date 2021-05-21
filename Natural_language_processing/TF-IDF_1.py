
from collections import defaultdict
import math
import operator
'''
    operator.itemgetter() 函数有一个被 rows 中的记录用来查找值的索引参数。可以是一个字典键名称，
     一个整形值或者任何能够传入一个对象的 __getitem__() 方法的值。 
    如果你传入多个索引参数给 itemgetter() ，它生成的 callable 对象会返回一个包含所有元素值的元组， 
    并且 sorted() 函数会根据这个元组中元素顺序去排序。 但你想要同时在几个字段上面进行排序（比如通过姓和名来排序，
    也就是例子中的那样）的时候这种方法是很有用的。
'''

def loadDataSet():
    dataset = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],  # 切分的词条
               ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
               ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
               ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
               ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
               ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 类别标签向量，1代表好，0代表不好
    return dataset, classVec


def feature_select():
    dataset, classVec = loadDataSet()
    data_1 = defaultdict(int)
    for i in dataset:
        for v in i:
            data_1[v] +=1
    #print(data_1)  # 计算出每个单词出现的次数
    # print(i,data_1)

    # 计算每个单词的TF值
    data_df = {}
    len_data = sum(data_1.values())

    for k,v in data_1.items():
        data_df[k] = v / len_data

    doc_num = len(dataset)
    data_idf = {}
    data_doc = defaultdict(int)

    for i in data_1:
        for j in dataset:
            if i in j:
                data_doc[i] +=1 # 包含对于词条的文档数

    for i in data_1:
        data_idf[i] = math.log(doc_num / (data_doc[i] + 1))
    # print(data_idf)
    # 计算每个词的TF*IDF的值
    word_tf_idf = {}
    for i in data_1:
        word_tf_idf[i] = data_df[i] * data_idf[i]
    print(word_tf_idf)
    word_tf_idf = dict(sorted(word_tf_idf.items(), key=operator.itemgetter(1), reverse=True))
    # print(word_tf_idf)
    print(word_tf_idf)
feature_select()