# -*- coding: utf-8 -*-
# @Time     : 2019-05-09 21:11
# @Author   : focusxyhoo
# @FileName : if_analyse.py


import os
from os import path
from collections import Counter
import codecs
from wordcloud import WordCloud
import nltk
from nltk import word_tokenize


def get_text(file):
    text = open(file, "r").read()
    # 将所有单词转换为小写去掉大小写的干扰
    text = text.lower()
    # 去掉所有的特殊符号
    for ch in '`!@#~$%^&*()_+-=*/{}[]:;,./?<>':
        text = text.replace(ch, " ")  # 将特殊符号替换成空格 即去掉
    return text


def generate_file_path(directory):
    files = os.listdir(directory)
    return [path.join(directory, file) for file in files]


def get_counter(directory, stop_words):
    file_paths = generate_file_path(directory)
    counter = Counter()
    for file in file_paths:
        if file.split('/')[-1] == ".DS_Store":
            print("Ignore file: %s" % file)
            continue
        text = get_text(file)
        words = text.split()
        for word in words:
            if len(word) > 1 and word not in stop_words and not word.isdigit():
                counter[word] += 1
    return counter


def save_to_file(result_path, counter):
    with codecs.open(result_path, 'w') as f:
        for k, v in counter.items():
            f.write(k + ", " + str(v) + "\r\n")
    print("已保存至本地：" + result_path)


def word_cloud(img_path, counter):
    # 制作云图
    # 英文不需要设置路径，但是中文需要，否则无法显示。font_path="/Users/huxiaoyang/Downloads/SimHei.ttf"
    wordcount = WordCloud(background_color='white',
                          max_font_size=80, scale=5,
                          max_words=150,
                          min_font_size=5
                          )
    wordcount = wordcount.generate_from_frequencies(counter)
    wordcount.to_file(img_path)


def tokenizer(file):
    raw = get_text(file)
    tokens = word_tokenize(raw)
    return tokens


def main():
    stop_words = {"the", "and", "of", "with", "but", "as", "be", "in", "or", "are", "to", "for", "at", "on", "https",
            "doi", "org", "was", "were", "is", "this", "had", "et", "al", "that", "can", "an", "am", "by", "have",
            "from", "we", "may", "has", "ing", "been", "all", "https:", "between", "using", "doi:https:", "used",
            "than", "not", "these", "no", "after", "our", "which", "non", "also", "more", "it", "low", "high", "kg",
            "both", "table", "during", "there", "based", "time", "journal", "overall", "only", "other", "two", "such",
            "one", "who", "m2", "studies", "vs", "ko", "muscles", "related", "clin", "total", "patient", "cm2", "e2",
            "however", }
    directory = "/Users/huxiaoyang/Desktop/同济项目论文搜索/docs/"
    result_path = "/Users/huxiaoyang/Desktop/同济项目论文搜索/WordsFrequency03.csv"
    img_path = "/Users/huxiaoyang/Desktop/同济项目论文搜索/images/if.png"

    # counter = get_counter(directory=directory, stop_words=stop_words)
    # save_to_file(result_path, counter)
    # word_cloud(img_path)

    # print(generate_file_path(directory))

    print(tokenizer("/Users/huxiaoyang/Desktop/同济项目论文搜索/docs/@voron2015.txt"))


if __name__ == '__main__':
    main()
