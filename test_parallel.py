from gensim.corpora import WikiCorpus
import jieba
from opencc import OpenCC
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor

cc = OpenCC('t2s')


def convert_and_segment(text):
    converted_text = cc.convert(text)
    return list(jieba.cut(converted_text))


def data_process():
    space = ' '
    l = []
    zhiwiki_name = './data/zhwiki-latest-pages-articles.xml.bz2'
    f = open('./data/reduce_zhiwiki.txt', 'w', encoding='utf-8')
    wiki = WikiCorpus(zhiwiki_name, dictionary={})
    pbar = tqdm(total=481932, desc="Processing", dynamic_ncols=True)

    with ProcessPoolExecutor() as executor:
        futures = []
        for text in wiki.get_texts():
            for temp_sentence in text:
                futures.append(executor.submit(convert_and_segment, temp_sentence))

            for future in futures:
                l.extend(future.result())
            f.write(space.join(l) + '\n')
            l = []
            pbar.update(1)

    f.close()
    print('Finish processing zhiwiki')


if __name__ == '__main__':
    data_process()
