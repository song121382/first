import requests
import codecs
import random
from bs4 import BeautifulSoup
import sys
import importlib
import os

importlib.reload(sys)

book_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
]

global headers
headers = {'User-Agent': random.choice(book_headers)}
server = 'http://www.biquge.cm'

# 星辰变地址
book = 'http://www.biquge.cm/2/2042/'

# 定义存储位置
global save_path
save_path = 'D:/book/星辰变'


# 获取章节内容
def get_contents(chapter):
    req = requests.get(chapter, headers=headers)
    html = req.content
    html_doc = str(html, 'gbk')
    soup = BeautifulSoup(html_doc, 'html.parser')
    texts = soup.find_all('div', id='content')
    # 获取div标签id属性content的内容 \xa0 是不间断空白符 &nbsp;
    content = texts[0].text.replace('\xa0' * 4, '\n')
    return content


# 创建文件夹
def create_file(file_path):
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    #切换路径至上面的文件夹
    os.chdir(file_path)


# 写入文件
# 传入参数为chapter，content；content为需要写入的内容，数据类型为字符串，chapter为写入文件，数据类型为字符串。
# 传入的chapter需如下定义：path= 'G:/星辰变/第五章 修炼功法秘藏.txt'
# f = codecs.open(path, 'a', code)中，’a’表示追加写入txt，可以换成’w’，表示覆盖写入。
# code 表示编码 比如 'utf8'、'gbk'等。
def write_txt(chapter, content, code):
    with codecs.open(chapter, 'a', encoding=code) as f:
        f.write(content)


def main():
    res = requests.get(book, headers=headers)
    html = res.content
    html_doc = str(html, 'gbk')
    # 使用自带的html.parser解析
    soup = BeautifulSoup(html_doc, 'html.parser')
    # 获取所有的章节
    a = soup.find('div', id='list').find_all('a')
    print('总章节数：%d' % len(a))
    for each in a:
        try:
            chapter = server + each.get('href')
            content = get_contents(chapter)
            chapter = save_path + "/" + each.string + ".txt"
            create_file(save_path)
            write_txt(chapter, content, 'utf8')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
