# -*- coding: utf-8 -*-
# @Time     : 2019-05-09 20:26
# @Author   : focusxyhoo
# @FileName : pdf_reader.py

import os
from pdfminer.pdfparser import PDFParser, PDFDocument, PDFSyntaxError
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def parse(file):
    # 不知道为什么这样不能过滤掉 .DS_Store 文件
    # if file == ".DS_Store":
    #     return

    # 解析PDF文本，并保存到TXT文件中
    fp = open(file, 'rb')

    # 用文件对象创建一个PDF文档分析器
    parser = PDFParser(fp)

    # 创建一个PDF文档
    doc = PDFDocument()

    # 连接分析器，与文档对象
    try:
        parser.set_document(doc)
        doc.set_parser(parser)
    except PDFSyntaxError:
        print("已过滤文件 %s" % file)
        return

    # 提供初始化密码，如果没有密码，就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDF，资源管理器，来共享资源
        pdf_resource_manager = PDFResourceManager()
        # 创建一个PDF设备对象
        la_params = LAParams()
        device = PDFPageAggregator(pdf_resource_manager, laparams=la_params)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(pdf_resource_manager, device)

        # 循环遍历列表，每次处理一个page内容
        # get_pages()方法用来获取page列表
        for page in doc.get_pages():
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着这个page解析出的各种对象
            # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal等等
            # 想要获取文本就获得对象的text属性，
            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):
                    # 这里就暴力点，没有修改原来文件的后缀名
                    with open(file + '.txt', 'a') as f:
                        results = x.get_text()
                        # print(results)
                        f.write(results + "\n")
        print("%s 转换成功，已保存本地！" % file)


def main():
    files_path = "/Users/huxiaoyang/Desktop/同济项目论文搜索/"
    for file in os.listdir(files_path):
        print("正在处理 %s" % file)
        parse(files_path + '/' + file)


if __name__ == '__main__':
    main()
