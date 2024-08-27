from gensim.corpora import WikiCorpus
import jieba
from opencc import OpenCC
from tqdm import tqdm


def convert_to_simplified_chinese(temp_sentence):
    cc = OpenCC('t2s')  # t2s 表示从繁体转为简体
    return cc.convert(temp_sentence)


def data_process():
    space = ' '
    l = []
    i = 0
    zhiwiki_name = './data/zhwiki-latest-pages-articles.xml.bz2'
    f = open('./data/reduce_zhiwiki.txt', 'w', encoding='utf-8')
    # 读取xml文件中的语料
    print('Start reading zhiwiki...')
    wiki = WikiCorpus(zhiwiki_name, dictionary={})
    print('Finish reading zhiwiki')
    # 遍历语料，进行分词
    print('Start processing zhiwiki...')
    # pbar = tqdm(total=wiki.get_texts())
    # print(wiki.get_texts().__sizeof__())
    pbar = tqdm(total=481932, desc="Processing", dynamic_ncols=True)
    for text in wiki.get_texts():
        for temp_sentence in text:
            # 将语料中的繁体字转化为中文
            temp_sentence = convert_to_simplified_chinese(temp_sentence)
            # 使用jieba进行分词
            seg_list = list(jieba.cut(temp_sentence))
            for temp_term in seg_list:
                l.append(temp_term)
        f.write(space.join(l) + '\n')
        l = []
        pbar.update(1)
    f.close()
    print('Finish processing zhiwiki')


if __name__ == '__main__':
    data_process()
