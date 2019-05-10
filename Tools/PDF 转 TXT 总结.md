# PDF 转 TXT 总结
## 背景
因为要对论文进行词频分析, 而论文格式一般都是 PDF 格式的, 因此首先想到的是要将 PDF 转换成更容易读取的 TXT 格式. 于是马上动手去 Google 查资料, “Python PDF转TXT”, 看到了`pdfminer`这个第三方模块, 接着就是读文档, 看博客, 了解基础使用方法, 然后照着教程开始写脚本, 最后就有了文末奇丑无比的`pdf_reader.py`文件.

这样的方法/思路有问题么? 根据需求找到问题所在, 接着通过各种方式找到解决问题的方法, 并实现之. 这样的思路我认为是没有问题的. 但关键在于解决问题的方法有很多, 我们不能仅仅局限于某一种. 比如我这里只想到去找 Python 相关模块去处理 PDF 文档, 而忘记了 Linux/Mac 底下丰富的命令行工具. 的确, 从底层开始手写代码可以了解得更多, 但是一定要放宽视野, 综合了解多种方法, 并比较其优缺点, 然后根据实际情况择优选择, 这样才能提高效率. 
## 了解和使用 pdftotext
可以访问参考资料 1 中的链接访问官网来了解`pdftotext`的详细信息. 这里只需要知道其是一款可以将 PDF 转换为 TXT 格式的命令行工具就可以了(看名字就知道了). 
### Mac 下安装 pdftotext
有了 `brew` 之后安装就会非常简单, 在终端中执行:
```
➜ brew install xpdf
```
或者执行:
```
➜ brew cask install pdftotext
```
注意两个命令择其一即可, 都运行会报错的.
### 转换
首先查看一下`pdftotext`的手册:
```
➜ pdftotext
pdftotext version 4.00
Copyright 1996-2017 Glyph & Cog, LLC
Usage: pdftotext [options] <PDF-file> [<text-file>]
  -f <int>             : first page to convert
  -l <int>             : last page to convert
  -layout              : maintain original physical layout
  -simple              : simple one-column page layout
  -table               : similar to -layout, but optimized for tables
  -lineprinter         : use strict fixed-pitch/height layout
  -raw                 : keep strings in content stream order
  -fixed <number>      : assume fixed-pitch (or tabular) text
  -linespacing <number>: fixed line spacing for LinePrinter mode
  -clip                : separate clipped text
  -nodiag              : discard diagonal text
  -enc <string>        : output text encoding name
  -eol <string>        : output end-of-line convention (unix, dos, or mac)
  -nopgbrk             : don't insert page breaks between pages
  -bom                 : insert a Unicode BOM at the start of the text file
  -opw <string>        : owner password (for encrypted files)
  -upw <string>        : user password (for encrypted files)
  -q                   : don't print any messages or errors
  -cfg <string>        : configuration file to use in place of .xpdfrc
  -v                   : print copyright and version info
  -h                   : print usage information
  -help                : print usage information
  --help               : print usage information
  -?                   : print usage information
```
重点看某几个选项就可以了, 我用到的有`-enc <string>`、`-nopgbrk`和`-layout`这几个. 可以看到这个命令的使用还是非常简单的.
```
➜ pdftotext -enc UTF-8 -nopgbrk filename.pdf
```
这样就可以在`filename.pdf`所在路径内生成一个同名的 TXT 文件.
### 批量转换
因为`pdftotext`不支持同时处理多个 PDF 文件, 所以为了能够实现批处理功能, 需要通过脚本搞定. 打开终端, 进入放置 PDF 的目录, 运行下面命令:
```
➜ find ./ -name '*.pdf' | while read i; do pdftotext -enc UTF-8 -nopgbrk $i; done
```
## 利用 Python 第三方库 pdfminer
这里还是贴一下使用 pdfminer 来解析 PDF 文件的过程. 因为是照着网上的教程写的, 我就不仔细解释其原理了, 参考资料 3 中的文章写得很详细了.

如果有需要(/ahh), 后面还会对这方面继续深入了解的~
```
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
    files_path = "/Users/huxiaoyang/Desktop/papers/"
    for file in os.listdir(files_path):
        print("正在处理 %s" % file)
        parse(files_path + '/' + file)

if __name__ == '__main__':
    main()
```
## 参考资料
1. [pdftotext(1) - Xpdf](https://www.xpdfreader.com/pdftotext-man.html)
2. [Linux下PDF的操作与转换](http://www.freeoa.net/osuport/desktopap/linux-pdf-operation-transformation_1588.html)
3. [Python使用PDFMiner解析PDF](https://www.cnblogs.com/jamespei/p/5339769.html)
