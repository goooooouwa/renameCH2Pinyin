#!/usr/bin/python

# renameCH2Pinyin.py
# Rename filename from Chinese characters to capitalized pinyin using the
# mapping file and taking out the tone numbers

# 批量更改文件名, 中文 -> 拼音, 原gist: https://gist.github.com/hxinblog/5001033
# 使用参考: http://sunzhen.blogspot.com/2016/05/rename-chinese-filenames-to-pinyin.html

# Origin gist link, which is broken: https://gist.github.com/hxinblog/5001033, 
# Reference: http://sunzhen.blogspot.com/2016/05/rename-chinese-filenames-to-pinyin.html

# 从 'ftp://ftp.cuhk.hk/pub/chinese/ifcss/software/data/Uni2Pinyin.gz' 下载 'uni2pinyin'文件
# 创建voc目录，将要重命名的文件放置于此目录下

# Download 'uni2pinyin' from 'ftp://ftp.cuhk.hk/pub/chinese/ifcss/software/data/Uni2Pinyin.gz'
# Place your files under directory named 'voc'

 
import os
import re
 
# File uni2pinyin is a mapping from hex to Pinyin with a tone number
f = open('uni2pinyin')
wf = f.read() # read the whole mapping file
 
os.chdir('voc') # to rename all files in sub folder 'voc'
myulist = os.listdir(u'.') # read all file names in unicode mode
for x in myulist: # each file name
    filenamePY = ''
    for y in x: # each character
        if 0x4e00 <= ord(y) <= 0x9fff: # Chinese Character Unicode range
            hexCH = (hex(ord(y))[2:]).upper() # strip leading '0x' and change
                                              # to uppercase
            p = re.compile(hexCH+'\t([a-z]+)[\d]*') # define the match pattern
            mp = p.search(wf)
            filenamePY+=mp.group(1).title() # get the pinyin without the tone
                                            # number and capitalize it
        else:
            filenamePY+=y
    print x
    filename = filenamePY
    print filename
    os.rename(x, filename)
os.chdir('..') # go back to the parent folder
