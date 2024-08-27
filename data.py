from gensim.corpora import WikiCorpus
import jieba
from opencc import OpenCC


def convert_to_simplified_chinese(temp_sentence):
    cc = OpenCC('t2s')  # t2s 表示从繁体转为简体
    return cc.convert(temp_sentence)


def data_process():
    space = ' '
    i = 0
    l = []
    zhiwiki_name = './data/zhiwiki-latest-pages-articles.xml.bz2'
    f = open('./data/reduce_zhiwiki.txt', 'w', encoding='utf-8')
    # 读取xml文件中的语料
    print('Start reading zhiwiki...')
    wiki = WikiCorpus(zhiwiki_name, dictionary={})
    print('Finish reading zhiwiki')
    # 遍历语料，进行分词
    print('Start processing zhiwiki...')
    for text in wiki.get_texts():
        print('Processing article ' + str(i))
        for temp_sentence in text:
            # 将语料中的繁体字转化为中文
            temp_sentence = convert_to_simplified_chinese(temp_sentence)
            # 使用jieba进行分词
            seg_list = list(jieba.cut(temp_sentence))
            for temp_term in seg_list:
                l.append(temp_term)
        f.write(space.join(l) + '\n')
        l = []
        i = i + 1
        if i % 20 == 0:
            print('Saved ' + str(i) + ' articles')
    f.close()


if __name__ == '__main__':
    data_process()
