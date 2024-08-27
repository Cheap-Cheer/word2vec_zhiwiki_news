# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def train():
    wiki_news = open('./data/reduce_zhiwiki.txt', 'r')
    # Word2Vec第一个参数代表要训练的语料
    # sg=0 表示使用CBOW模型进行训练
    # size 表示特征向量的维度，默认为100。大的size需要更多的训练数据,但是效果会更好. 推荐值为几十到几百。
    # window 表示当前词与预测词在一个句子中的最大距离是多少
    # min_count 可以对字典做截断. 词频少于min_count次数的单词会被丢弃掉, 默认值为5
    # workers 表示训练的并行数
    model = Word2Vec(LineSentence(wiki_news), sg=0, size=192, window=5, min_count=5, workers=9)
    model.save('zhiwiki_news.word2vec')


if __name__ == '__main__':
    train()
